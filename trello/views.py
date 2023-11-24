from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from trello.models import Card, Note, Board
from trello.serializers import (
    CardSerializer, NoteSerializer,
    UpdateDestroyNoteSerializer, UpdateDestroyCardSerializer,
    BoardSerializer, UpdateDestroyBoardSerializer
)


class BoardGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BoardSerializer

    def get(self, request):
        user = request.user.id
        board = Board.objects.filter(user=user)
        serializer_board = self.get_serializer(board, many=True)
        return Response(serializer_board.data)

    def post(self, request):
        serializer_board = self.get_serializer(data=request.data)
        serializer_board.is_valid(raise_exception=True)
        serializer_board.save()
        return Response(serializer_board.data)


class AddCardGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CardSerializer

    def post(self, request):
        data = request.data
        serializer_card = self.get_serializer(data=data)
        serializer_card.is_valid(raise_exception=True)
        serializer_card.save()
        return Response(serializer_card.data)


class AddNoteGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NoteSerializer

    def post(self, request):
        serializer_note = self.get_serializer(data=request.data)
        serializer_note.is_valid(raise_exception=True)
        serializer_note.save()
        return Response(serializer_note.data)


class UpdateDestroyBoardGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateDestroyBoardSerializer

    def patch(self, request, pk):
        user = request.user.id
        board = Board.objects.get(Q(user=user) & Q(pk=pk))
        serializer_board = self.get_serializer(board, request.data, partial=True)
        serializer_board.is_valid(raise_exception=True)
        serializer_board.save()
        return Response(serializer_board.data)

    def delete(self, request, pk):
        user = request.user.id
        board = Board.objects.get(Q(user=user) & Q(pk=pk))

        try:
            board.delet()
        except Exception as e:
            return Response({'success': False, 'message': str(e)})
        return Response(status=204)


class UpdateDestroyCardGenericAPIView(GenericAPIView):
    queryset = Card.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateDestroyCardSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Card.objects.filter(Q(user=user))

    def patch(self, request, pk):
        card = self.get_object()
        print(request)
        serializer_card = self.get_serializer(card, request.data, partial=True)
        serializer_card.is_valid(raise_exception=True)
        serializer_card.save()
        return Response(serializer_card.data)

    def delete(self, request, pk):
        card = self.get_object()

        try:
            card.delete()
        except Exception as e:
            return Response({'success': False, 'message': str(e)})
        return Response(status=204)


class UpdateDestroyNoteGenericAPIView(GenericAPIView):
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
