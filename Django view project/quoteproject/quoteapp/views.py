import random

quotes = [
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
]
from django.shortcuts import render

def random_quote(request):
    # Select a random quote
    selected_quote = random.choice(quotes)

    # Prepare context to pass data to the template
    context = {'quote': selected_quote}

    # Render the template with the selected quote
    return render(request, 'quoteapp/random_quote.html', context)