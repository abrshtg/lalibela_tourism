from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("attractions/", views.attraction_list, name="attraction_list"),
    path(
        "attractions/<int:attraction_id>/",
        views.attraction_detail,
        name="attraction_detail",
    ),
    path("attractions/add/", views.attraction_create, name="attraction_create"),
    path(
        "attractions/<int:attraction_id>/update/",
        views.attraction_update,
        name="attraction_update",
    ),
    path(
        "attractions/<int:attraction_id>/delete/",
        views.attraction_delete,
        name="attraction_delete",
    ),
    path("tourists/", views.tourist_list, name="tourist_list"),
    path("tourists/<int:tourist_id>/", views.tourist_detail, name="tourist_detail"),
    path("tourists/add/", views.tourist_create, name="tourist_create"),
    path(
        "tourists/<int:tourist_id>/update/", views.tourist_update, name="tourist_update"
    ),
    path(
        "tourists/<int:tourist_id>/delete/", views.tourist_delete, name="tourist_delete"
    ),
    path("tour-packages/", views.tour_package_list, name="tour_package_list"),
    path(
        "tour-packages/<int:tour_package_id>/",
        views.tour_package_detail,
        name="tour_package_detail",
    ),
    path("tour-packages/add/", views.tour_package_create, name="tour_package_create"),
    path(
        "tour-packages/<int:tour_package_id>/update/",
        views.tour_package_update,
        name="tour_package_update",
    ),
    path(
        "tour-packages/<int:tour_package_id>/delete/",
        views.tour_package_delete,
        name="tour_package_delete",
    ),
    path("bookings/", views.booking_list, name="booking_list"),
    path("bookings/<int:booking_id>/", views.booking_detail, name="booking_detail"),
    path("bookings/add/", views.booking_create, name="booking_create"),
    path(
        "bookings/<int:booking_id>/update/", views.booking_update, name="booking_update"
    ),
    path(
        "bookings/<int:booking_id>/delete/", views.booking_delete, name="booking_delete"
    ),
    path("about-us/", views.about, name="about"),
]
