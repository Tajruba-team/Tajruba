from django.db import models

from backend.api.core.models import TimestampedModel
from backend.api.accounts.models import Profile


class Experience(TimestampedModel):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    tags = models.ManyToManyField('experiences.Tag', related_name='experiences')

    def __str__(self):
        return self.title


class Comment(TimestampedModel):
    body = models.TextField()
    experience = models.ForeignKey('experiences.Experience', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, related_name='comments', on_delete=models.CASCADE)


class Tag(TimestampedModel):
    tag = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return self.tag
