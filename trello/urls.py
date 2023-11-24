from django.urls import path

from trello.views import AddCardGenericAPIView, UpdateDestroyNoteGenericAPIView, UpdateDestroyCardGenericAPIView, \
    AddNoteGenericAPIView, BoardGenericAPIView, UpdateDestroyBoardGenericAPIView

urlpatterns = [
    path('board', BoardGenericAPIView.as_view(), name='add_board'),
    path('add-card', AddCardGenericAPIView.as_view(), name='add_card'),
    path('add-note', AddNoteGenericAPIView.as_view(), name='add_note'),
    path('updatedestroyboard/<int:pk>', UpdateDestroyBoardGenericAPIView.as_view(), name='update_destroy_board'),
    path('updatedestroynote/<int:pk>', UpdateDestroyNoteGenericAPIView.as_view(), name='update_destroy_note'),
    path('updatedestroycard/<int:pk>', UpdateDestroyCardGenericAPIView.as_view(), name='update_destroy_note'),
]
