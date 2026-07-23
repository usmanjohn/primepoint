from django.utils.functional import SimpleLazyObject

from .subjects import SUBJECTS, SUBJECT_MAP, get_study_subjects, has_chosen_subjects


def study_subjects(request):
    return {
        'all_study_subjects': SUBJECTS,
        'study_subject_slugs': SimpleLazyObject(lambda: get_study_subjects(request)),
        'study_subjects_chosen': SimpleLazyObject(lambda: has_chosen_subjects(request)),
        'my_study_subjects': SimpleLazyObject(
            lambda: [SUBJECT_MAP[s] for s in (get_study_subjects(request) or [])]
        ),
    }
