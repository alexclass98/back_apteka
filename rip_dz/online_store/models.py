from django.db import models

#Описание всех таблиц
class Drugs(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    active_substance = models.CharField(max_length=45, blank=True, null=True)
    for_children = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drugs'



class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    tel = models.CharField(max_length=45, blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class Order(models.Model):
    product = models.ForeignKey(Drugs, models.DO_NOTHING, db_column='product')
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='auth_user')
    quantity = models.IntegerField()
    price = models.IntegerField()
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    number_of_order = models.CharField(max_length=45)
    date_of_delivery = models.DateField()
    is_provider = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order'



