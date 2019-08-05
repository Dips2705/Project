from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Product(models.Model):
	name = models.CharField(max_length=1024)
	desc = models.CharField(max_length=1024)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	imageUrl = models.CharField(max_length=1024, null=True)
	location = models.CharField(max_length=1024, null=True)

	def __str__(self):
		return f'{self.name}-({self.price}) Product'



class Buyer(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='buyerUser')
	itemsInCart = models.ManyToManyField(Product, blank=True, related_name='itemsInCart')
	location = models.CharField(max_length=1024, null=True)

	def __str__(self):
		return f'{self.user.username} Buyer'



class Traveller(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE,  related_name='travellerUser')
	origin = models.CharField(max_length=1024)
	destination = models.CharField(max_length=1024)
	day = models.DateField(default= date.today)
	itemsToBuy = models.ManyToManyField(Product, blank=True)

	def __str__(self):
		return f'{self.user.username} Traveller'



class ProductBuyer(models.Model):
	product = models.ForeignKey(Product, on_delete= models.CASCADE)
	buyer = models.ForeignKey(Buyer, on_delete= models.CASCADE)
	quantity = models.IntegerField(default=1)
	traveller = models.ForeignKey(Traveller, null=True, on_delete= models.SET_NULL)
	timeOfOrder = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f'{self.product.name} - {self.buyer.user.username}({self.timeOfOrder})'



