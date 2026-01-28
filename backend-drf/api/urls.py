from django.urls import path,include
from users import views as Userviews
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView 
from products import views as Productviews

urlpatterns=[
    path('register/',Userviews.Registerview.as_view()),

    # USER APIS
    path('token/',TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name ='token_refresh'),
    path('profile/',Userviews.Profileview.as_view()),


    # PRODUCT APIS
    path('products/',Productviews.ProductListView.as_view()),
    path('products/<int:pk>/',Productviews.ProductDetailView.as_view()),
    

]