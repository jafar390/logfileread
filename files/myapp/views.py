from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
import os


@requires_csrf_token
@xframe_options_exempt
def index(request):
    template='index.html'
    return render(request,template)

@csrf_exempt
def firstpage(request):
	if request.method == 'POST':
		file='text/'
		file+='Files.log.2018080601.log'
		aDict = {}
		fo = open(file, "r")
		print(fo.tell())
		for i in range(1,6):
			str1 = fo.readline()
			print(fo.tell())
			aDict[i]=str1
		index=fo.tell()
		fo.close()
		return JsonResponse({'result' : aDict,'index1' : index})
	return HttpResponse("wrong text")

@csrf_exempt
def nextpage(request):
	if request.method == 'POST':
		len1=request.POST['position']
		file='text/'
		file+='Files.log.2018080601.log'
		print(len1)
		aDict = {}
		fo = open(file, "r")
		position = fo.seek(int(len1), 0)
		print(fo.tell())
		for i in range(1,6):
			str1 = fo.readline()
			print(fo.tell())
			aDict[i]=str1
		index=fo.tell()
		fo.close()
		return JsonResponse({'result' : aDict,'index1' : index})
	return HttpResponse("wrong text")

