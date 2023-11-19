from rest_framework.serializers import ModelSerializer
from trello.models import Card, Note, Board


class BoardSerializer(ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'


class CardSerializer(ModelSerializer):

    class Meta:
        model = Card
        fields = ('name', 'user')


class NoteSerializer(ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'


class UpdateDestroyBoardSerializer(ModelSerializer):

    class Meta:
        model = Board
        fields = ('name',)


class UpdateDestroyCardSerializer(ModelSerializer):

    class Meta:
        model = Card
        fields = ('name',)


class UpdateDestroyNoteSerializer(ModelSerializer):

    class Meta:
        model = Note
        fields = ('text', 'card')
