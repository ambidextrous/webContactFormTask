from django import forms
from send_email.models import Post

class ContactForm(forms.ModelForm):
    """
    Web contact form
    """
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True, max_length=100)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=500)

    class Meta:
        """
        Link to model, Set all fields to 'required'
        """
        model = Post
        fields = '__all__'
