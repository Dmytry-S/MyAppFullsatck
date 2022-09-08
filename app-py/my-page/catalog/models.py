from django.db import models


# Create your models here.
class MyJob(models.Model):
    my_job = models.CharField(max_length=15, help_text="My current job")

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.my_job
