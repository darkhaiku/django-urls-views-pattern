# {{seccond:2}}

from django.shortcuts import get_object_or_404

# Generic class base views!
# it looks like magic
from django.views.generic import DetailView, ListView

from .models import Tag

# Create your views here.


class TagList(ListView):

    queryset = Tag.objects.all()
    template_name = "tag/list.html"


class TagDetail(DetailView):

    queryset = Tag.objects.all()
    template_name = "tag/detail.html"
