from django import forms
from .models import Contact, BlogPost


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['full_name', 'email', 'contact', 'message']

#         widgets = {
#             'full_name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Full Name'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Email'
#             }),
#             'contact': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Contact Number'
#             }),
#             'message': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Your Message',
#                 'rows': 5
#             }),
#         }

# class ContactForm(forms.ModelForm):

#     class Meta:
#         model = Contact
#         fields = ['full_name', 'email', 'subject', 'message']

#         widgets = {
#             'full_name': forms.TextInput(attrs={
#                 'id': 'form_name',
#                 'class': 'form-control',
#                 'placeholder': 'Full Name',
#                 'required': True,
#                 'data-error': 'Name is required.'
#             }),

#             'email': forms.EmailInput(attrs={
#                 'id': 'form_email',
#                 'class': 'form-control',
#                 'placeholder': 'Email Address',
#                 'required': True,
#                 'data-error': 'Valid email is required.'
#             }),

#             'contact': forms.TextInput(attrs={
#                 'id': 'form_subject',
#                 'class': 'form-control',
#                 'placeholder': 'Contact',
#                 'required': True,
#                 'data-error': 'Contact is required.'
#             }),

#             'message': forms.Textarea(attrs={
#                 'id': 'form_message',
#                 'class': 'form-control',
#                 'placeholder': 'Message',
#                 'rows': 7,
#                 'required': True,
#                 'data-error': 'Please, leave me a message.'
#             }),
#         }


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'contact', 'message']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'id': 'form_name',
                'name': 'name',
                'class': 'form-control',
                'placeholder': 'Full Name',
                'required': 'required',
                'data-error': 'Name is required.'
            }),

            'email': forms.EmailInput(attrs={
                'id': 'form_email',
                'name': 'email',
                'class': 'form-control',
                'placeholder': 'Email Address',
                'required': 'required',
                'data-error': 'Valid email is required.'
            }),

            'contact': forms.TextInput(attrs={
                'id': 'form_subject',
                'name': 'contact',
                'class': 'form-control',
                'placeholder': 'Contact',
                'required': 'required',
                'data-error': 'Contact is required.'
            }),

            'message': forms.Textarea(attrs={
                'id': 'form_message',
                'name': 'message',
                'class': 'form-control',
                'placeholder': 'Message',
                'rows': 7,
                'required': 'required',
                'data-error': 'Please, leave me a message.'
            }),
        }

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost

        fields = [
            "title",
            "category",
            "tags",
            "content",
            "featured_image",
            "status",
            "published_at",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "category": forms.Select(
                attrs={"class": "form-select"}
            ),
            "tags": forms.SelectMultiple(
                attrs={"class": "form-select"}
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 10,
                }
            ),
            "status": forms.Select(
                attrs={"class": "form-select"}
            ),
            "published_at": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                }
            ),
        }