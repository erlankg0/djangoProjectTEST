from django.urls import path
from app.views import Home, SAPListView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('table/', SAPListView.as_view(), name='table'),
]
