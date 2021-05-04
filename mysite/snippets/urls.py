from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

#Because the API chooses the content type of the
# response based on the client request, it will, by default, return an HTML-formatted representation
urlpatterns = format_suffix_patterns(urlpatterns)