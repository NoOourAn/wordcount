from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')   #hygeb eltemplate mn elsettings
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddic = {}
    for word in wordlist:
        if word in worddic:
            worddic[word] +=1
        else:
            worddic[word] =1
    return render(request,'count.html' , {'text':fulltext ,'count':len(wordlist),'worddic':worddic})