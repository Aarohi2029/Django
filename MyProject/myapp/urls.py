from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blog_list/',views.blog_list,name='blog_list'),
    path('contact/',views.contact,name='contact'),
    path('product/',views.product,name='product'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('change-password/',views.change_password,name='change-password'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('update-password/',views.update_password,name='update-password'),
    path('add-product/',views.add_product,name='add-product'),
    path('view-product/',views.view_product,name='view-product'),
    path('seller-product-details/<int:pk>/',views.seller_product_details,name='seller-product-details'),
    path('seller-product-edit/<int:pk>/',views.seller_product_edit,name='seller-product-edit'),
    path('seller-product-delete/<int:pk>/',views.seller_product_delete,name='seller-product-delete'),
    path('product-details/<int:pk>/',views.product_details,name='product-details'),
    path('add-to-wishlist/<int:pk>/',views.add_to_wishlist,name='add-to-wishlist'),
    path('wishlist/',views.wishlist,name='wishlist'),



]