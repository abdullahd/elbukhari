from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from datetime import timedelta

from .forms import NewsletterSubscriptionForm
from .models import NewsletterSubscriber

# Create your views here.

@require_http_methods(["GET", "POST"])
def newsletter_subscribe(request):
    """Handle newsletter subscription"""
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            subscriber = form.save(commit=True, request=request)
            messages.success(
                request,
                _('Thank you for subscribing! Please check your email to confirm your subscription.')
            )
            return redirect('newsletter_success')
    else:
        form = NewsletterSubscriptionForm()
    
    return render(request, 'newsletter/subscribe.html', {'form': form})

def newsletter_confirm(request, token):
    """Confirm newsletter subscription"""
    # Look for the token, limiting to tokens created in the last 7 days
    valid_from = timezone.now() - timedelta(days=7)
    subscriber = get_object_or_404(
        NewsletterSubscriber,
        confirmation_token=token,
        confirmation_sent_at__gte=valid_from,
        confirmed=False
    )
    
    subscriber.confirm_subscription()
    messages.success(request, _('Thank you! Your subscription has been confirmed.'))
    return redirect('newsletter_confirmed')

def newsletter_success(request):
    """Show success page after form submission"""
    return render(request, 'newsletter/success.html')

def newsletter_confirmed(request):
    """Show confirmation success page"""
    return render(request, 'newsletter/confirmed.html')

def newsletter_unsubscribe(request, email_encoded):
    """Handle unsubscription"""
    # Simple encoding/decoding for the email in URL
    import base64
    try:
        email = base64.b64decode(email_encoded).decode('utf-8')
        subscriber = get_object_or_404(NewsletterSubscriber, email=email)
        
        if request.method == 'POST':
            subscriber.is_active = False
            subscriber.save(update_fields=['is_active'])
            messages.success(request, _('You have been unsubscribed from our newsletter.'))
            return redirect('newsletter_unsubscribed')
        
        return render(request, 'newsletter/unsubscribe_confirm.html', {'email': email})
    
    except Exception:
        return HttpResponse(_('Invalid unsubscribe link'), status=400)

def newsletter_unsubscribed(request):
    """Show unsubscribe confirmation page"""
    return render(request, 'newsletter/unsubscribed.html')
