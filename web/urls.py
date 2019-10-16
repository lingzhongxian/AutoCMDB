"""AutoCMDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, re_path
from web.views import account
from web.views import home
from web.views import asset
from web.views import user
from web.views import test

urlpatterns = [
    # url(r'test/',test.hello),
    url(r'test/user/',test.User.user),
    # url(r'^login.html$', account.LoginView.as_view()),
    # url(r'^logout.html$', account.LogoutView.as_view()),
    # url(r'^index.html$', home.IndexView.as_view()),
    # url(r'^cmdb.html$', home.CmdbView.as_view()),
    # url(r'^asset.html$', asset.AssetListView.as_view()),
    # url(r'^assets.html$', asset.AssetJsonView.as_view()),
    # url(r'^asset-(?P<device_type_id>\d+)-(?P<asset_nid>\d+).html$', asset.AssetDetailView.as_view()),
    # url(r'^add-asset.html$', asset.AddAssetView.as_view()),
    # url(r'^users.html$', user.UserListView.as_view()),
    # url(r'^user.html$', user.UserJsonView.as_view()),
    # url(r'^chart-(?P<chart_type>\w+).html$', home.ChartView.as_view()),
    url(r'login.html', account.LoginView.as_view()),
    url(r'logout.html', account.LogoutView.as_view()),
    url(r'index.html', home.IndexView.as_view()),
    url(r'cmdb.html', home.CmdbView.as_view()),
    url(r'asset.html', asset.AssetListView.as_view()),
    url(r'assets.html', asset.AssetJsonView.as_view()),
    url(r'asset-(?P<device_type_id>\d+)-(?P<asset_nid>\d+).html', asset.AssetDetailView.as_view()),
    url(r'add-asset.html', asset.AddAssetView.as_view()),
    url(r'users.html', user.UserListView.as_view()),
    url(r'user.html', user.UserJsonView.as_view()),
    re_path(r'chart-(?P<chart_type>\w+).html', home.ChartView.as_view()),
]
app_name = 'web'
