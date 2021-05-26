# I HAVE CREATED THIS FILE - VARNIKA 
from django.http import HttpResponse

from django.shortcuts import render
####################################################################################################################################
#CODE OF VIDEO 6


#def index(request):
   # return HttpResponse('''<h1>VARNIKA </h1> <a href="https://www.facebook.com/"> FACEBOOK </a>
    #<a href="https://www.instagram.com/> INSTAGRAM </a>"''')#ye line ni chal ri alag se hi chlana padega nya function bana k ya aese bhi ho kisi trah se


#def about(request):
  #  return HttpResponse("hello varuuu")  
##################################################################################################################################
#CODE OF VIDEO 6
# def index(request):
  #  return HttpResponse("<h1>Home</h1>")

def ex1(request):
    s = '''<h2>Navigation Bar<br></h2>
            <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 
            <a href="https://www.facebook.com/">Facebook</a><br>
            <a href="https://www.flipkart.com/">Flipkart</a><br>
            <a href="https://www.hindustantimes.com">News</a><br>
            <a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)
   

def analyze(request):
   #get the text
    djtext = request.GET.get('text','default')
    print(djtext)
    #checkbox values
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    charcounter= request.GET.get('charcounter','off')
    #check which checkbox is on
    if removepunc == "on":
   
      # analyzed=djtext
        punctuations ='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                params={'purpose':'removed punctuations','analyzed_text': analyzed}
        # ANalyze text 
        return render(request,'analyze.html',params)

    elif fullcaps=="on":
      analyzed=""
      for char in djtext:
          analyzed = analyzed + char.upper()
          params={'purpose':'changed to uppercase','analyzed_text': analyzed}
      return render(request,'analyze.html',params)

    elif(newlineremover=="on"):
      analyzed=""
      for char in djtext:
        if char!="\n":
          analyzed = analyzed + char
          params={'purpose':'remove new line','analyzed_text': analyzed}
      return render(request,'analyze.html',params)
    

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):
                analyzed = analyzed + char

                params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        return render(request, 'analyze.html', params)

    elif(charcounter=="on"):
        analyzed = 0
        
        for char in djtext:
            analyzed=analyzed+1
            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        return render(request, 'analyze.html', params)

    else:
      return HttpResponse("Error")


def index(request):
  
    return render(request,'index.html') 







