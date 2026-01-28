from django.urls import path,include
from users import views as Userviews
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView 


urlpatterns=[
    path('register/',Userviews.Registerview.as_view()),

    # USER APIS
    path('token/',TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name ='token_refresh'),
    path('profile/',Userviews.Profileview.as_view())

]