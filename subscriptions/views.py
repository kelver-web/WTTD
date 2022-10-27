from django.shortcuts import render
from subscriptions.forms import SubscriptionForm


def subscription(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)