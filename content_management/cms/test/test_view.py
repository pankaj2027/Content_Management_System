import json

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from ..models import Content, User
from ..serializer import ContentSerializers
from django.contrib.auth.models import Group



class AuthorRegistationTestcase(APITestCase):

    """ Test module for register a new author """
    def test_registation(self):
        data =    {
                    "email": "pankaj45678@gmail.com",
                    "first_name": "pankaj",
                    "last_name": "chaudhary",
                    "password": "Pankaj@2027",
                    "profile": {
                        "phone": 9099878677,
                        "address": "agra",
                        "city": "Agra",
                        "state": "UTTAR PRADESH",
                        "country": "India",
                        "pincode": 282005
                    }
                }
        response = self.client.post('/author_registration/', data, format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        
    
    """ Test module for list of users """
    def test_user_list(self):
        response = self.client.get(reverse("author_registration-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
 

class ContentTestcase(APITestCase):

    def setUp(self):
        self.groups = Group.objects.create(name='author')
        self.user = User.objects.create_user(username="rahul2027",password = "Pankaj@2027",groups=self.groups)
        self.token = Token.objects.get(user=self.user.id)
        self.api_authentication()
        self.content = Content.objects.create(user=self.user, title= "testing1",body= "testing1", summary="testing1", categories= "chemistry")        
             

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION= "Token " + self.token.key)    
    

    # Test module for adding_content for author 
    def test_AddingContent_By_Author(self):
        data = {                                         
                "title": "testing1",
                "body": "testing1",
                "summary": "testing1",
                "categories": "chemistry",
                # "document": "5_6337082923644092854.pdf",  # I am not able to test file field, so I made Document field  from Content Model as null=True

                }  

        response = self.client.post('/content_data/',data, format='multipart')
     
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'],data['title'])
        self.assertEqual(response.data['user'],str(self.user.id))
        

    # Test module for retrieve_content for author
    def test_Retrieve_AuthorContent(self):
        response = self.client.get(reverse("content_author-detail", kwargs={'pk':self.content.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'],'testing1')

 
    # Test module for update_content for author 
    def test_Update_ValidData_AuthorContent(self):
        response = self.client.put(reverse("content_author-detail",kwargs={"pk":self.content.id}),
                                               {"title": "testing7",
                                                "body": "body empty",
                                                "summary": "testing9",
                                                "categories": "chemistry4"
                                                })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['body'], "body empty")

    # Body field is not null 
    def test_Update_InValidData_AuthorContent(self):
        response = self.client.put(reverse("content_author-detail",kwargs={"pk":self.content.id}),
                                               {"title": "testing7",
                                                # "body": "body empty",
                                                "summary": "testing9",
                                                "categories": "chemistry4"
                                                })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
       


    # Test module for Delete_content for author 
    def test_Delete_AuthorContent(self):
        response = self.client.delete(reverse("content_author-detail", kwargs={'pk':self.content.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        

    # Test module for Delete_content for author  which is not exist
    def test_Delete_AuthorContent_DoesNotExist(self):
        response = self.client.delete(reverse("content_author-detail", kwargs={'pk':9}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        

