/* storyvideo seek runtime.
 *
 * There are NO CSS animations in this project. Every moving thing is a pure
 * function of absolute time: seek(t) walks the DOM and writes inline styles.
 * That makes a frame reproducible from t alone -- which is what lets six
 * parallel renderers each jump straight to their own slice of the timeline,
 * and what lets preview.html scrub without rendering anything.
 *
 * Element contract (all times are ABSOLUTE seconds from video start, resolved
 * once by resolve() so seek() never has to think about nesting):
 *
 *   data-in     when it enters            data-dur  how long the entrance takes
 *   data-anim   which entrance            data-out  when it leaves (optional)
 *   data-stagger  on a container: children enter one after another this far apart
 *
 * A scene is <section class="scene" data-start data-end [data-cam]>.
 */

const EASE = {
  linear: p => p,
  smooth: p => p * p * (3 - 2 * p),
  out:    p => 1 - Math.pow(1 - p, 3),
  in:     p => p * p * p,
  // Overshoots past 1 and settles back -- the "lands with weight" feel.
  pop:    p => {
    if (p >= 1) return 1;
    const s = 1.70158 * 1.3;
    const q = p - 1;
    return 1 + q * q * ((s + 1) * q + s);
  },
};

const clamp = (v, a = 0, b = 1) => Math.max(a, Math.min(b, v));

/* Entrances. Each returns the inline style for progress p in [0,1].
 * They must all be identity at p=1 so a settled element is pixel-clean. */
const ANIM = {
  fade:   p => ({ opacity: p }),
  rise:   p => ({ opacity: clamp(p * 1.6), transform: `translateY(${(1 - EASE.out(p)) * 60}px)` }),
  drop:   p => ({ opacity: clamp(p * 1.6), transform: `translateY(${(1 - EASE.out(p)) * -60}px)` }),
  slidel: p => ({ opacity: clamp(p * 1.6), transform: `translateX(${(1 - EASE.out(p)) * -140}px)` }),
  slider: p => ({ opacity: clamp(p * 1.6), transform: `translateX(${(1 - EASE.out(p)) * 140}px)` }),
  pop:    p => ({ opacity: clamp(p * 2.2), transform: `scale(${0.3 + 0.7 * EASE.pop(p)})` }),
  /* A mistake that will not sit still. The amplitude decays with (1-p), so it is
   * identity at p=1 like every other entrance -- a settled element is pixel-clean
   * and a renderer that lands exactly on the end of the entrance sees no wobble. */
  shake:  p => ({ opacity: clamp(p * 3),
                  transform: `translateX(${Math.sin(p * Math.PI * 6) * 30 * (1 - p)}px)` }),
  /* Lands from above the camera rather than growing into it: scale 2.4 down to 1
   * with the tilt straightening out. Used where something ARRIVES with authority
   * -- the correct form, the verdict, the root inside the word. */
  stamp:  p => ({ opacity: clamp(p * 2.6),
                  transform: `scale(${2.4 - 1.4 * EASE.out(p)}) `
                           + `rotate(${(1 - EASE.out(p)) * -8}deg)` }),
  grow:   p => ({ opacity: 1, transform: `scaleY(${EASE.out(p)})` }),
  widen:  p => ({ opacity: 1, transform: `scaleX(${EASE.out(p)})` }),
  none:   () => ({ opacity: 1 }),
};

/* Camera moves. The scene is scaled/translated as a whole so something is
 * always drifting -- with no narration on the track, stillness reads as a
 * frozen video. p is progress through the scene. */
const CAM = {
  hold: () => 'scale(1.0)',
  push: p => `scale(${1.0 + 0.075 * EASE.smooth(p)})`,
  pull: p => `scale(${1.075 - 0.075 * EASE.smooth(p)})`,
  panl: p => `scale(1.05) translateX(${(0.5 - EASE.smooth(p)) * 46}px)`,
  panr: p => `scale(1.05) translateX(${(EASE.smooth(p) - 0.5) * 46}px)`,
  rise: p => `scale(1.05) translateY(${(0.5 - EASE.smooth(p)) * 46}px)`,
  sink: p => `scale(1.05) translateY(${(EASE.smooth(p) - 0.5) * 46}px)`,
};

/* ---- resolve: flatten every relative time into an absolute one, once ----
 *
 * This is the fix for the bug that killed the previous renderer: it drove CSS
 * animations off one global clock, so any child authored with a scene-relative
 * offset rendered blank. Here nesting is resolved up front and seek() only
 * ever sees absolute seconds. */
