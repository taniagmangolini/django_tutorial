"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from polls import views
from snippets import views as snippets


router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'choices', views.ChoiceViewSet)
router.register(r'snippets', snippets.SnippetViewSet)
router.register(r'users', snippets.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# Because we're using viewsets instead of views, we can automatically generate
# the URL conf for our API, by simply registering the viewsets with a router class.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # login
    path('', include(router.urls)),
    #path('', include('snippets.urls')),
    #path('', include('polls.urls'))
]

'''
urlpatterns = [
    #include: referencia a urls.py de outros apps
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
'''