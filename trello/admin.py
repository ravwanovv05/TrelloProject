from django.contrib import admin
from .models import Board, Card, Note


@admin.register(Board)
class AdminBoard(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'created_at')


@admin.register(Card)
class AdminCard(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'board', 'created_at')


@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'card', 'created_at')


