from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None

    if month == 'january':
        challenge_text = "Eat no carbs for the entire month!"
    elif month == 'february':
        challenge_text = "Walk for at least 20 minutes everyday!"
    elif month == 'march':
        challenge_text = "Learn Django for at least an hour everyday!"
    elif month == 'april':
        challenge_text = "Read at least one book per week!"
    elif month == 'may':
        challenge_text = "Go hiking every weekend!"
    elif month == 'june':
        challenge_text = "Drink 2 litres of water everyday!"
    elif month == 'july':
        challenge_text = "Change all wirings in your house!"
    elif month == 'august':
        challenge_text = "Make a handmade merchandise everyday!"
    elif month == 'september':
        challenge_text = "Watch a new movie every weekend!"
    elif month == 'october':
        challenge_text = "Participate in contest programming!"
    elif month == 'november':
        challenge_text = "Get a facial at least twice a week!"
    elif month == 'december':
        challenge_text = "Take herbal tea every morning!"
    else:
        return HttpResponseNotFound("Unsupported month!")

    return HttpResponse(challenge_text)