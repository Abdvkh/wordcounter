from django.http import HttpResponse
from django.shortcuts import render
import operator

def about(request):
    about = 'I am very keen on programming that\'s awesome.'
    
    return render(request, 'about.html', {'about': about})

def homepage(request):
    context = {
        'no': 'no'
    }
    return render(request, 'home.html', context)

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    # wordlist.sort()
    worddictionary = {}
    
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
            
    sortedwords = sorted(worddictionary.items(), 
           key=operator.itemgetter(1), 
           reverse=True)
            
    context = { 
               'words_number': len(wordlist),
               'fulltext': fulltext,
               'sortedwords': sortedwords,
               }
    return render(request, 'count.html', context)