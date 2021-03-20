from django.urls import path,include
from rest_framework import routers
from cms.views import AuthorRegistration, ContentDetail
from rest_framework.authtoken import views as authviews


router = routers.DefaultRouter()

router.register('author_registration', AuthorRegistration, basename='author_registration')
router.register('content_data', ContentDetail, basename='content_author')  
           
urlpatterns = [
    path('', include(router.urls)),
    path('login/',authviews.obtain_auth_token)  
]