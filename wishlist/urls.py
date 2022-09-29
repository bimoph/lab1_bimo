from django.urls import path
from wishlist.views import show_wishlist, show_wishlistjson, show_filter, register, login_user, logout_user


app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist, name='show_wishlist'),
    path('json/', show_wishlistjson, name='show_wishlistjson'),
    path('json/<int:id>', show_filter, name='show_filter'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

]