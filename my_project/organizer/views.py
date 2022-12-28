# {{seccond:2}}

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.views.decorators.http import require_safe

from .models import Tag

# Create your views here.

@require_safe
def tag_list(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('tag/list.html')
    # context = statement 
    # "tag_list" used in the html file 
    context = {"tag_list": tag_list}
    html_content = template.render(context)
    return HttpResponse(html_content)


@require_safe
def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    template = loader.get_template("tag/detail.html")
    context = {"tag": tag}
    html_content = template.render(context)
    return HttpResponse(html_content)