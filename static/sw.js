const CACHE = 'powerty-v7';

// Self-hosted shell assets only. These used to point at jsDelivr, but the site
// stopped loading Bootstrap from a CDN — and one failed request makes addAll()
// reject, which aborts the whole install and leaves the app un-installable.
const PRECACHE = [
    '/static/css/style.css',
    '/static/vendor/bootstrap.min.css',
    '/static/vendor/bootstrap-icons.min.css',
    '/static/vendor/bootstrap.bundle.min.js',
    '/static/vendor/fonts/bootstrap-icons.woff2',
    '/static/favicon/favicon-32x32.png',
    '/static/icons/icon-192.png',
];

self.addEventListener('install', e => {
    e.waitUntil(
        caches.open(CACHE)
            // Cache each asset on its own so a single 404 can't abort the install.
            .then(c => Promise.all(PRECACHE.map(u =>
                c.add(new Request(u, { cache: 'reload' })).catch(() => null)
            )))
            .then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', e => {
    e.waitUntil(
        caches.keys()
            .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
            .then(() => self.clients.claim())
    );
});

self.addEventListener('fetch', e => {
    if (e.request.method !== 'GET') return;
    if (!e.request.url.startsWith('http')) return;
    if (e.request.url.includes('/admin/')) return;
    if (e.request.url.includes('/ckeditor5/')) return;

    // Never cache HTML navigation — always fetch fresh so auth state and CSRF tokens are correct
    if (e.request.mode === 'navigate') {
        e.respondWith(
            fetch(e.request).catch(() => caches.match(e.request))
        );
        return;
    }

    // Static assets: cache-first, update in background
    e.respondWith(
        caches.match(e.request).then(cached => {
            const network = fetch(e.request).then(res => {
                if (res.ok) {
                    const clone = res.clone();
                    caches.open(CACHE).then(c => c.put(e.request, clone));
                }
                return res;
            }).catch(() => cached);
            return cached || network;
        })
    );
});
