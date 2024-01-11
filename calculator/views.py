from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add(request, num_1, num_2):
    result = num_1 + num_2
    return HttpResponse(f"<h1> {num_1} + {num_2} = {result}</h1>")

def sub(request, num_1, num_2):
    result = num_1 - num_2
    return HttpResponse(f"<h1> {num_1} - {num_2} = {result}</h1>")

def mult(request, num_1, num_2):
    result = num_1 * num_2
    return HttpResponse(f"<h1> {num_1} * {num_2} = {result}</h1>")

def div(request, num_1, num_2):
    result = num_1 / num_2
    return HttpResponse(f"<h1> {num_1} / {num_2} = {result}</h1>")



