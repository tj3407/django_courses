# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(req):
    context = {
        "desc": Description.objects.all()  
    }
    return render(req, 'course/index.html', context)

def add(req):
    errors = Description.objects.basic_validator(req.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(req, error, extra_tags=tag)
        return redirect('/')
    else:
        id = Course.objects.create(name=req.POST['course_name'])
        Description.objects.create(desc=req.POST['course_desc'], course=id)
        return redirect("/")

def delete(req, id):
    context = {
        "data": Description.objects.get(id=id)
    }
    return render(req, 'course/remove.html', context)

def destroy(req):
    Course.objects.get(id=req.POST['id']).delete()
    return redirect('/')


