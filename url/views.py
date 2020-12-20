from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.shortcuts import render,redirect
from .forms import Url
from .models import UrlData
import random, string
from django.urls import reverse_lazy
from django.contrib import messages


def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    while True:
        short_id = ''.join(random.choice(char) for _ in range(length))
        try:
            temp = UrlData.objects.get(slug=short_id)
        except:
            return short_id

def urlShort(request):
    if request.method == 'POST':
        form = Url(request.POST)
        if form.is_valid():
            slug = get_short_code()
            url = form.cleaned_data["url"]

            if url.startswith("https://www."):
                initial = "https://www."
                url = url.replace("https://www.", "")
                print(url)

            elif url.startswith("https://"):
                initial = "https://www."
                url = url.replace("https://", "")
                print(url)
            
            elif url.startswith("http://www."):
                initial = "https://www."
                url = url.replace("http://www.", "")
                print(url)

            elif url.startswith("http://"):
                initial = "https://www."
                url = url.replace("http://", "")
                print(url)

            elif url.startswith("www."):
                initial = "www."
                url = url.replace("www.", "")
                print(url)

            len = url.find("/")
            domain = url[:len+1]

            data = UrlData.objects.all()
            url = initial+url
            d= UrlData.objects.filter(url=url)
            if d.exists():
                messages.warning(request, "this url is already shotrened")
                return redirect(".")
            
            

            new_url = UrlData(url=url, slug=slug,domain=domain)
            new_url.save()
            messages.success(request, "url shortened successfully")
            return redirect('.')
    else:
        form = Url()
    data = UrlData.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'index.html', context)


def urlRedirect(request, slugs):
    data = UrlData.objects.get(slug=slugs)
    return redirect(data.url)


class ShortenedUrlListView(ListView):
    model = UrlData
    template_name = "url/shortened_url_list.html"
    
class UrlDetailView(DetailView):
    model = UrlData
    template_name = "url/original_url.html"

class UrlDeleteView(DeleteView):
    model = UrlData
    template_name = "url/delete_confirm.html"
    success_url = reverse_lazy('url:shortened_url_list')
