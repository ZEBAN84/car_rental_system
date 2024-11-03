from django.db import models

# Create your models here.
class Tbl_User(models.Model):
	name=models.CharField(max_length=30,default='')
	phone=models.CharField(max_length=50,default='')
	address=models.CharField(max_length=30,default='')
	email=models.CharField(max_length=30,default='')
	pswd=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=30,default='')
	user_type=models.CharField(max_length=30,default='')
	idproof=models.ImageField(upload_to='pic/',default='')

	def __str__(self):
		return self.name

class Tbl_Product(models.Model):
	user_id=models.ForeignKey(Tbl_User,on_delete=models.CASCADE, blank=True,null=True)
	img=models.ImageField(upload_to='pic/',default='')
	name=models.CharField(max_length=30,default='')
	car_number=models.CharField(max_length=50,default='')
	seat=models.CharField(max_length=30,default='')
	specification=models.CharField(max_length=30,default='')
	price=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=30,default='')

class Tbl_feedback(models.Model):
	user_id=models.ForeignKey(Tbl_User,on_delete=models.CASCADE, blank=True,null=True)
	feedback=models.CharField(max_length=30,default='')

class Tbl_booking(models.Model):
	buyer_id=models.ForeignKey(Tbl_User,on_delete=models.CASCADE, blank=True,null=True)
	# owner_id=models.CharField(max_length=30,default='')
	product_id=models.ForeignKey(Tbl_Product,on_delete=models.CASCADE, blank=True,null=True)
	date=models.CharField(max_length=30,default='')
	fromdate=models.CharField(max_length=30,default='')
	todate=models.CharField(max_length=30,default='')
	day=models.CharField(max_length=30,default='')
	totalprice=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=30,default='')
	owner_email=models.CharField(max_length=30,default='')


class Tbl_driverBook(models.Model):
	buyer_id=models.ForeignKey(Tbl_User,on_delete=models.CASCADE, blank=True,null=True)
	driverid=models.CharField(max_length=30,default='')
	driver_email=models.CharField(max_length=30,default='')
	driver_phone=models.CharField(max_length=30,default='')
	date=models.CharField(max_length=30,default='')
	fromdate=models.CharField(max_length=30,default='')
	todate=models.CharField(max_length=30,default='')
	day=models.CharField(max_length=30,default='')
	totalprice=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=30,default='')

class Tbl_complaint(models.Model):
	buyer_id=models.ForeignKey(Tbl_User,on_delete=models.CASCADE, blank=True,null=True)
	police_email=models.CharField(max_length=30,default='')
	subject=models.CharField(max_length=30,default='')
	description=models.CharField(max_length=30,default='')
	location=models.CharField(max_length=30,default='')
	date=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=30,default='')
	reply=models.CharField(max_length=30,default='')

class Tbl_buyer_payment(models.Model):
	buyer_id=models.ForeignKey(Tbl_User,on_delete=models.CASCADE, blank=True,null=True)
	driver_id=models.ForeignKey(Tbl_User,on_delete=models.CASCADE, blank=True,null=True,related_name='driver')
	cardname=models.CharField(max_length=250,default='')
	cardnum=models.CharField(max_length=255,default='')
	expiry=models.CharField(max_length=250,default='')
	cvvnum=models.CharField(max_length=250,default='')
	status=models.CharField(max_length=250,default='')
	price=models.CharField(max_length=250,default='')


class Tbl_buyer_car_payment(models.Model):
	buyer_id=models.ForeignKey(Tbl_User,on_delete=models.CASCADE, blank=True,null=True)
	owner_email=models.CharField(max_length=250,default='')
	cardname=models.CharField(max_length=250,default='')
	cardnum=models.CharField(max_length=255,default='')
	expiry=models.CharField(max_length=250,default='')
	cvvnum=models.CharField(max_length=250,default='')
	price=models.CharField(max_length=250,default='')
	status=models.CharField(max_length=255,default='')


class Tbl_Review(models.Model):
	product_id=models.ForeignKey(Tbl_Product,on_delete=models.CASCADE, blank=True,null=True)
	user_id=models.ForeignKey(Tbl_User,on_delete=models.CASCADE, blank=True,null=True)
	review=models.CharField(max_length=100,default='')
	# reply=models.CharField(max_length=100,default='')
	# status=models.CharField(max_length=100,default='')
	
