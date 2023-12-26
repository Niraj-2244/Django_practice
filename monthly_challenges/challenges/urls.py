from django.urls import path

from . import views

urlpatterns =[
    
    # path("january", views.index),
    # path("february", views.february),
    # path("march", views.march),
    # path("april", views.april),
    # path("may", views.may),
    # path("june", views.june),
    path("",views.index),#/challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenges, name="month-challenge"),
]
