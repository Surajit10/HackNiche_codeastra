from django.contrib import admin
from django.urls import path,include
from users import views

urlpatterns = [
     path('register/', views.users_register, name='register'),
     path('login/', views.users_login, name='login'),
     path('register_hackathon/', views.register_hackathon, name='reg_hack'),
     path('hackathons/', views.see_hackathon, name='view_hackathons'),
     path('contact/', views.contact, name='contact'),
     path('admin_index/', views.admin_index, name='admin_index'),
     path('hack-details/<int:pk>', views.hack_details, name='hack-details'),
     path('hackathons/show/<int:pk>', views.show_hackathon, name='show_hackathons'),
     path('hackathons/show/show_hackathon/<int:pk>', views.part_register, name='show_hackathon'),
     path('hackathons/show/parti_register/<int:pk>', views.part_register, name='part_register'),
     # path('hackathons/show/register/<int:pk>', views.part_register, name='part_register'),
]
