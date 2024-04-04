
from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category_detail'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('save_review/<int:product_id>/', save_review, name='save_review'),
    path('login_registration/', login_registration, name='login_registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('cart/', cart, name='cart'),
    path('my_favourite/', FavouriteProductsView.as_view(), name='my_favourite'),
    path('to_cart/<int:product_id>/<str:action>/', to_cart, name='to_cart'),
    path('add_favourite/<slug:product_slug>/', save_favourite_product, name='add_favourite'),
    path('checkout/', checkout, name='checkout'),
    path('payment/', create_checkout_session, name='payment'),
    path('success/', successPayment, name='success'),
    path('clear_cart/', clear_cart, name='clear_cart'),
    path('profil/', profil, name='profil'),
    path('about.html/', AboutList.as_view(), name='about'),
    path('contact.html/', ContactList.as_view(), name='contact'),
    path('items.html/', ItemsList.as_view(), name='items'),
    path('testimonial.html/', TestimonialList.as_view(), name='testimonial'),




]