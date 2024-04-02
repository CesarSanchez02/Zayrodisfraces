from allauth.account.adapter import DefaultAccountAdapter

class CustomUserAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
        user.direccion = form.cleaned_data.get('direccion')
        user.telefono = form.cleaned_data.get('telefono')

        if commit:
            user.save()

        return user
