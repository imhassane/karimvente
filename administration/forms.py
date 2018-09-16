from django import forms

class ProductForm(forms.Form):
    
    auto_id = True
    
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input',
        'placeholder': "Ex: table"
    }))

    category = forms.CharField(max_length=155)

    description = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'description',
        'class': 'uk-input',
        'placeholder': "Entrez la description du produit",
        "row": "10"
    }))

    price = forms.DecimalField(max_digits=7, decimal_places=2, widget=forms.NumberInput(attrs={
        'class': 'uk-input',
        'placeholder': "Entrez le prix du produit",
    }))

    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input',
        'placeholder': "Ce produit est dans quel ville ?"
    }))

    quantity = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'uk-input',
        'placeholder': "Quelle est la quantité du produit en stock ?"
    }))

    availability = forms.CharField(widget=forms.DateTimeInput(attrs={
        'class': 'uk-input',
        'placeholder': "Format: jj/mm/aa hh:mm"
    }))

    pictures = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'multiple': True
    }))
