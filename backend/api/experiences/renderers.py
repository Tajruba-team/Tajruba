from backend.api.core.renderers import TajrubaJSONRenderer


class ExperienceJSONRenderer(TajrubaJSONRenderer):
    object_label = 'experience'
    pagination_object_label = 'experiences'
    pagination_count_label = 'experiencesCount'


class CommentJSONRenderer(TajrubaJSONRenderer):
    object_label = 'comment'
    pagination_object_label = 'comments'
    pagination_count_label = 'commentsCount'