function resolve(root = document) {
  root.querySelectorAll('.scene').forEach(scene => {
    const start = parseFloat(scene.dataset.start);

    // Children authored relative to their scene.
    scene.querySelectorAll('[data-at]').forEach(el => {
      el.dataset.in = (start + parseFloat(el.dataset.at)).toFixed(4);
      delete el.dataset.at;
    });

    // Karaoke timings. A lit word is NOT an entrance -- every ANIM must be
    // identity at p=1, so none of them can hold a state -- so these live on
    // their own attributes and the entrance loop never sees them.
    scene.querySelectorAll('[data-lit]').forEach(el => {
      el.dataset.litIn = (start + parseFloat(el.dataset.lit)).toFixed(4);
      if (el.dataset.until !== undefined)
        el.dataset.litOut = (start + parseFloat(el.dataset.until)).toFixed(4);
      delete el.dataset.lit;
      delete el.dataset.until;
    });

    // A staggered container deals its children in one at a time.
    scene.querySelectorAll('[data-stagger]').forEach(box => {
      const step = parseFloat(box.dataset.stagger);
      const base = box.dataset.in !== undefined ? parseFloat(box.dataset.in) : start;
      const dur  = box.dataset.childDur ? parseFloat(box.dataset.childDur) : 0.34;
      const kids = [...box.children];
      kids.forEach((kid, i) => {
        if (kid.dataset.in === undefined) kid.dataset.in = (base + i * step).toFixed(4);
        if (kid.dataset.dur === undefined) kid.dataset.dur = dur;
        if (kid.dataset.anim === undefined) kid.dataset.anim = box.dataset.childAnim || 'pop';
      });
      // The container itself must not also animate, or it double-hides its kids.
      delete box.dataset.stagger;
      delete box.dataset.in;
    });
  });
  // Keyframed tracks (bridgekit, 2026-10-29). Same rule as everything above:
  // authored relative to the scene, made absolute here, once.
  root.querySelectorAll('.scene').forEach(scene => {
    const start = parseFloat(scene.dataset.start);
    scene.querySelectorAll('[data-kf]').forEach(el => {
      const kf = JSON.parse(el.dataset.kf);
      for (const k in kf) kf[k] = kf[k].map(([t, v]) => [t + start, v]);
      el._kf = kf;
      delete el.dataset.kf;
      el.dataset.kfa = '1';
    });
  });
  document.body.dataset.resolved = '1';
}

/* ---- keyframed tracks: a thing that MOVES, not a thing that enters ----
 *
 * Added for the bridge puzzles (bridgekit.py), where a person walks across a
 * bridge, a lantern follows a hand and the dark follows the lantern. An
 * entrance cannot hold a state, so these live on their own attribute:
 *
 *   data-kf='{"x":[[t,v],...], "y":..., "s":..., "r":..., "o":...,
 *             "m":..., "n":..., "--var":...}'
 *
 * Piecewise linear between keys and flat outside them -- a pure function of t
 * like everything else here. x/y/s/r build the transform, o is opacity, n is
 * the element's text (floored: a clock never shows a second that has not
 * passed), --var sets a CSS custom property. `m` (0..1) means "walking": it
 * adds a step bounce and a sway driven by the DISTANCE walked, so feet and
 * floor agree at any speed. Never put data-kf and data-at on one element --
 * both write transform. Wrap one in the other instead. */
function track(keys, t) {
  if (t <= keys[0][0]) return keys[0][1];
  const last = keys[keys.length - 1];
  if (t >= last[0]) return last[1];
  for (let i = 1; i < keys.length; i++) {
    const [t1, v1] = keys[i];
    if (t <= t1) {
      const [t0, v0] = keys[i - 1];
      return v0 + (v1 - v0) * ((t - t0) / Math.max(t1 - t0, 1e-6));
    }
  }
  return last[1];
}

