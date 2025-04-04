"""
URL configuration for django_indexer_web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_indexer_web_app import views
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name="home_page"),
    path('blocks/', views.blocks_page, name="blocks_page"),
    path('blocks/<int:height>', views.search_page, name="search_page"),
    path('transactions/', views.transactions_page, name="transactions_page"),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("__reload__/", include("django_browser_reload.urls"))
]
