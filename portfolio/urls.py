from django.urls import path
from django.conf.urls import url

from . import views
from .views import (
    HomeView,
)

urlpatterns = [

    url(
        regex=r'^$',
        view=HomeView.as_view(),
        name='home',
    )
]