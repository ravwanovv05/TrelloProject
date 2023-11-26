from django.contrib import admin
from trello.models import Board, Card, Note, Template


@admin.register(Board)
class AdminBoard(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'created_at')


@admin.register(Card)
class AdminCard(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'board', 'created_at')


@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'card', 'created_at')


@admin.register(Template)
class AdminTemplate(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description', 'created_at')

