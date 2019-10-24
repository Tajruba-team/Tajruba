from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    ExperienceViewSet, ExperienceFavoriteAPIView,
    CommentsListCreateAPIView, CommentsDestroyAPIView, TagListAPIView
)

router = DefaultRouter(trailing_slash=True)
router.register(r'experiences', ExperienceViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('experiences/<experience_slug>/favorite/',ExperienceFavoriteAPIView.as_view()),
    path('experiences/<experience_slug>/comments/', CommentsListCreateAPIView.as_view()),
    path('experiences/<article_slug>/comments/<comment_pk>/',CommentsDestroyAPIView.as_view()),
    path('tags/', TagListAPIView.as_view()),
]
