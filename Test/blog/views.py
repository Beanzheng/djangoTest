from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.views import defaults
# Create your views here.

def do_normal(request):
    print("in the noraml")
    return HttpResponse("This is NormalMap")

def withparam(request,year,month):
    print("in the data")
    return HttpResponse("today is {0} year {1} month".format(year,month))

def findNumber(request,pagenumber):
    return HttpResponse("Page is number {0}".format(pagenumber))

def extraparam(request,name):
    return HttpResponse("My name is {0}".format(name))

def revParse(request):
    return HttpResponse("Request URl is {0}".format(reverse("askname")))

def v10_1(request):
    return HttpResponseRedirect("/v11")

def v10_2(request):
    return HttpResponseRedirect(reverse("hello"))

def v11(request):
    return HttpResponse("你终于访问到我了!")

def getReqContent(request):
    rsp = ""
    for k,v in request.GET.items():
        rsp += k+"----"+v
        rsp += ","

    return HttpResponse("This is Request: {0}".format(rsp))

def blog_get(request):
    return render_to_response("for_post.html")

def blog_post(request):
    rsq =""
    for k,v in request.POST.items():
        rsq +=k +"----"+v
        rsq += ","

    return HttpResponse("Message:{0}".format(rsq))

def render_test(request):
    rsp = render(request,"renderTest.html")
    return rsp

def render2_test(request):
    c=dict()
    c["name"]="郑高翔"
    rsp = render(request,"renderTest2.html",context=c)
    return rsp

def render3_test(request):
    t = loader.get_template("renderTest2.html")

    rsp = t.render({"name":"zgx"})

    return HttpResponse(rsp)

def get404(request):

    return defaults.page_not_found(request,template_name="renderTest.html")