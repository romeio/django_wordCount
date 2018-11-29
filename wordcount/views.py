from django.http import  HttpResponse
from django.shortcuts import render



def home(request):
	return render(request,'home.html')

def about(request):
	return render(request,'about.html')
def eggs(request):
	return HttpResponse('Collect The Eggs Page')

def fake(request):
	return render(request,'fake.html')

def count(request):
  fullText=request.GET['fulltext']
  wordlist=fullText.split()
  wordcountdictionary={''}
  for word in wordlist:
	  if word in wordcountdictionary:
	       wordcountdictionary +=1
  else:
	      wordcountdictionary =1
	     

  return render(request,'count.html',{'fulltext':fullText,'count':len(wordlist),'wordcountdictionary':str(wordcountdictionary)})




















