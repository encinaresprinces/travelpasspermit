from django.db import models

'''Gender_CHOICES = (
   ('Male', 'Male'),
   ('Female', 'Female')
)'''

class Barangay(models.Model):
	zbarangay = models.CharField(max_length=50, default="")
	municipal = models.CharField(max_length=50, default="")
	address = models.CharField(max_length=50, default="")
	class meta:
		db_table = "vbarangay"

class TravelerProfile(models.Model):

	barangay = models.ForeignKey(Barangay, on_delete=models.CASCADE)
	Tname = models.TextField(max_length=50, default="")
	'''age = models.IntegerField( default="")'''
	birthday = models.CharField(max_length=10, default="")
	gender = models.TextField(max_length=10, default="")
	address = models.CharField(max_length=50, default="")
	cnumber = models.IntegerField(default="")
	email = models.CharField(max_length=50, default="")
	class meta:
		db_table = "travelerprofile"

class Trequest(models.Model):

	travelprofile = models.ForeignKey(TravelerProfile, on_delete=models.CASCADE)
	departuredate = models.DateField(max_length=12, default="")
	returndate = models.DateField(max_length=12, default="")
	destinationtravel = models.CharField(max_length=50, default="")
	class meta:
		db_table = "trequest"


class Requirements(models.Model):
	
	travelprofile = models.ForeignKey(TravelerProfile, on_delete=models.CASCADE)
	swabresult = models.TextField(max_length=50, default="")
	identificationCards = models.FileField(upload_to='documents/')
	transportation = models.TextField(max_length=50, default="")
	class meta:
		db_table = "trequirements"

class Status(models.Model):

	requirements = models.ForeignKey(Requirements, on_delete=models.CASCADE)
	rstatus= models.TextField(max_length=50, default="")
	remarks = models.TextField(max_length=50, default="")
	class meta:
		db_table = "Status"
