from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from lxml import html
import requests
from random import randint

# Create your views here.
def index(request):
	pageStr = 'https://xkcd.com/' + str(randint(1,1818)) + '/'
	page = requests.get(pageStr)
	tree = html.fromstring(page.content)
	comic = tree.xpath('//div[@id="comic"]/node()')
	comicImg = comic[1].xpath('//img/@src')
	context = {'comic': 'https:' + str(comicImg[1])}
	return render(request, 'hello/index.html', context) 
