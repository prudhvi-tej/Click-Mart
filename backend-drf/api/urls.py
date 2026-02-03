from django.urls import path,include
from users import views as UserViews
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView 
from products import views as Productviews
from carts import views as CartViews
from orders import views as OrderViews

urlpatterns=[
    path('register/',UserViews.Registerview.as_view()),

    # USER APIS
    path('token/',TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name ='token_refresh'),
    path('profile/',UserViews.Profileview.as_view()),


    # PRODUCT APIS
    path('products/',Productviews.ProductListView.as_view()),
    path('products/<int:pk>/',Productviews.ProductDetailView.as_view()),
    

    # CART APIS
    path('cart/',CartViews.CartView.as_view()),

    # AddtoCart API
    path('cart/add/',CartViews.AddtoCart.as_view()),

    # Manage Quantity
    path('cart/items/<int:item_id>/',CartViews.ManageQuantity.as_view()),
     
     # Orders
     path('orders/place/',OrderViews.PlaceOrderView.as_view()),
     path('orders/',OrderViews.MyOrderView.as_view()),
     
     

]