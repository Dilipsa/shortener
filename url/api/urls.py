from django.urls import path
from . import views

urlpatterns = [
    path("", views.urlShortCreateView.as_view(), name="home"),
    path("all-urls/", views.AllUrl.as_view(), name="all_urls"),
    path("shortened-url-list/<slug>/", views.ShortenedUrlListView.as_view(), name="shortened_url_list"),
    path("delete-url/<pk>/", views.UrlDeleteView.as_view(), name="delete_url"),
    path("<slug>/", views.RedirectView.as_view(), name="redirect"),
    path("original-url/<pk>/", views.UrlDetailView.as_view(), name="original_url"),
]