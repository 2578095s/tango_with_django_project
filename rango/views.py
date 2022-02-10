from django.shortcuts import render

from django.shortcuts import HttpResponse

from rango.models import Category

from rango.models import Page


def index(request):
  category_list = Category.objects.order_by('-likes')[:5]
  
  context_dict = {}
  context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
  context_dict['categories'] = category_list
  return render(request, 'rango/index.html', context=context_dict)



def about(request):
  context_dict = {'name': 'Rhythm Sodhi'}
  return render(request, 'rango/about.html', context = context_dict)


def show_category(request, category_name_slug):
  try:
    context_dict['pages'] = pages
  except Category.DoesNotExist:
    context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)

