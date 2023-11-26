from rest_framework.serializers import ModelSerializer
from trello.models import Card, Note, Board


class BoardSerializer(ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        return Board.objects.create(user=user, **validated_data)


class CardSerializer(ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        return Card.objects.create(user=user, **validated_data)


class NoteSerializer(ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        return Note.objects.create(user=user, **validated_data)


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
