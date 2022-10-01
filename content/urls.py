from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view),
    path('postadd/', views.post_add),
    path('postedit/', views.post_edit)
]