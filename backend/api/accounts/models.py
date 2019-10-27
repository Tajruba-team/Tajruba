from django.db import models
from django.contrib.auth.models import User


class Settings(models.Model):
    notify_when_reply = models.IntegerField()
    notify_when_comment = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    settings = models.OneToOneField(Settings, on_delete=models.CASCADE, blank=True, null=True)

    bio = models.TextField(max_length=200, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    job = models.CharField(max_length=50, blank=True, null=True)
    favorites = models.ManyToManyField('experiences.Experience', related_name='favorited_by')

    def __str__(self):
        return self.user.username

    def favorite(self, experience):
        self.favorites.add(experience)

    def unfavorite(self, experience):
        self.favorites.remove(experience)

    def has_favorited(self, experience):
        return self.favorites.filter(pk=experience.pk).exists()
