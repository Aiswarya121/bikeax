# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from .models import *
from .forms import CategoryForm , ProductForm

from django.db.models import Q 

import re

# Create your views here.
def dashboard(request):
	return render(request, "backend/index.html")

	
def index(request):
	categories=Category.objects.all()
	products=Product.objects.all()[:4]
	productstwo = Product.objects.all()[8:10]
	featured = Product.objects.all()[10:13]
	productsnext = Product.objects.all()[4:8]
	return render(request,'frontend/index.html', {'products':products, 'productstwo':productstwo,'featured':featured,'productsnext':productsnext,'categories':categories})


def single(request):
	return render(request,'frontend/single.html')

	
def checkout(request):
	return render(request,'frontend/checkout.html')

	

def addcategory(request):
	form=CategoryForm()
	if request.method=="POST":
		form=CategoryForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.save()	
	return render(request,'backend/addcategory.html' ,{'form':form})


def addproduct(request):
	form=ProductForm()
	if request.method=="POST":
		form=ProductForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.save()				
	return render(request,'backend/addproduct.html',{'form':form})


#search box 
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):
    
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        print query_string
        entry_query = get_query(query_string, [ 'Name',])
        print entry_query

        found_entries = Product.objects.filter(entry_query)
        
    return render_to_response('frontend/search.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          )
