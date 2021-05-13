from django.urls import path, include
#from machina import urls as machina_urls
from . import views

urlpatterns = [
    #path('forum/', include(machina_urls)),
    path('', views.CalendarView.as_view(template_name = 'appointments/calendar.html'), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),
]
