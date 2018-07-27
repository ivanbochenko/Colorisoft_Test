from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=40,
        widget=forms.TextInput(attrs={
            'class': 'input', 'type': 'text', 'placeholder': 'Прекрасная заметка!'}))

    text = forms.CharField(max_length=10000,
        widget=forms.TextInput(attrs={
            'class': 'textarea', 'placeholder': 'Не такая уж она и прекрасная'}))
