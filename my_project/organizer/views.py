# {{seccond:2}}

from django.shortcuts import get_object_or_404,render

# django class based views.
from django.views import View

from .models import Tag

# Create your views here.


class TagList(View):
    def get(self, request):
        tag_list = Tag.objects.all()
        # context = statement 
        # "tag_list" used in the html file 
        context = {"tag_list": tag_list}
        return render(request, "tag/list.html", context)


class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        context = {"tag": tag}
        return render(request, "tag/detial.html", context)