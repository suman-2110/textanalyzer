from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'mypack.html')

def signin(request):
    print(request.GET.get('text','default'))
    print(request.GET.get('text', 'default'))
    return HttpResponse("<h1> welcome</h1> <a href = http://127.0.0.1:8000/explore>lets do </a>")
    #<a href = http://127.0.0.1:8000/explore>lets do </a>

def explore(request):
   return render(request,'textutils.html')

def removepunc(request):
    djtext=(request.POST.get('text','default'))
    removepunc=(request.POST.get('removepunc','off'))
    uppercase=(request.POST.get('uppercase','off'))
    newline = (request.POST.get('newline', 'off'))
    lowercase = (request.POST.get('lowercase', 'off'))

    #print(removepunc)
    #print(djtext)
    if(removepunc=='on'):
        Punctuations = '''/[-[\]{}() * +?.,  , \ ;\ ^ $ | '!/ # \,/g, :", \ \ ,$ ,& '''
        analyzed = ''
        for char in djtext:
            if char not in Punctuations:
                analyzed = analyzed + char
                # analyzed = djtext
        print(analyzed)
        params = {'purpose': 'remove punctations', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed
        #return HttpResponse("<h1>punctutaion removed</h1> <a href=http://127.0.0.1:8000/explore>Do it again</a>")
    if(uppercase=='on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'capitalize letter', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed
    if(newline=='on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
            else:
                print("no")
                # analyzed = djtext
        print('pre',analyzed)
        params = {'purpose': 'remove newline character', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed
    if(lowercase=='on'):
        analyzed = ''
        for char in djtext:
                analyzed = analyzed + char.lower()
                # analyzed = djtext
        #print(analyzed)
        params = {'purpose': 'capital letter removed', 'analyzed_text': analyzed}
        djtext=analyzed

    '''else:
        return HttpResponse("error")'''


    if removepunc != 'on' and uppercase !='on' and lowercase !='on' and newline !='on':

        return HttpResponse("invalid input")

    return render(request, 'analyze.html', params)

def navibar(request):
    return render(request,'navi.html')










