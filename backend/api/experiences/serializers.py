from rest_framework import serializers

from backend.api.accounts.serializers import ProfileSerializer

from .models import Experience, Comment, Tag
from .relations import TagRelatedField


class ExperienceSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    description = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)

    # does this experience favorited bt the current user
    favorited = serializers.SerializerMethodField()
    # how many times this experience has been favorited
    favoritesCount = serializers.SerializerMethodField(method_name='get_favorites_count')

    tagList = TagRelatedField(many=True, required=False, source='tags')
    created_at = serializers.SerializerMethodField(method_name='get_created_at')
    updated_at = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Experience
        fields = (
            'author',
            'slug',
            'title',
            'description',
            'body',    
            'favorited',
            'favoritesCount',
            'tagList',
            'created_at',
            'updated_at',
        )

    def create(self, validated_data):
        author = self.context.get('author', None)

        tags = validated_data.pop('tags', [])

        experience = Experience.objects.create(author=author, **validated_data)

        for tag in tags:
            experience.tags.add(tag)

        return experience

    def get_created_at(self, instance):
        return instance.created_at.isoformat()
    
    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()

    def get_favorited(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False

        if not request.user.is_authenticated:
            return False

        return request.user.profile.has_favorited(instance)

    def get_favorites_count(self, instance):
        return instance.favorited_by.count()


class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(required=False)
    created_at = serializers.SerializerMethodField(method_name='get_created_at')
    updated_at = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'body',
            'created_at',
            'updated_at',
        )

    def create(self, validated_data):
        experience = self.context['experience']
        author = self.context['author']

        return Comment.objects.create(
            author=author, experience=experience, **validated_data
        )

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)

    def to_representation(self, obj):
        return obj.tag
