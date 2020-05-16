from django.db import models
from django.contrib.auth.models import User
PREFERENCE=(
	("yes","YES"),
	("no","NO")
)
USER_FRIENDLY=(
	("yes","YES"),
	("no","NO")
)

class Owner(models.Model):
	diaryname=models.CharField(max_length=100, null=True,blank=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)

	def __str__(self):
		return f"{self.diaryname} | {self.user.username}" 

class DiaryEntries(models.Model):
	highlight=models.CharField(max_length=100, null=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	diarycontent=models.TextField(null=True)
	is_favourite=models.BooleanField(default=False)
	
	def __str__(self):
		return f"{self.highlight} | {self.user}"  

class Feedback(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	number_of_times=models.IntegerField()
	prefer=models.CharField(choices=PREFERENCE, max_length=10)
	user_friendly=models.CharField(choices=USER_FRIENDLY, max_length=10)

	def __str__(self):
		return f"{self.user}"  



