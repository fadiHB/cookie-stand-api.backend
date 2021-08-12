from django.urls import path
from . import views

urlpatterns = [
    path("", views.CookieStandList.as_view(), name="cookieStand_list"),
    path("<int:pk>/", views.CookieStandDetail.as_view(), name="cookieStand_detail"),
]
