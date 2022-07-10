from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'index_list'),
    #path('group/', views.group_posts, name = 'gr_list')
    path('group/<slug:post_id>/', views.group_posts, name = 'gr_list')
]
# Create your views here.