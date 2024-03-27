from django.shortcuts import render, get_object_or_404, redirect


from .forms import AttractionForm, BookingForm, TourPackageForm, TouristForm
from .models import Tourist, TourPackage, Attraction, Booking


def home(request):
    return render(request, "tourism/home.html")


def attraction_list(request):
    attractions = Attraction.objects.all()
    return render(
        request, "tourism/attraction/attraction_list.html", {"attractions": attractions}
    )


def attraction_detail(request, attraction_id):
    attraction = get_object_or_404(Attraction, id=attraction_id)
    return render(
        request, "tourism/attraction/attraction_detail.html", {"attraction": attraction}
    )


def attraction_create(request):
    if request.method == "POST":
        form = AttractionForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("attraction_list")
    else:
        form = AttractionForm()
    return render(request, "tourism/attraction/attraction_form.html", {"form": form})


def attraction_update(request, attraction_id):
    attraction = get_object_or_404(Attraction, id=attraction_id)
    if request.method == "POST":
        form = AttractionForm(request.POST, instance=attraction)
        if form.is_valid():
            form.save()
            return redirect("attraction_list")
    else:
        form = AttractionForm(instance=attraction)
    return render(request, "tourism/attraction/attraction_form.html", {"form": form})


def attraction_delete(request, attraction_id):
    attraction = get_object_or_404(Attraction, id=attraction_id)
    if request.method == "POST":
        attraction.delete()
        return redirect("attraction_list")
    return render(
        request,
        "tourism/attraction/attraction_confirm_delete.html",
        {"attraction": attraction},
    )


def tourist_list(request):
    tourists = Tourist.objects.all()
    return render(request, "tourism/tourist/tourist_list.html", {"tourists": tourists})


def tourist_detail(request, tourist_id):
    tourist = get_object_or_404(Tourist, id=tourist_id)
    return render(request, "tourism/tourist/tourist_detail.html", {"tourist": tourist})


def tourist_create(request):
    if request.method == "POST":
        form = TouristForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tourist_list")
    else:
        form = TouristForm()
    return render(request, "tourism/tourist/tourist_form.html", {"form": form})


def tourist_update(request, tourist_id):
    tourist = get_object_or_404(Tourist, id=tourist_id)
    if request.method == "POST":
        form = TouristForm(request.POST, instance=tourist)
        if form.is_valid():
            form.save()
            return redirect("tourist_list")
    else:
        form = TouristForm(instance=tourist)
    return render(request, "tourism/tourist/tourist_form.html", {"form": form})


def tourist_delete(request, tourist_id):
    tourist = get_object_or_404(Tourist, id=tourist_id)
    if request.method == "POST":
        tourist.delete()
        return redirect("tourist_list")
    return render(
        request, "tourism/tourist/tourist_confirm_delete.html", {"tourist": tourist}
    )


def tour_package_list(request):
    tour_packages = TourPackage.objects.all()
    return render(
        request,
        "tourism/tour_package/tour_package_list.html",
        {"tour_packages": tour_packages},
    )


def tour_package_detail(request, tour_package_id):
    tour_package = get_object_or_404(TourPackage, id=tour_package_id)
    return render(
        request,
        "tourism/tour_package/tour_package_detail.html",
        {"tour_package": tour_package},
    )


def tour_package_create(request):
    if request.method == "POST":
        form = TourPackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tour_package_list")
    else:
        form = TourPackageForm()
    return render(
        request, "tourism/tour_package/tour_package_form.html", {"form": form}
    )


def tour_package_update(request, tour_package_id):
    tour_package = get_object_or_404(TourPackage, id=tour_package_id)
    if request.method == "POST":
        form = TourPackageForm(request.POST, instance=tour_package)
        if form.is_valid():
            form.save()
            return redirect("tour_package_list")
    else:
        form = TourPackageForm(instance=tour_package)
    return render(
        request, "tourism/tour_package/tour_package_form.html", {"form": form}
    )


def tour_package_delete(request, tour_package_id):
    tour_package = get_object_or_404(TourPackage, id=tour_package_id)
    if request.method == "POST":
        tour_package.delete()
        return redirect("tour_package_list")
    return render(
        request,
        "tourism/tour_package/tour_package_confirm_delete.html",
        {"tour_package": tour_package},
    )


def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, "tourism/booking/booking_list.html", {"bookings": bookings})


def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, "tourism/booking/booking_detail.html", {"booking": booking})


def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking_list")
    else:
        form = BookingForm()
        tourist = Tourist.objects.all()
        tour_package = TourPackage.objects.all()
        context = {"form": form, "tourist": tourist, "tour_package": tour_package}
        return render(request, "tourism/booking/booking_form.html", {"context": context})
    return render(request, "tourism/booking/booking_form.html", {"form": form})


def booking_update(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect("booking_list")
    else:
        form = BookingForm(instance=booking)
    return render(request, "tourism/booking/booking_form.html", {"form": form})


def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        booking.delete()
        return redirect("booking_list")
    return render(
        request, "tourism/booking/booking_confirm_delete.html", {"booking": booking}
    )


def about(request):
    return render(request, "tourism/about.html")