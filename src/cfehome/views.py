import pathlib
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path= request.path)

    my_title= "My page"
    html_ = "home.html"

    context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": (page_qs.count()*100)/qs.count(),
        "total_visit_count": qs.count()
    }
    PageVisit.objects.create(path=request.path)
    return render(request, html_, context)




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