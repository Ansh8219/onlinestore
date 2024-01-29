from django.db import models
from django.contrib.auth.models import User 


# Create your models here



class shoes_men(models.Model):
    shoes_company=models.CharField( max_length=50)
    
class shoes_women(models.Model):
    shoes_company=models.CharField( max_length=50)
    
class man_shoe(models.Model):
    man_fks=models.ForeignKey(shoes_men,on_delete=models.CASCADE)
    man_sopic=models.ImageField(upload_to='menshoes')
    man_so_discprtion=models.CharField( max_length=50)
    man_soprise=models.IntegerField()

class woman_shoe(models.Model):
    woman_fks=models.ForeignKey(shoes_women,on_delete=models.CASCADE)
    woman_sopic=models.ImageField(upload_to='womenshoes')
    woman_so_discprtion=models.CharField( max_length=50)
    woman_soprise=models.IntegerField()



class Tshirt_men(models.Model):
     tshirt_men=models.CharField( max_length=50)
class shirts_men(models.Model):
     shirt_men=models.CharField( max_length=50)
class jeans_men(models.Model):
     jeans_men=models.CharField( max_length=50)
     
class jacket_men(models.Model):
     jacket_men=models.CharField( max_length=50)
     
     

    

    
class Tshirt_women(models.Model):
     tshirt_women=models.CharField( max_length=50)
class shirts_women(models.Model):
     shirt_women=models.CharField( max_length=50)
class jeans_women(models.Model):
     jeans_women=models.CharField( max_length=50)
     
class jacket_women(models.Model):
     jacket_women=models.CharField( max_length=50)
     
     
class Tshirts_women_data(models.Model):
    woman_fks=models.ForeignKey(Tshirt_women,on_delete=models.CASCADE)
    woman_sopic=models.ImageField(upload_to='Tshirts_womens')
    woman_so_discprtion=models.CharField( max_length=50)
    woman_soprise=models.IntegerField()


class shirts_women_data(models.Model):
    woman_fks=models.ForeignKey(shirts_women,on_delete=models.CASCADE)
    woman_sopic=models.ImageField(upload_to='shirts_women')
    woman_so_discprtion=models.CharField( max_length=50)
    woman_soprise=models.IntegerField()
    
class jeans_women_data(models.Model):
    woman_fks=models.ForeignKey(jeans_women,on_delete=models.CASCADE)
    woman_sopic=models.ImageField(upload_to='jeans_women')
    woman_so_discprtion=models.CharField( max_length=50)
    woman_soprise=models.IntegerField()
    
    
class jacket_women_data(models.Model):
    woman_fks=models.ForeignKey(jacket_women,on_delete=models.CASCADE)
    woman_sopic=models.ImageField(upload_to='jacket_women')
    woman_so_discprtion=models.CharField( max_length=50)
    woman_soprise=models.IntegerField()
    
    
class Tshirt_men_data(models.Model):
    man_fks=models.ForeignKey(Tshirt_men,on_delete=models.CASCADE)
    man_sopic=models.ImageField(upload_to='Tshirts_men')
    man_so_discprtion=models.CharField( max_length=50)
    man_soprise=models.IntegerField()
    
    
    
    
class shirts_men_data(models.Model):
    man_fks=models.ForeignKey(shirts_men,on_delete=models.CASCADE)
    man_sopic=models.ImageField(upload_to='Shirts_men')
    man_so_discprtion=models.CharField( max_length=50)
    man_soprise=models.IntegerField()
    
    
class jeans_men_data(models.Model):
    man_fks=models.ForeignKey(jeans_men,on_delete=models.CASCADE)
    man_sopic=models.ImageField(upload_to='jeans_men')
    man_so_discprtion=models.CharField( max_length=50)
    man_soprise=models.IntegerField()
    
    
    
class jacket_men_data(models.Model):
    man_fks=models.ForeignKey(jacket_men,on_delete=models.CASCADE)
    man_sopic=models.ImageField(upload_to='jackets_men')
    man_so_discprtion=models.CharField( max_length=50)
    man_soprise=models.IntegerField()
    
    
    
    
    


    
    