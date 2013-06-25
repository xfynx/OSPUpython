__author__ = 'xfynx'

from django.http import HttpResponse, Http404
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

def hello(request):
    now = datetime.datetime.now()
    return render_to_response('homepage.html', {'current_date': now})

def hours(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('time.htm',{'next_time': dt, 'hour':offset})

def timer(request):
    return render_to_response('timer.html', )

def square_print(request):
    return render_to_response('square.html', )

def square(request):
    if 'a' in request.GET:
        a = request.GET['a']
        a = float(a)*float(a)
        message = 'your square is %r' % a
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def triangle_print(request):
    return render_to_response('triangle.html', )

def triangle(request):
    if 'a' in request.GET and 'b' in request.GET and 'c' in request.GET:
        a = request.GET['a']
        b = request.GET['b']
        c = request.GET['c']
        p = float(a)+float(b)+float(c)
        message = 'your perimeter is %r' % p
    else:
        message = 'You submitted an empty forms.'
    return HttpResponse(message)

def circle_print(request):
    return render_to_response('circle.html', )

def circle(request):
    if 'radius' in request.GET:
        rad = request.GET['radius']
        rad = 2*3.1415*float(rad)
        message = 'your circle`s area is %r' % rad
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def paral_print(request):
    return render_to_response('paral.html', )

def paral(request):
    if 'a' in request.GET and 'b' in request.GET and 'c' in request.GET:
        a = request.GET['a']
        b = request.GET['b']
        c = request.GET['c']
        v = float(a)*float(b)*float(c)
        message = 'your volume: %r' % v
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def demo(request):
    return render_to_response('demo.html', )