function seekKf(scene, t) {
  scene.querySelectorAll('[data-kfa]').forEach(el => {
    const kf = el._kf;
    if (!kf) return;
    const v = {};
    for (const k in kf) v[k] = track(kf[k], t);
    if ('x' in v || 'y' in v || 's' in v || 'r' in v || 'm' in v || 'sx' in v) {
      const x = v.x || 0, m = v.m || 0;
      const ph = x / 21;
      const bob = -Math.abs(Math.sin(ph)) * 9 * m;
      const r = (v.r || 0) + Math.sin(ph) * 2.6 * m;
      el.style.transform = `translate(${x}px, ${(v.y || 0) + bob}px) `
                         + `rotate(${r}deg) scale(${(v.s ?? 1) * (v.sx ?? 1)}, ${v.s ?? 1})`;
    }
    if ('o' in v) el.style.opacity = clamp(v.o);
    if ('n' in v) {
      const txt = String(Math.floor(v.n + 1e-6));
      if (el.textContent !== txt) el.textContent = txt;
    }
    for (const k in v) if (k.startsWith('--')) el.style.setProperty(k, v[k]);
  });
}

function seek(t) {
  if (!document.body.dataset.resolved) resolve();

  document.querySelectorAll('.scene').forEach(scene => {
    const a = parseFloat(scene.dataset.start), b = parseFloat(scene.dataset.end);
    const live = t >= a && t < b;
    scene.style.display = live ? '' : 'none';
    if (!live) return;

    const p = clamp((t - a) / (b - a));
    scene.style.transform = (CAM[scene.dataset.cam] || CAM.hold)(p);

    scene.querySelectorAll('[data-in]').forEach(el => {
      const tin = parseFloat(el.dataset.in);
      const dur = parseFloat(el.dataset.dur || 0.5);
      const fn  = ANIM[el.dataset.anim || 'fade'] || ANIM.fade;

      if (t < tin) { el.style.opacity = 0; el.style.visibility = 'hidden'; return; }
      el.style.visibility = '';

      const st = fn(clamp((t - tin) / Math.max(dur, 1e-6)));
      el.style.opacity   = st.opacity ?? 1;
      el.style.transform = st.transform || '';

      // Optional exit: fade and shrink away over 0.4s.
      if (el.dataset.out !== undefined) {
        const q = clamp((t - parseFloat(el.dataset.out)) / 0.4);
        if (q > 0) {
          el.style.opacity = (st.opacity ?? 1) * (1 - q);
          el.style.transform = `${st.transform || ''} scale(${1 - 0.12 * q})`;
        }
      }
    });

    // Counters do not animate alongside the objects -- they COUNT them.
    // The entrance loop above has already written every element's opacity, so
    // reading it back is free, and the number is a readout of the picture
    // rather than a second animation that can drift out of step with it.
    // That is what makes "every quantity countable on screen" true by
    // construction instead of true by careful authoring.
    scene.querySelectorAll('.counter').forEach(el => {
      const tin = parseFloat(el.dataset.in || scene.dataset.start);
      let v;
      if (el.dataset.counts) {
        v = 0;
        scene.querySelectorAll(el.dataset.counts).forEach(o => {
          if (parseFloat(o.style.opacity || 1) > 0.5) v++;
        });
      } else if (el.dataset.sumOf) {
        // Same idea as counting, but adding each visible thing's own value --
        // walking a boundary and watching the metres pile up.
        v = 0;
        scene.querySelectorAll(el.dataset.sumOf).forEach(o => {
          if (parseFloat(o.style.opacity || 1) > 0.5)
            v += parseFloat(o.dataset.val || 0);
        });
        v = Math.round(v * 100) / 100;
      } else {
        const from = parseFloat(el.dataset.from || 0);
        const to   = parseFloat(el.dataset.to);
        const dur  = parseFloat(el.dataset.countDur || el.dataset.dur || 1);
        v = Math.round(from + (to - from) * clamp((t - tin) / Math.max(dur, 1e-6)));
      }
      if (el.textContent !== String(v)) el.textContent = v;
    });

    // The karaoke highlight: a word is ON while the voice is on it and DONE
    // once the voice has passed. Same shape as .tick below -- a state toggled
    // by time, not an animation -- so it stays a pure function of t and three
    // parallel renderers cannot disagree about which word is lit.
    scene.querySelectorAll('.lite').forEach(el => {
      const a = parseFloat(el.dataset.litIn);
      const b = el.dataset.litOut !== undefined ? parseFloat(el.dataset.litOut) : a;
      el.classList.toggle('on', t >= a && t < b);
      el.classList.toggle('done', t >= b);
    });

    seekKf(scene, t);

    // Dots that tick away a silent thinking beat.
    scene.querySelectorAll('.tick').forEach(el => {
      const tin = parseFloat(el.dataset.in);
      el.classList.toggle('on', t >= tin);
    });
  });
}

window.seek = seek;
window.resolve = resolve;
