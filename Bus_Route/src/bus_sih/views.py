import pathlib
from django.shortcuts import render
from django.http import HttpResponse # type: ignore
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, **args):
    queryset = PageVisit.objects.all()
    queryset_page = PageVisit.objects.filter(path=request.path)
    my_title = "DTC"
    my_context = {
        "page_title": my_title,
        "page_visit_count": queryset_page.count(),
        "total_visit_count": queryset.count(),
    }
    html_template = "index.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)

def about_page_view(request, **args):
        title_about = "About"
        about_context = {
            "page_title": title_about,
        }
        html_template=""
