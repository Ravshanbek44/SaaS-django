import pathlib
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        print(request.user.first_name)
    return about_view(request, *args, **kwargs)


def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path= request.path)
    try:
        percent= (page_qs.count()*100)/qs.count()
    except:
        percent=0    


    my_title= "My page"
    html_templates = "home.html"
    context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count()
    }
    PageVisit.objects.create(path=request.path)
    return render(request, html_templates, context)








def my_old_home_page_view(request, *args, **kwargs):
    html_ ="""
<!DOCTYPE html>
<html>

<body>
    <h1>is this anythinwwxdeewg</h1>
</body>
</html>
"""
    #html_file_path = this_dir / "home.html"
    #html_ = html_file_path.read_text()
    return HttpResponse(html_)