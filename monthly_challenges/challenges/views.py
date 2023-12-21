from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

m_challenges = {#this is dictionary
    "january" : "eat no meat for the entire month!",
    "february" : "hi it's me!",
    "march" : "how are you!",
    "april" : "fine",
    "june" : "how about you!",
    "july" : "same goes for me",
    "august" : "so what are you working on!",
    "september" : "nothing just learning Django!",
    "october" : "what is it, i never heard of it",
    "november" : "this is a python module or frame work for web development",
    "december" : "okay i get it now!!"
        
}
# Create your views here.


# def index(request):
#     return HttpResponse("This works!")

# def february(request):
#     return HttpResponse("walk for at least 20 mins everyday!")

# def march(request):
#     return HttpResponse("go for gymnastic training")

# def april(request):
#     return HttpResponse("take bath daily")

# def may(request):
#     return HttpResponse("talk to your partner")

# def june(request):
#     return HttpResponse("take some rest")
def monthly_challenge_by_number(request, month):
    months = list(m_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)



def monthly_challenges(request, month):
    try:
        challenge_text = m_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
    # if month == 'january':
    #     challenge_text == "eat no meat for the entire month"
        
    # elif month == 'february':
    #     challenge_text = "walk for at least 20 mins everyday!"
        
    # elif month == 'march':
    #     challenge_text = "go for gymnastic training! "
        
    # elif month == 'april':
    #     challenge_text ="test your strenght"
        
    # elif month == 'may':
    #     challenge_text ="learn django 1 hour daily"
        
    # elif month == 'june':
    #     challenge_text ="have a healthy meal"
        
    # elif month == 'july':
    #     challenge_text ="exercise daily"
        
    # elif month == 'august':
    #     challenge_text ="go for sports"
        
    # elif month == 'september':
    #     challenge_text ="have fun with firends"
        
    # elif month == 'october':
    #     challenge_text ="new sem begins and study hard"
        
    # elif month == 'november':
    #     challenge_text ="get your assignment ready"
        
    # elif month == 'december':
    #     challenge_text ="celeberate christmas"
        
    # else:
    #     return HttpResponseNotFound("This month is not supported")
    


