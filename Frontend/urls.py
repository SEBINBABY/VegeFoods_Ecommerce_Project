from django.urls import path
from Frontend import views

urlpatterns = [
    path('Homepage/', views.Homepage, name='Homepage'),
    path('ProductsPage/<catname>/', views.ProductsPage, name='ProductsPage'),
    path('AboutPage/', views.AboutPage, name='AboutPage'),
    path('ContactPage/', views.ContactPage, name='ContactPage'),


    path('SignUpLoginPage/', views.SignUpLoginPage, name='SignUpLoginPage'),
    path('UserRegistrationDBsave/', views.UserRegistrationDBsave, name='UserRegistrationDBsave'),
    path('UserLogin/', views.UserLogin, name='UserLogin'),
    path('UserLogout/', views.UserLogout, name='UserLogout'),

    path('FrontendBlog/', views.FrontendBlog, name='FrontendBlog'),
    path('SingleProduct/<int:proid>/', views.SingleProduct, name='SingleProduct'),
    path('ContactPage_save/', views.ContactPage_save, name='ContactPage_save'),
    path('BlogSingle/<int:blogid>/', views.BlogSingle, name='BlogSingle'),

    path('cartDBsave/', views.cartDBsave, name='cartDBsave'),
    path('cart_page/', views.cart_page, name='cart_page'),
    path('Checkout/', views.Checkout, name='Checkout'),
    path('CheckoutDBsave/', views.CheckoutDBsave, name='CheckoutDBsave'),
    path('cartDelete/<int:cartid>/', views.cartDelete, name='cartDelete'),
]