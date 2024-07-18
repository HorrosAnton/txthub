import random
import string
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def nest(request, urls_site):
    try:
        article = Articles.objects.get(urls_site=urls_site)
        text = ""
        # for i in Articles.objects.all():
        #     if str(i) == urls_site:
        #         print(f"I -> {i.title}")
        #         text = i.title
        # print(f"url_site = {urls_site}")
        if str(urls_site) == str(article):
            return render(request, 'main/details.html', {"art": article})
    except:
        return render(request, "main/error.html")

class NewDetail(DetailView):
    model = Articles
    template_name = 'main/details.html'
    context_object_name = 'article'

def index(request):
    list_string_lowercase = list(string.ascii_lowercase)
    list_string_uppercase = list(string.ascii_uppercase)
    list_string = list_string_uppercase + list_string_lowercase
    urls_s = []
    for i in range(15):
        a = random.choice(list_string)
        urls_s.append(a)
        print(urls_s)
    strok = ''
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form = Articles(urls_site=f'{strok.join(urls_s)}', title=form.cleaned_data['title'])
            form.save()
            return redirect(f"/{strok.join(urls_s)}", strok.join(urls_s))
        else:
            error = "404"

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, "main/index.html", data)



def about(request):
    return render(request, "main/about.html")