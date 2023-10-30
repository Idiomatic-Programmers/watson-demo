from django.contrib import admin
from django.urls import include, path

from posts.views import SearchView, search_page

urlpatterns = [
    path('search-api/', SearchView.as_view()),
    path("search-page/", search_page),
    path("search/", include("watson.urls", namespace="watson")),
    path('admin/', admin.site.urls),
]
