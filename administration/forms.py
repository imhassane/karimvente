from django import forms

class ProductForm(forms.Form):
    
    auto_id = True
    
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input',
        'placeholder': "Ex: table"
    }))

    category = forms.CharField(widget=forms.SelectMultiple(attrs={
        'class': 'uk-input'
    }, choices=(
        ("Chambres", "Chambres"),
        ("Salons", "Salons"),
        ("Terasses", "Terasses")
    )))

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
        'placeholder': "Format: aaaa-mm-jj"
    }))

    pictures = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'multiple': True
    }))


class CategoryForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'description',
        'class': 'uk-input',
        "row": "10"
    }))

    image = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': 'uk-input'
    }))
