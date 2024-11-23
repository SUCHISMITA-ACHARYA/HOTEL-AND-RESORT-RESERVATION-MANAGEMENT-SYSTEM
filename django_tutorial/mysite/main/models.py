from django.db import models

class hotel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Create your models here.
class hotel_detail(models.Model):
    h = models.ForeignKey(hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    ratings=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    types_of_room_available=models.CharField(max_length=100)
    address=models.CharField(max_length=300, default='Unknown')

    def __str__(self):
        return self.name
    
class resort(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class resort_detail(models.Model):
    r = models.ForeignKey(resort, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    ratings=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    types_of_room_available=models.CharField(max_length=100)
    address=models.CharField(max_length=300, default='Unknown')
    
    def __str__(self):
        return self.name
    








class  desc(models.Model):
    h = models.ForeignKey(hotel, on_delete=models.CASCADE)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.description
    
class  rats(models.Model):
    h = models.ForeignKey(hotel, on_delete=models.CASCADE)
    ratings=models.CharField(max_length=100)

    def __str__(self):
        return self.ratings

class  price(models.Model):
    h = models.ForeignKey(hotel, on_delete=models.CASCADE)
    price=models.CharField(max_length=100)

    def __str__(self):
        return self.price
    
    
class tora(models.Model):
    h = models.ForeignKey(hotel, on_delete=models.CASCADE)
    types_of_room_available=models.CharField(max_length=100)

    def __str__(self):
        return self.types_of_room_available
    
class  address(models.Model):
    h = models.ForeignKey(hotel, on_delete=models.CASCADE)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.address

    


    
    
