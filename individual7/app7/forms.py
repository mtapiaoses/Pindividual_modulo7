from django import forms

class Login(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'w3-input'}))
    clave = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w3-input'}))

class Registro(forms.Form):
    nombre_usuario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    apellido = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    clave = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w3-input'}))
    direccion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    ciudad = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))

class Filtro(forms.Form):
    estado_choice = (('','Todos'),('Pendiente','Pendiente'),('En proceso','En proceso'),('Completado','Completado'))
    estado = forms.ChoiceField(choices=estado_choice, required=False)

# class TareaForm(forms.Form):
#     titulo = forms.CharField(label='Título', max_length=100)
#     descripcion = forms.CharField(label='Contenido', widget=forms.Textarea(attrs={'rows': 3}))
#     fecha_publicacion = forms.DateField(label='Fecha de Publicación', widget=forms.DateInput(attrs={'type': 'date'}))
#     fecha_vencimiento = forms.DateField(label='Fecha de Vencimiento', widget=forms.DateInput(attrs={'type': 'date'}))
#     estado = forms.ChoiceField(label='Estado', choices=[('Pendiente', 'Pendiente'), ('En proceso', 'En proceso'), ('Completado', 'Completado')])
#     categoria = forms.ChoiceField(label='Categoría', choices=[('Casa', 'Casa'), ('Trabajo', 'Trabajo'), ('Estudio', 'Estudios')])
#     observaciones = forms.CharField(widget=forms.Textarea, required=False)

class TareaForm(forms.Form):
    titulo = forms.CharField(
        label='Título',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    descripcion = forms.CharField(
        label='Contenido',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
    fecha_publicacion = forms.DateField(
        label='Fecha de Publicación',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    fecha_vencimiento = forms.DateField(
        label='Fecha de Vencimiento',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    estado = forms.ChoiceField(
        label='Estado',
        choices=[('Pendiente', 'Pendiente'), ('En proceso', 'En proceso'), ('Completado', 'Completado')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    categoria = forms.ChoiceField(
        label='Categoría',
        choices=[('Casa', 'Casa'), ('Trabajo', 'Trabajo'), ('Estudio', 'Estudios')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    observaciones = forms.CharField(
        label='Observaciones',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )


# class ObservacionesForm(forms.Form):
#     observaciones = forms.CharField(widget=forms.Textarea)
