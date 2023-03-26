from django import forms

class UserForm(forms.Form):
    basket = forms.BooleanField(label="Исполнено", required=False)

class TodoItemForm(forms.ModelForm):
    title = forms.CharField(label="", max_length=40, widget=forms.TextInput(
        attrs={
        'type': 'text', 'class': 'new item', 'placeholder': 'Add item', 'aria-label': 'add list'}))

