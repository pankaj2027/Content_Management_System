from rest_framework import viewsets, status
from .models import User
from .serializer import UserSerializer
from rest_framework.response import Response


# Registration for the author
class AuthorRegistration(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Your registration has been completed Successfully!!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self,request):
        author_list = User.objects.all()
        serializer = UserSerializer(author_list, many=True )
        return Response(serializer.data)
