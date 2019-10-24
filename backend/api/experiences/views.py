from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Experience, Comment, Tag
from .renderers import ExperienceJSONRenderer, CommentJSONRenderer
from .serializers import ExperienceSerializer, CommentSerializer, TagSerializer


class ExperienceViewSet(mixins.CreateModelMixin, 
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    lookup_field = 'slug'
    queryset = Experience.objects.select_related('author', 'author__user')
    permission_classes = (IsAuthenticatedOrReadOnly, )
    renderer_classes = (ExperienceJSONRenderer,)
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        queryset = self.queryset

        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = queryset.filter(author__user__username=author)

        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            queryset = queryset.filter(tags__tag=tag)

        favorited_by = self.request.query_params.get('favorited', None)
        if favorited_by is not None:
            queryset = queryset.filter(
                favorited_by__user__username=favorited_by
            )

        return queryset

    def create(self, request):
        serializer_context = {
            'author': request.user.profile,
            'request': request
        }
        serializer_data = request.data.get('experience', {})

        serializer = self.serializer_class(
        data=serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )

        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, slug):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Experience.DoesNotExist:
            raise NotFound('An experience with this slug does not exist.')

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


    def update(self, request, slug):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Experience.DoesNotExist:
            raise NotFound('An experience with this slug does not exist.')
            
        serializer_data = request.data.get('experience', {})

        serializer = self.serializer_class(
            serializer_instance, 
            context=serializer_context,
            data=serializer_data, 
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentsListCreateAPIView(generics.ListCreateAPIView):
    lookup_field = 'experience__slug'
    lookup_url_kwarg = 'experience_slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.select_related(
        'experience', 'experience__author', 'experience__author__user',
        'author', 'author__user'
    )
    renderer_classes = (CommentJSONRenderer,)
    serializer_class = CommentSerializer

    def filter_queryset(self, queryset):
        # The built-in list function calls `filter_queryset`. Since we only
        # want comments for a specific article, this is a good place to do
        # that filtering.
        filters = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}

        return queryset.filter(**filters)

    def create(self, request, experience_slug=None):
        data = request.data.get('comment', {})
        context = {'author': request.user.profile}

        try:
            context['experience'] = Experience.objects.get(slug=experience_slug)
        except Experience.DoesNotExist:
            raise NotFound('An experience with this slug does not exist.')

        serializer = self.serializer_class(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentsDestroyAPIView(generics.DestroyAPIView):
    lookup_url_kwarg = 'comment_pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()

    def destroy(self, request, experience_slug=None, comment_pk=None):
        try:
            comment = Comment.objects.get(pk=comment_pk)
        except Comment.DoesNotExist:
            raise NotFound('A comment with this ID does not exist.')

        comment.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ExperienceFavoriteAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ExperienceJSONRenderer,)
    serializer_class = ExperienceSerializer

    def delete(self, request, experience_slug=None):
        profile = self.request.user.profile
        serializer_context = {'request': request}

        try:
            experience = Experience.objects.get(slug=experience_slug)
        except Experience.DoesNotExist:
            raise NotFound('An experience with this slug was not found.')

        profile.unfavorite(experience)

        serializer = self.serializer_class(experience, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, experience_slug=None):
        import pdb; pdb.set_trace()
        
        profile = self.request.user.profile
        serializer_context = {'request': request}

        try:
            experience = Experience.objects.get(slug=experience_slug)
        except Experience.DoesNotExist:
            raise NotFound('An experience with this slug was not found.')

        profile.favorite(experience)

        serializer = self.serializer_class(experience, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    pagination_class = None
    permission_classes = (AllowAny,)
    serializer_class = TagSerializer

    def list(self, request):
        serializer_data = self.get_queryset()
        serializer = self.serializer_class(serializer_data, many=True)

        return Response({
            'tags': serializer.data
        }, status=status.HTTP_200_OK)
