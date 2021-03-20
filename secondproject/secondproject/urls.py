"""secondproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from demoApp.views import gm_view , ga_view , ge_view , gn_view
# from demoApp import views as v1

# from timeApp.views import tellMeTime
from timeApp import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('gm/', gm_view),
    path('ga/', ga_view),
    path('ge/', ge_view),
    path('gn/', gn_view),

    # timeApp URL
    path('time/', v2.tellMeTime),

]
