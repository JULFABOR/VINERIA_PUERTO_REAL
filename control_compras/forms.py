from django import forms
from Home.models import Productos, Proveedores, Compras, Detalle_Compras, Pedidos_Proveedores, Detalle_Pedidos_Proveedores

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
    def __init__(self, *args, **kwargs):
            super(ProductosForm, self).__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = '__all__'

class Detalle_ComprasForm(forms.ModelForm):
    class Meta:
        model = Detalle_Compras
        fields = '__all__'

class Pedidos_ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Pedidos_Proveedores
        fields = '__all__'

class Detalle_Pedidos_ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Detalle_Pedidos_Proveedores
        fields = '__all__'
