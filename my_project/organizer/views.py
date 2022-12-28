# {{seccond:2}}

from django.shortcuts import get_object_or_404,render
from django.views.decorators.http import require_safe

from .models import Tag

# Create your views here.

@require_safe
def tag_list(request):
    tag_list = Tag.objects.all()
    # context = statement 
    # "tag_list" used in the html file 
    context = {"tag_list": tag_list}
    return render(request, "tag/list.html", context)


@require_safe
def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    context = {"tag": tag}
    return render(request, "tag/detial.html", context)