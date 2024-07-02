from django.urls import path
from .views import amocrm_chats

urlpatterns = [
    # mainpage
    path('<slug:scope_id>', amocrm_chats),
]