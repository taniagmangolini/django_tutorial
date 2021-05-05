from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions #para verificar autenticacao de usuarios
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly

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
# ou ainda, e possivel deixar ainda mais enxuto
class SnippetList(generics.ListCreateAPIView) :
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
'''

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows snippets to be viewed or edited.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

