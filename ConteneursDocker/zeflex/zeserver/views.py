from django.shortcuts import render


def index(request):
    ctx = {}
    template = "zeserver/index.html"
    return(render(request=request,template_name=template,context=ctx))