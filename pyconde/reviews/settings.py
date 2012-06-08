from django.conf import settings


ENABLE_COMMENT_NOTIFICATIONS = getattr(settings, 'REVIEWS_ENABLE_COMMENT_NOTIFICATIONS', True)
ENABLE_PROPOSAL_UPDATE_NOTIFICATIONS = getattr(settings, 'REVIEW_ENABLE_PROPOSAL_UPDATE_NOTIFICATIONS', True)

PROPOSAL_UPDATE_FORMS = getattr(settings, 'REVIEWS_PROPOSAL_UPDATE_FORMS', {
    'talk': 'pyconde.reviews.forms.UpdateTalkProposalForm',
    'tutorial': 'pyconde.reviews.forms.UpdateTutorialProposalForm',
    })
