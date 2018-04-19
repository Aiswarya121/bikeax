# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def dashboard(request):
	return render(request, "backend/index.html")

	
def index(request):
	return render(request,'frontend/index.html')


def single(request):
	return render(request,'frontend/single.html')

	
def checkout(request):
	return render(request,'frontend/checkout.html')
