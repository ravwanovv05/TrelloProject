from django.urls import path

from trello.views import AddCardGenericAPIView, UpdateDestroyNoteGenericAPIView

urlpatterns = [
    path('add-card', AddCardGenericAPIView.as_view(), name='add_card'),
    path('updatedestroynote/<int:pk>', UpdateDestroyNoteGenericAPIView.as_view(), name='update_destroy_note'),
]
