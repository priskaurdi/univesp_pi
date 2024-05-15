from django.db import models
from datetime import datetime
# Create your models here. 


## Opções de Itens
class TypeItem(models.TextChoices):
    BLOUSE = 'BLUSA','BLUSA'
    PANTS = 'CALCA','CALCA'
    HANDBAG = 'BOLSA','BOLSA'
    DRESS = 'VESTIDO', 'VESTIDO'
    TSHIRT = 'CAMISETA', 'CAMISETA'

## Cadastro de Itens
class Item(models.Model):
    code = models.CharField(max_length=100)
    type_item = models.CharField(max_length=100, choices=TypeItem.choices)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    is_reserved = models.BooleanField(default=False)
    
    
    def __str__(self):
        return "{} - {}".format(self.code, self.type_item)
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        ordering = ['-id']

## Cadastrar as Imagens do Item
class ItemImage(models.Model):
    image = models.ImageField('Images',upload_to='images')
    item = models.ForeignKey(Item, related_name='item_images', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item.code # form key
    
# Registrar Reserva - adaptação final:
class RegisterReservation(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reg_reservation')
    booking_date = models.DateTimeField('Data')
    create_at = models.DateField(default=datetime.now, blank=True)
    name = models.CharField(max_length=100, blank=False, null=False)   
    email = models.EmailField(max_length=200, blank=True, null=True)   
    phone = models.CharField(max_length=15, blank=False, null=False)   

    def __str__(self):
        return "{}".format(self.item)

    class Meta:
        verbose_name = 'Registrar Reserva'
        verbose_name_plural = 'Registrar Reservas'
        ordering = ['-id']

# Registrar Agendamento
class RegisterAppointment(models.Model): #Registrar agendamento
    booking_date = models.DateTimeField('Data')
    create_at = models.DateField(default=datetime.now, blank=True)
    name = models.CharField(max_length=100, blank=False, null=False)   
    email = models.EmailField(max_length=200, blank=True, null=True)   
    phone = models.CharField(max_length=15, blank=False, null=False)   
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Registrar Agendamento'
        verbose_name_plural = 'Registrar Agendamentos'
        ordering = ['-id']