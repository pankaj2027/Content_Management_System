from rest_framework import viewsets, status
from .models import User, Content
from .serializer import UserSerializer, ContentSerializers
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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



# This will handle all the CRUD operation for Content
class ContentDetail(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializers

    # Token based Authentication is implimented
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    #  search content by matching terms in title, body, summary and categories. 
    filter_backends = [SearchFilter]
    search_fields = ['title','body','summary','categories']

    # Sets the user profile to the logged in User.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    ''' if user is author then he will see their own content only and if user is admin then he can view, 
        edit and delete all the contents created by multiple authors. '''

    def get_queryset(self):
        user_group =str(self.request.user.groups)        
        if user_group == 'author':                                    
            return self.queryset.filter(user=self.request.user)
        return Content.objects.all()                               
    