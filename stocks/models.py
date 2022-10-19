from django.db import models


class Services(models.Model):
    idservice = models.IntegerField(db_column='idService', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    price = models.IntegerField(blank=True, null=True)


class User(models.Model):
    iduser = models.AutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(max_length=64)
    user_email = models.CharField(unique=True, max_length=64)
    user_password = models.CharField(max_length=255)


class UserService(models.Model):
    iduserservice = models.AutoField(db_column='idUserService', primary_key=True)  # Field name made lowercase.
    id_service = models.ForeignKey(Services, models.DO_NOTHING, db_column='id_service')
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
    status = models.IntegerField()
    order_date = models.DateTimeField()