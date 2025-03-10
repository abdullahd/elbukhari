from django import forms
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from .models import NewsletterSubscriber

class NewsletterSubscriptionForm(forms.ModelForm):
    """Form for newsletter subscription"""
    email = forms.EmailField(
        label=_('Email Address'),
        validators=[EmailValidator()],
        widget=forms.EmailInput(attrs={
            'placeholder': _('Your email address'),
            'class': 'form-control'
        })
    )
    name = forms.CharField(
        label=_('Name'),
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': _('Your name (optional)'),
            'class': 'form-control'
        })
    )
    
    # Optional checkboxes for interests
    interests = forms.MultipleChoiceField(
        choices=NewsletterSubscriber.INTEREST_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'interest-checkbox'})
    )
    
    class Meta:
        model = NewsletterSubscriber
        fields = ['email', 'name', 'interests']
    
    def clean_email(self):
        """Check if email already exists"""
        email = self.cleaned_data.get('email')
        
        # Check if this email is already subscribed and confirmed
        existing = NewsletterSubscriber.objects.filter(email=email, confirmed=True).first()
        if existing and existing.is_active:
            raise forms.ValidationError(_('This email is already subscribed to our newsletter.'))
        
        return email
    
    def save(self, commit=True, request=None):
        """Save the form and send confirmation email"""
        instance = super().save(commit=False)
        
        # Convert interests list to comma-separated string
        interests = self.cleaned_data.get('interests', [])
        instance.interests = ','.join(interests)
        
        if commit:
            # Check if this email already exists but is unconfirmed
            existing = NewsletterSubscriber.objects.filter(email=instance.email).first()
            if existing:
                # Update the existing record
                existing.name = instance.name
                existing.interests = instance.interests
                existing.is_active = True
                existing.save()
                
                # Re-send confirmation if needed
                if not existing.confirmed:
                    existing.send_confirmation_email(request)
                
                return existing
            else:
                # Save new subscriber
                instance.save()
                # Send confirmation email
                if request:
                    instance.send_confirmation_email(request)
        
        return instance 