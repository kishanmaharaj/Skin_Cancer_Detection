from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

#from machina import urls as machina_urls

urlpatterns = [
    path('', views.home, name='home'),
    path('appointments/',views.appointments, name='appointments'),
    #path('forum/',views.forum, name='forum'),
    #path('forum/', include(machina_urls), name='forum'),
    path('predict/', views.predict, name = 'predict'),
]
