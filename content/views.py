# coding=utf-8
from django.shortcuts import render

from content.models import banner
from para.models import Para


def commonfunc(flag):
    ctx = {}
    if flag == 'homeactive':
        ctx['homeactive'] = 'active'
        ctx['serviceactive'] = ''
        ctx['solutionactive'] = ''
        ctx['aboutactive'] = ''
        ctx['contactactive'] = ''
    if flag == 'serviceactive':
        ctx['homeactive'] = ''
        ctx['serviceactive'] = 'active'
        ctx['solutionactive'] = ''
        ctx['aboutactive'] = ''
        ctx['contactactive'] = ''
    if flag == 'solutionactive':
        ctx['homeactive'] = ''
        ctx['serviceactive'] = ''
        ctx['solutionactive'] = 'active'
        ctx['aboutactive'] = ''
        ctx['contactactive'] = ''
    if flag == 'aboutactive':
        ctx['homeactive'] = ''
        ctx['serviceactive'] = ''
        ctx['solutionactive'] = ''
        ctx['aboutactive'] = 'active'
        ctx['contactactive'] = ''
    if flag == 'contactactive':
        ctx['homeactive'] = ''
        ctx['serviceactive'] = ''
        ctx['solutionactive'] = ''
        ctx['aboutactive'] = ''
        ctx['contactactive'] = 'active'
    return ctx


def loadbanner(ctx):
    banners = banner.objects.filter(info='banner1')
    if banners:
        bn = banners[0]
    else:
        bn = None
    ctx['banner1'] = {'img': bn.banner.url, 'para1': bn.para1, 'para2': bn.para2, 'para3': bn.para3, 'para4': bn.para4}
    banners = banner.objects.filter(info='banner2')
    if banners:
        bn = banners[0]
    else:
        bn = None
    ctx['banner2'] = {'img': bn.banner.url, 'para1': bn.para1, 'para2': bn.para2, 'para3': bn.para3, 'para4': bn.para4}
    banners = banner.objects.filter(info='banner3')
    if banners:
        bn = banners[0]
    else:
        bn = None
    ctx['banner3'] = {'img': bn.banner.url, 'para1': bn.para1, 'para2': bn.para2, 'para3': bn.para3, 'para4': bn.para4}
    return ctx


def recentword(ctx):
    projs = []
    rws = Para.objects.filter(key__contains='KEY_RECENTWORK_').order_by('-id')
    for r in rws:
        projs.append(r)
    ctx['recentwork'] = {'projs': projs}
    return ctx


def mainpage(request):
    ctx = commonfunc('homeactive')
    ctx = loadbanner(ctx)
    ctx = recentword(ctx)
    return render(request, 'index.html', ctx)


def tcs(request):
    ctx = commonfunc('serviceactive')
    return render(request, 'tcs.html', ctx)


def ito(request):
    ctx = commonfunc('serviceactive')
    return render(request, 'ito.html', ctx)


def bpo(request):
    ctx = commonfunc('serviceactive')
    return render(request, 'bpo.html', ctx)


def pgs(request):
    ctx = commonfunc('serviceactive')
    return render(request, 'pgs.html', ctx)


def mobsolu(request):
    ctx = commonfunc('solutionactive')
    return render(request, 'mobile_solutions.html', ctx)


def digital(request):
    ctx = commonfunc('solutionactive')
    return render(request, 'digital.html', ctx)


def about(request):
    ctx = commonfunc('aboutactive')
    return render(request, 'about.html', ctx)


def contact(request):
    ctx = commonfunc('contactactive')
    return render(request, 'contact.html', ctx)
