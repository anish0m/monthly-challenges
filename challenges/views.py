from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


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


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month<1 or month>len(months):
        return HttpResponseNotFound("Unsupported month!")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Unsupported month!")