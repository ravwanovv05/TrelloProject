from django.urls import path

from trello.views import AddCardGenericAPIView, UpdateDestroyNoteGenericAPIView, UpdateDestroyCardGenericAPIView, \
    AddNoteGenericAPIView

urlpatterns = [
    path('add-card', AddCardGenericAPIView.as_view(), name='add_card'),
    path('add-note', AddNoteGenericAPIView.as_view(), name='add_note'),
    path('updatedestroynote/<int:pk>', UpdateDestroyNoteGenericAPIView.as_view(), name='update_destroy_note'),
    path('updatedestroycard/<int:pk>', UpdateDestroyCardGenericAPIView.as_view(), name='update_destroy_note'),
]
