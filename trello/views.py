from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from trello.models import Card, Note
from trello.serializers import CardSerializer, NoteSerializer, UpdateDestroyNoteSerializer, UpdateDestroyCardSerializer


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
        serializer_note.save()
        return Response(serializer_note.data)


class UpdateDestroyCardGenericAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateDestroyCardSerializer

    def patch(self, request, pk):
        user = request.user.id
        card = Card.objects.get(Q(user=user) & Q(pk=pk))
        serializer_card = self.get_serializer(card, request.data, partial=True)
        serializer_card.is_valid(raise_exception=True)
        serializer_card.save()
        return Response(serializer_card.data)

    def delete(self, request, pk):
        user = request.user.id
        card = Card.objects.get(Q(user=user) & Q(pk=pk))

        try:
            card.delete()
        except Exception as e:
            return Response({'success': False, 'message': str(e)})
        return Response(status=204)


class UpdateDestroyNoteGenericAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateDestroyNoteSerializer

    def patch(self, request, pk):
        user = request.user.id
        note = Note.objects.get(Q(user=user) & Q(pk=pk))
        serializer_note = self.get_serializer(note, request.data, partial=True)
        serializer_note.is_valid(raise_exception=True)
        serializer_note.save()
        return Response(serializer_note.data)

    def delete(self, request, pk):
        user = request.user.id
        note = Note.objects.get(Q(user=user) & Q(pk=pk))

        try:
            note.delete()
        except Exception as e:
            return Response({'success': False, 'message': str(e)})
        return Response(status=204)
