from django.db import models
from django.db.models.enums import Choices
from django.db.models.expressions import ValueRange

# Create your models here.
class Client(models.Model):
    Firstname=models.CharField(max_length=50, verbose_name='Nombre(s)')
    Lastname1=models.CharField(max_length=50,verbose_name='Apellido Paterno')
    Lastname2=models.CharField(max_length=50,verbose_name='Apellido Materno')
    Age=models.IntegerField(verbose_name='Edad')
    CP=models.IntegerField(verbose_name='Codigo Postal')
    Location=models.CharField(max_length=50,verbose_name='Localidad')
    Street=models.CharField(max_length=50,verbose_name='Calle')
    Municipality=models.CharField(max_length=50,verbose_name='Municipio')
    State=models.CharField(max_length=50,verbose_name='Estado')
    Phone=models.CharField(max_length=15,verbose_name='Telefono')

    def __str__(self):
        return "{0} {1} {2}" .format(self.Firstname, self.Lastname1, self.Lastname2)

    class Meta:
        verbose_name="Cliente"
        verbose_name_plural="Clientes"

class Doctor(models.Model):
    Firstname=models.CharField(max_length=50, verbose_name='Nombre(s)')
    Lastname1=models.CharField(max_length=50,verbose_name='Apellido Paterno')
    Lastname2=models.CharField(max_length=50,verbose_name='Apellido Materno')
    Age=models.IntegerField(verbose_name='Edad')
    CP=models.IntegerField(verbose_name='Codigo Postal')
    Location=models.CharField(max_length=50,verbose_name='Localidad')
    Street=models.CharField(max_length=50,verbose_name='Calle')
    Municipality=models.CharField(max_length=50,verbose_name='Municipio')
    State=models.CharField(max_length=50,verbose_name='Estado')
    Phone=models.CharField(max_length=15,verbose_name='Telefono')
    Professional = models.CharField(max_length=15, verbose_name='Cedula Profesional')

    def __str__(self):
        return "{0} {1} {2}" .format(self.Firstname,self.Lastname1,self.Lastname2)

    class Meta:
        verbose_name="Medico"
        verbose_name_plural="Medicos"

class Vendor(models.Model):
    Firstname=models.CharField(max_length=50, verbose_name='Nombre(s)')
    Lastname1=models.CharField(max_length=50,verbose_name='Apellido Paterno')
    Lastname2=models.CharField(max_length=50,verbose_name='Apellido Materno')
    Age=models.IntegerField(verbose_name='Edad')
    CP=models.IntegerField(verbose_name='Codigo Postal')
    Location=models.CharField(max_length=50,verbose_name='Localidad')
    Street=models.CharField(max_length=50,verbose_name='Calle')
    Municipality=models.CharField(max_length=50,verbose_name='Municipio')
    State=models.CharField(max_length=50,verbose_name='Estado')
    Phone=models.CharField(max_length=15,verbose_name='Telefono')
    
    def __str__(self):
        return "{0} {1} {2}" .format(self.Firstname,self.Lastname1,self.Lastname2)

    class Meta:
        verbose_name="Vendedor"
        verbose_name_plural="Vendedores"

class Provider(models.Model):
    Firstname=models.CharField(max_length=50, verbose_name='Nombre(s)')
    Lastname1=models.CharField(max_length=50,verbose_name='Apellido Paterno')
    Lastname2=models.CharField(max_length=50,verbose_name='Apellido Materno')
    Phone=models.CharField(max_length=15,verbose_name='Telefono')

    def __str__(self):
        return "{0} {1} {2}" .format(self.Firstname,self.Lastname1,self.Lastname2)

    class Meta:
        verbose_name="Proveedor"
        verbose_name_plural="Proveedores"

class Service(models.Model):
    Name=models.CharField(max_length=50 ,verbose_name="Nombre del servicio")
    Description = models.CharField(max_length=500, verbose_name="Descripción")


    def __str__(self):
        return "{0}" .format(self.Name)

    class Meta:
        verbose_name="Servicio"
        verbose_name_plural="Servicios"


MASCOTTYPE=[('Felino','Felino'),('Canino','Canino'), ('Reptil','Reptil'), ('Ave','Ave'),('Animal de granja','Animal de granja'),('Roedor','Roedor')]


class Mascot(models.Model):
    Name=models.CharField(max_length=50, verbose_name='Nombre(s)')
    Race=models.CharField(max_length=50,verbose_name='Raza')
    Color=models.CharField(max_length=50,verbose_name='Color')
    Age=models.CharField(max_length=50,verbose_name='Edad')
    Type=models.CharField(choices=MASCOTTYPE, verbose_name='Especie', max_length=20)
    Client=models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    Foto=models.ImageField(verbose_name='Agregar imagen', null=True, upload_to='imgMascot')


    def __str__(self):
        return "{0} {1}" .format(self.Name,self.Race)
    
    class Meta:
        verbose_name="Mascota"  
        verbose_name_plural="Mascotas"


class Product(models.Model):
    Name=models.CharField(max_length=50, verbose_name='Nombre')
    Quantity=models.IntegerField(verbose_name='Cantidad',)
    Price=models.DecimalField(verbose_name='Precio', max_digits=5,decimal_places=2, default=0.00)
    Expiration=models.DateField(verbose_name='Fecha de Caducidad')
    Provider=models.ForeignKey(Provider,on_delete=models.CASCADE, verbose_name='Proveedor')

    def __str__(self):
        return "{0} {1}" .format(self.Name,self.Price,self.Provider)
    
    class Meta:
        verbose_name="Producto"  
        verbose_name_plural="Productos"

class Office(models.Model):
    Name=models.CharField(max_length=50, verbose_name='Nombre')
    CP=models.IntegerField(verbose_name='Codigo Postal')
    Location=models.CharField(max_length=50,verbose_name='Localidad')
    Street=models.CharField(max_length=50,verbose_name='Calle')
    Municipality=models.CharField(max_length=50,verbose_name='Municipio')
    State=models.CharField(max_length=50,verbose_name='Estado')
    Phone=models.CharField(max_length=15,verbose_name='Telefono')

    def __str__(self):
        return "{0}" .format(self.name)
    
    class Meta:
        verbose_name="Sucursal"  
        verbose_name_plural="Sucursales"

class Cite(models.Model):
    Date=models.DateField(verbose_name='Fecha de la cita')
    Service=models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Tipo de servicio')
    Doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE,verbose_name='Medico')
    Product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Producto')
    Client=models.ForeignKey(Client,on_delete=models.CASCADE,verbose_name='Cliente')

    def __str__(self):
        return "Fecha de la cita: {0}   Cliente: {1} " .format(self.Date, self.Client)
    
    class Meta:
        verbose_name="Cita"  
        verbose_name_plural="Citas"



class Sale(models.Model):
    Date=models.DateField(verbose_name='Fecha de la compra')
    Office=models.ForeignKey(Office,on_delete=models.CASCADE,verbose_name='Sucursal')
    Client=models.ForeignKey(Client,on_delete=models.CASCADE,verbose_name='Cliente')
    Product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Producto')

    def __str__(self):
        return "Fecha de la Venta: {0}   Cliente: {1} " .format(self.Date, self.Client)
    
    class Meta:
        verbose_name="Venta"  
        verbose_name_plural="Ventas"
   




