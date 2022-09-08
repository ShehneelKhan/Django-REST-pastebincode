from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetList,SnippetDetail, UserDetail, UserList, SnippetHighlight
from snippets import views

urlpatterns = [
    path('snippets/',SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/',SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('', views.api_root)
]

urlpatterns = format_suffix_patterns(urlpatterns)