from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


monthly_challenges = {
    "january": "Eat no carbs for the entire month!",
    "february": "Walk for at least 20 minutes everyday!",
    "march": "Learn Django for at least an hour everyday!",
    "april": "Read at least one book per week!",
    "may": "Go hiking every weekend!",
    "june": "Drink 2 litres of water everyday!",
    "july": "Change all wirings in your house!",
    "august": "Make a handmade merchandise everyday!",
    "september": "Watch a new movie every weekend!",
    "october": "Participate in contest programming!",
    "november": "Get a facial at least twice a week!",
    "december": "Take herbal tea every morning!"
}

# Create your views here.


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Unsupported month!")