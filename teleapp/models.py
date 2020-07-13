from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
#from currentaffairs import settings
#collection=settings.MONGO_DB.collection

#from django.conf import settings

#tb_tutorial_collection = settings.MONGO_DB.tb_tutorial_collection

class pdf(models.Model):
    chatid=models.IntegerField(default=0)
    pdf=models.FileField()
#class Event(models.Model):
 #   title = models.CharField(max_length=255)
  #  description = models.TextField(blank=True)
   # start_date = models.DateTimeField(null=True)



#vivek info
#api_id=1564169
#api_hash=932f6545cdc73ab259a5cf3c0d9ef557

#subodh info
#api_id = 1586339
#api_hash = 52dcf6e77d0dab47c918261e7532d6b1
