from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


def index(req):
    # index
    # return redirect("127.0.0.1:8000/show")
    return HttpResponseRedirect('/show/')
