from django.conf.urls import url

from .views import (
    HomeView,
)

app_name = 'main_app'

urlpatterns = [
    url('', HomeView.as_view(), name='home_page'),

]
