from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from lxml import html
import requests

# Create your views here.
def index(request):
	page = requests.get('https://xkcd.com/780/')
	tree = html.fromstring(page.content)
	comic = tree.xpath('//div[@id="comic"]/node()')
	comicImg = comic[1].xpath('//img/@src')
	context = {'comic': 'https:' + str(comicImg[1])}
	print "tree: " + str(tree)
	print "comic" + str(comic[1])
	print "comic length" + str(len(comic))
	print context
	print str(comicImg[1])
	return render(request, 'hello/index.html', context) 
