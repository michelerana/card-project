from django.db import models

class Companies(models.Model):
    id = models.AutoField(primary_key = True, editable = False)
    name = models.CharField(max_length = 100)
    vat = models.CharField(max_length = 11) # partita iva
    office = models.CharField(max_length = 100) # indirizzo sede legale
    city = models.CharField(max_length = 50) # citta sede legale
    email = models.EmailField() # email sede legale
    password = models.CharField(max_length = 30) 
    phone = models.CharField(max_length = 10) # telefono sede legale

class Stores(models.Model):
    id = models.AutoField(primary_key = True, editable = False)
    id_company = models.ForeignKey('Companies')
    address = models.CharField(max_length = 30)
    city = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 10)

class Items(models.Model):
    id = models.AutoField(primary_key = True, editable = False)
    name = models.CharField(max_length = 100)

class Sellings (models.Model): # tabella di congiunzione dell'associazione N-N Punto_Vendita - Prodotto
    id_store = models.ForeignKey('Stores', primary_key = True)
    id_item = models.ForeignKey('Items', primary_key = True)
    quantity = models.PositiveIntegerField(null = False)

class Points(models.Model):
    id = models.AutoField(primary_key = True, editable = False)
    id_card = models.ForeignKey('user.Users', null = False)
    id_item = models.ForeignKey('Items', null = False)
    assigning = models.DateTimeField(null = False) # data assegnazione
    expiration = models.DateTimeField(null = False) # data di scadenza

# Create your models here.
