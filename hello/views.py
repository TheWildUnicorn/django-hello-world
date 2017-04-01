from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from lxml import html
import requests

# Create your views here.
def index(request):
	page = requests.get('https://xkcd.com/780/')
	tree = html.fromstring(page.content)
	comic = tree.xpath('//div[@id="comic"]/text()')
	context = {'comic': comic}
	return render(request, 'hello/index.html', context)

