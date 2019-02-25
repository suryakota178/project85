from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from app85 import views

app_name='app85'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(),name='index'),
    path('table/', views.Table.as_view(),name='table'),
    path('create/', views.Create.as_view(),name='create'),
    url (r'^table/(?P<pk>\d+)/$',views.Detail.as_view(),name='detail')

]
