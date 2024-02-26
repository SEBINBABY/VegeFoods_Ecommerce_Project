from django.urls import path
from Backend import views

urlpatterns = [
    path('indexpage/', views.indexpage, name='indexpage'),
    path('AddCategory/', views.AddCategory, name='AddCategory'),
    path('categorysave/', views.categorysave, name='categorysave'),
    path('displaycat/', views.displaycat, name='displaycat'),
    path('editcategory/<int:catid>/', views.editcategory, name='editcategory'),
    path('updatecategory/<int:catid>/', views.updatecategory, name='updatecategory'),
    path('deletecategory/<int:catid>/', views.deletecategory, name='deletecategory'),
# ******************************************************************************************************************
    path('AddProduct/', views.AddProduct, name='AddProduct'),
    path('productsave/', views.productsave, name='productsave'),
    path('displayproduct/', views.displayproduct, name='displayproduct'),
    path('editproduct/<int:proid>/', views.editproduct, name='editproduct'),
    path('updateproduct/<int:proid>/', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<int:proid>/', views.deleteproduct, name='deleteproduct'),
# ******************************************************************************************************************
    path('AddBlog/', views.AddBlog, name='AddBlog'),
    path('Blogsave/', views.Blogsave, name='Blogsave'),
    path('BlogDisplay/', views.BlogDisplay, name='BlogDisplay'),
    path('editblog/<int:blogid>/', views.editblog, name='editblog'),
    path('updateblog/<int:blogid>/', views.updateblog, name='updateblog'),
    path('deleteblog/<int:blogid>/', views.deleteblog, name='deleteblog'),
# ******************************************************************************************************************
    path('admin_login_page/', views.admin_login_page, name='admin_login_page'),
    path('AdminLogin/', views.AdminLogin, name='AdminLogin'),
    path('AdminLogout/', views.AdminLogout, name='AdminLogout'),
# ******************************************************************************************************************
    path('CustomerContactDisplay/', views.CustomerContactDisplay, name='CustomerContactDisplay'),
    path('CustomerContactDelete/<int:customid>/', views.CustomerContactDelete, name='CustomerContactDelete'),
]