from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions #para verificar autenticacao de usuarios
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action using the @action decorator
   -  ModelViewSet class provides a complete set of default read and write operations.
    - Custom actions which use the @action decorator will respond to GET requests by default.
      We can use the methods argument if we wanted an action that responded to POST requests.
      url_path is a decorator keyword argument that permits to especify the custom action's url.
   - This viewset replaces the SnippetList, SnippetDetail and SnippetHighlight view classes.
     We can remove the three views, and again replace them with this single class.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

'''
#Using mixins for reusability
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    #sobrescrever o metodo abaixo para obter o usuario do request e associá-lo ao snippet serializado
    def perform_create(self, serializer) :
        serializer.save(owner=self.request.user)
'''

'''
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView) :

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs) :
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs) :
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs) :
        return self.destroy(request, *args, **kwargs)
'''

'''
# ou ainda, e possivel deixar ainda mais enxuto
class SnippetList(generics.ListCreateAPIView) :
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
'''
'''
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
'''

'''
#ViewSet classes are almost the same thing as View classes,
# except that they provide operations such as retrieve, or update
# Provides only readonly operations if it is an ReadOnlyModelViewSet
class SnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows snippets to be viewed or edited.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
'''

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    it is a refactor our UserList and UserDetail views into a single UserViewSet.
     We can remove the two views, and replace them with a single class:
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


'''
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
'''

