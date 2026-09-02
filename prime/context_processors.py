from django.utils.functional import SimpleLazyObject

from .social import CONTACT_EMAIL, SOCIAL_LINKS, SOCIAL_MAP, SOCIAL_PROFILE_URLS
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


def social(request):
    """Official accounts (see prime/social.py) for the sidebar, About and Help."""
    return {
        'social_links': SOCIAL_LINKS,
        'social': SOCIAL_MAP,
        'contact_email': CONTACT_EMAIL,
        'social_profile_urls': SOCIAL_PROFILE_URLS,
    }
