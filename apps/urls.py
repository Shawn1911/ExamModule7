from django.urls import path

from apps.views import IndexView, UserDeleteView, UserUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update'),
]
