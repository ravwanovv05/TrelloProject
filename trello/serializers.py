from rest_framework.serializers import ModelSerializer
from trello.models import Card, Note


class CardSerializer(ModelSerializer):

    class Meta:
        model = Card
        fields = ('name', 'user')


class NoteSerializer(ModelSerializer):

    class Meta:
        model = Note
        fields = ('text', 'card')

