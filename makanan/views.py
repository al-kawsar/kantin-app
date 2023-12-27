from django.shortcuts import render
from django.http import HttpResponse
from .models import Makanan
from django.shortcuts import get_object_or_404
from .models import Kantin
from .models import Makanan

# Create your views here

def Home(request):
    kantins = Kantin.objects.all()
    searchMakanan = request.GET.get('nama')
    kantin_id = request.GET.get('kantin_id')
    if searchMakanan:
        makanans = Makanan.objects.filter(nama__icontains=searchMakanan)
    elif kantin_id:
        makanans = Makanan.objects.filter(kantin_id = 'kantin_id')
    else:
        makanans = Makanan.objects.all()
    return render(request, 'home.html', {'searchMakanan':searchMakanan,'makanans' : makanans,'kantins':kantins})
def detail(request,makanan_id):
    makanan = get_object_or_404(Makanan,pk=makanan_id)
    return render(request,'detail.html',{'makanan' : makanan})



