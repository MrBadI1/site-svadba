from django import forms


ALCOHOL_CHOICES = [
    ("vodka", "Водка"),
    ("red_wine", "Вино красное"),
    ("white_wine", "Вино белое"),
    ("beer", "Пиво"),
    ("whiskey", "Виски"),
]


class WeddingInviteForm(forms.Form):

    name = forms.CharField(
        label="Ваше имя",
        widget=forms.TextInput(
            attrs={
                "class": "form-input"
            }
        )
    )

    will_come = forms.ChoiceField(
        choices=[
            ("yes", "Приду"),
            ("no", "Не приду"),
        ],
        widget=forms.RadioSelect(
            attrs={
                "class": "radio-input"
            }
        ),
        label="Вы придёте?"
    )

    alcohol = forms.MultipleChoiceField(
        choices=ALCOHOL_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Алкоголь"
    )

    alcohol_comment = forms.CharField(
        required=False,
        label="Уточнение",
        widget=forms.Textarea(
            attrs={
                "class": "form-input",
                "placeholder": "Например: красное — полусладкое",
                "rows": 3
            }
        )
    )