
from .models import Tourist, TourPackage, Attraction, Booking


from django.shortcuts import render, get_object_or_404, redirect
from .forms import AttractionForm

def attraction_list(request):
    attractions = Attraction.objects.all()
    return render(request, 'tourism/attraction/attraction_list.html', {'attractions': attractions})

def attraction_detail(request, attraction_id):
    attraction = get_object_or_404(Attraction, id=attraction_id)
    return render(request, 'tourism/attraction/attraction_detail.html', {'attraction': attraction})

def attraction_create(request):
    if request.method == 'POST':
        form = AttractionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attraction_list')
    else:
        form = AttractionForm()
    return render(request, 'tourism/attraction/attraction_form.html', {'form': form})

def attraction_update(request, attraction_id):
    attraction = get_object_or_404(Attraction, id=attraction_id)
    if request.method == 'POST':
        form = AttractionForm(request.POST, instance=attraction)
        if form.is_valid():
            form.save()
            return redirect('attraction_list')
    else:
        form = AttractionForm(instance=attraction)
    return render(request, 'tourism/attraction/attraction_form.html', {'form': form})

def attraction_delete(request, attraction_id):
    attraction = get_object_or_404(Attraction, id=attraction_id)
    if request.method == 'POST':
        attraction.delete()
        return redirect('attraction_list')
    return render(request, 'tourism/attraction/attraction_confirm_delete.html', {'attraction': attraction})
