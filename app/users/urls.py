from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login_view'),
    path('items/', views.ToDoItemCreateListView.as_view(), name='create_todo_item'),
    path('items/<int:pk>/', views.ToDoItemCreateListView.as_view(),
         name='create_todo_item'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
