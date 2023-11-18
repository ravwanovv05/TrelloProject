from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from trello.models import Card, Note
from trello.serializers import CardSerializer, NoteSerializer


class AddCardGenericAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CardSerializer

    def post(self, request):
        data = request.data
        serializer_card = self.get_serializer(data=data)
        serializer_card.is_valid(raise_exception=True)
        serializer_card.save()
        return Response(serializer_card.data)


class AddNoteGenericAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NoteSerializer

    def post(self, request):
        serializer_note = self.get_serializer(data=request.data)
        serializer_note.is_valid(raise_exception=True)
        serializer_note.savae()
        return Response(serializer_note.data)


class UpdateDestroyNoteGenericAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NoteSerializer

    def get_object(self, pk, user):
        return Note.objects.get(Q(user=user) & Q(pk=pk))

    def patch(self, request, pk):
        card = self.get_object(pk, request.user.id)
        serializer_card = self.get_serializer(card, request.data, partial=True)
        serializer_card.is_valid(raise_exception=True)
        serializer_card.save()
        return Response(serializer_card.data)

    def delete(self, request, pk):
        note = Note.objects.get(pk=pk)

        try:
            note.delete()
        except Exception as e:
            return Response({'success': False, 'message': str(e)})
        return Response(status=204)
