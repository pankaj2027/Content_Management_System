from django.urls import path,include
from rest_framework import routers
from cms.views import AuthorRegistration
from rest_framework.authtoken import views as authviews


router = routers.DefaultRouter()

router.register('author_registration', AuthorRegistration, basename='author_registration')  
           
urlpatterns = [
    path('', include(router.urls)),
    path('login/',authviews.obtain_auth_token)  
]