from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator, MinValueValidator
STATE_CHOICES=(
    ('Anadaman & Nicobar Island','Anadaman & Nicobar Isaland'),
    ('Andra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('chattisgarh','Chattisgarh'),
    ('Dadra & nagar Haveli','Dadra & nagar Haveli'),
    ('Daman and Diu ','Daman and Diu'),
    ('Karnatak','Karnatak'),
    ('Kearala','Kearala'),
    ('Tamilnadu','Tamilnadu'),
    ('Tripura','Tripur'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bangal'),
    ('Madya Pradesh','Madya Pradesh'),
    ('Gujarath','Gujarath'),
    ('Goa','Goa'),
    ('Dehli','Dehli'),
    ('Rajastan','Rajastan'),
    ('Jammu Kashmir','Jammu Kashmir')
    
)


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices= STATE_CHOICES, max_length=50)
    
    
    def __str__(self):
        return str(self.id)
    
    
    
    
CATEGORY_CHOICES=(
    ('M', 'mobile'),
    ('L', 'laptop'),
    ('TW', 'topwear'),
    ('BW', 'bottomwear')
)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    product_image = models.ImageField(upload_to= 'productimg')
    
    
    
    def __str__(self):
        return str(self.id)
    
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    
    
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
STATUS_CHOICES= (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)
    
    
class OredrPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer  = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    orderd_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    