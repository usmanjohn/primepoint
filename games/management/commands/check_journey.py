"""Prime Journey's safety gate.

Prime Math has an arithmetic gate because a wrong answer key is the worst bug
that course can ship. Prime Journey's equivalent worst bug is a **road that
cannot be walked**: an obstacle whose lesson has no question left to ask, a
fork with one branch, a guardian with nothing to review. A pupil hitting one of
those is simply stuck, with no way forward and no way back.

So every road is built here across many seeds and every node is checked before
anything reaches a pupil. Run it after touching `games/journey.py`, after
importing new lessons, and before deploying:

    python manage.py check_journey
    python manage.py check_journey --seeds=200 --road=math
"""
from django.core.management.base import BaseCommand

from games import journey


VALID_KINDS = {'gate', 'twin', 'camp', 'chest', 'elder', 'guard'}


class Command(BaseCommand):
    help = 'Build every Prime Journey map across many seeds and prove each one is walkable.'

    def add_arguments(self, parser):
        parser.add_argument('--seeds', type=int, default=50,
                            help='Maps to build per road+leg (default 50).')
        parser.add_argument('--road', default='',
                            help='Check one road only (math/english/korean/russian).')
        parser.add_argument('--questions', action='store_true',
                            help='Also draw a real question at every threat for every '
                                 'lesson on the road. Slower, and worth it before a deploy.')

    def handle(self, *args, **options):
        seeds = options['seeds']
        roads = [options['road']] if options['road'] else journey.ROAD_SLUGS
        problems = []
        maps_built = nodes_checked = 0

        for road in roads:
            if road not in journey.ROAD_MAP:
                problems.append(f'{road}: no such road')
                continue

            lessons = journey.road_lessons(road)
            legs = journey.leg_count(road)
            self.stdout.write(
                f"{journey.ROAD_MAP[road]['emoji']}  {road}: "
                f'{len(lessons)} usable lessons, {legs} legs')

            if not lessons:
                problems.append(f'{road}: no lesson on this road can supply a question')
                continue

            for leg in range(1, legs + 1):
                leg_lessons = journey.leg_lessons(road, leg)
                if not leg_lessons:
                    problems.append(f'{road} leg {leg}: no lessons')
                    continue

                for seed in range(seeds):
                    game_map = journey.build_map(road, leg, seed)
                    maps_built += 1
                    where = f'{road} leg {leg} seed {seed}'

                    if not game_map:
                        problems.append(f'{where}: empty map')
                        continue

                    ids = set()
                    kinds = []
                    for index, step in enumerate(game_map):
                        if not step:
                            problems.append(f'{where}: step {index} has no nodes')
                            continue
                        if len(step) > 3:
                            problems.append(f'{where}: step {index} forks {len(step)} ways')

                        for node in step:
                            nodes_checked += 1
                            kinds.append(node['kind'])
                            problems += self._check_node(where, index, node, ids)

                    # A leg has to end at its guardian, and the guardian has to
                    # have something to review.
                    if kinds[-1:] != ['guard']:
                        problems.append(f'{where}: the road does not end at a guardian')
                    if not any(k in ('gate', 'twin') for k in kinds):
                        problems.append(f'{where}: nothing stands in the way anywhere')

                    # Every lesson of the leg must appear, or the road quietly
                    # skips teaching material.
                    covered = {n.get('lesson') for step in game_map for n in step}
                    missing = [l['title'] for l in leg_lessons if l['id'] not in covered]
                    if missing:
                        problems.append(f'{where}: lessons never met — {", ".join(missing)}')

            if options['questions']:
                problems += self._check_questions(road, lessons)

        self.stdout.write('')
        self.stdout.write(f'{maps_built} maps built, {nodes_checked} nodes checked.')

        if problems:
            self.stdout.write(self.style.ERROR(f'\n{len(problems)} problem(s):'))
            for line in problems[:40]:
                self.stdout.write(self.style.ERROR(f'  ✗ {line}'))
            if len(problems) > 40:
                self.stdout.write(self.style.ERROR(f'  … and {len(problems) - 40} more'))
            raise SystemExit(1)

        self.stdout.write(self.style.SUCCESS('Every road is walkable. ✓'))

    # ------------------------------------------------------------------
    def _check_node(self, where, index, node, ids):
        problems = []
        node_id = node.get('id')

        if not node_id:
            problems.append(f'{where}: step {index} has a node with no id')
        elif node_id in ids:
            problems.append(f'{where}: duplicate node id {node_id}')
        else:
            ids.add(node_id)

        if node['kind'] not in VALID_KINDS:
            problems.append(f'{where}: {node_id} has unknown kind {node["kind"]!r}')

        if node['terrain'] not in journey.TERRAINS:
            problems.append(f'{where}: {node_id} is in unknown terrain {node["terrain"]!r}')

        cast = journey.ENCOUNTER_MAP.get(node['encounter'])
        if cast is None:
            problems.append(f'{where}: {node_id} names a missing encounter '
                            f'{node["encounter"]!r}')
        elif node['kind'] not in cast['kinds']:
            problems.append(f'{where}: {node_id} uses "{node["encounter"]}" as a '
                            f'{node["kind"]}, which it cannot serve')

        if node['kind'] in ('gate', 'twin', 'guard'):
            if not node.get('lesson'):
                problems.append(f'{where}: {node_id} blocks the road but teaches nothing')
            if node.get('threat') not in (1, 2, 3):
                problems.append(f'{where}: {node_id} has threat {node.get("threat")!r}')
            if journey.node_coins(node) <= 0:
                problems.append(f'{where}: {node_id} pays nothing')

        if node['kind'] == 'guard' and not node.get('sources'):
            problems.append(f'{where}: {node_id} is a guardian with nothing to review')

        return problems

    # ------------------------------------------------------------------
    def _check_questions(self, road, lessons):
        """The expensive check: every lesson must answer at every threat, even
        for a traveller who has already seen its whole bank."""
        problems = []
        for lesson in lessons:
            for threat in (1, 2, 3):
                question = journey.pick_question(lesson['id'], threat, [])
                if question is None:
                    problems.append(f'{road}: "{lesson["title"]}" has no question '
                                    f'at threat {threat}')
                    continue
                if question.get('correct') is None:
                    problems.append(f'{road}: "{lesson["title"]}" Q{question["qid"]} '
                                    f'has no correct choice marked')
                if len(question.get('choices') or []) < 2:
                    problems.append(f'{road}: "{lesson["title"]}" Q{question["qid"]} '
                                    f'has fewer than two choices')

            # …and the case that actually strands people: a pupil who has met
            # everything this lesson has. The fallback chain must still answer.
            from tutorial.models import Tutorial
            tutorial = Tutorial.objects.filter(id=lesson['id']).first()
            practice = next((p for p in tutorial.practices.all() if p.is_published), None)
            all_ids = list(practice.questions.values_list('id', flat=True)) if practice else []
            if all_ids and journey.pick_question(lesson['id'], 3, all_ids) is None:
                problems.append(f'{road}: "{lesson["title"]}" strands a traveller who '
                                f'has seen its whole bank')
        return problems
