from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Card(models.Model):
    name = models.CharField('Name', max_length=255)
    user = models.ForeignKey(User, models.CASCADE, verbose_name='User')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = ('Card',)
        verbose_name_plural = ('Cards',)


class Note(models.Model):
    text = models.TextField(verbose_name='Text')
    user = models.ForeignKey(User, models.CASCADE, verbose_name='User')
    card = models.ForeignKey(Card, models.CASCADE, verbose_name='Card')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = ('Note',)
        verbose_name_plural = ('Notes',)

