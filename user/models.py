from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'user'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48)
    email = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128)
    
    def __repr__(self):
        return "%s[%d]" % (self.name, self.id)