from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Board(models.Model):
    name = models.CharField(max_length=255, verbose_name='Board')
    user = models.ForeignKey(User, models.CASCADE, verbose_name='User')
    template = models.ForeignKey('Template', on_delete=models.SET_NULL, null=True, verbose_name='Template')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'


class Card(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    user = models.ForeignKey(User, models.CASCADE, verbose_name='User')
    board = models.ForeignKey(Board, models.CASCADE, verbose_name='Board')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'


class Note(models.Model):
    text = models.TextField(verbose_name='Text')
    user = models.ForeignKey(User, models.CASCADE, verbose_name='User')
    card = models.ForeignKey(Card, models.CASCADE, verbose_name='Card')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'


class Template(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    image = models.ImageField(upload_to='pics', verbose_name='Template')
    description = models.TextField(verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'
