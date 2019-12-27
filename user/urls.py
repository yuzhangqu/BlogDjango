# -*- coding: utf-8 -*-

from django.urls import path
from .views import reg

urlpatterns = [
    path('reg', reg),
]
