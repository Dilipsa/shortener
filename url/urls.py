from django.urls import path
from . import views
app_name = "url"
urlpatterns = [
    path("short/", views.urlShort, name="short"),
    path("u/<str:slugs>/", views.urlRedirect, name="redirect"),
    path("", views.ShortenedUrlListView.as_view(), name="shortened_url_list"),
    path("original-url/<slug>/", views.UrlDetailView.as_view(), name="original_url"),
    path("delete-url/<slug>/", views.UrlDeleteView.as_view(), name="delete_url"),
]