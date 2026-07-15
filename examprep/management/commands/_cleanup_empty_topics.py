"""Delete examprep Topics that have no lessons (run via: python manage.py shell < thisfile).

Needed after retitling a topic in a data file: re-importing with --republish creates the
new-titled topic and moves the lessons over, leaving the old title as an empty orphan.
"""
from examprep.models import Topic

empty = [t for t in Topic.objects.all() if not t.lessons.exists()]
for t in empty:
    print('deleting empty topic:', t)
    t.delete()
print('done —', len(empty), 'empty topic(s) removed')
