from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('add-student/',views.add_student,name='add-student'),
    path('add-to-student/',views.add_to_student,name='add-to-student'),
    path('view-student/',views.view_student,name='view-student'),
]
