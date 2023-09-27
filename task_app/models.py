from django.db import models

# Create your models here.
#image time ,date 
import datetime
import os


#for image
def Taskimg(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

Priority=(
    ('Low','Low'),
    ('Media','Media'),
    ('High','High'),
)

BOOL=(
    ('Yes','Yes'),
    ('No','No'),
)

class TaskModel(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    due_date=models.DateField()
    photo=models.ImageField(upload_to=Taskimg, null=True, blank=True )
    option_priority=models.CharField(choices=Priority, max_length=100)
    task_complete=models.CharField(choices=BOOL, max_length=50)
    create_time=models.TimeField()

    class Meta:
        verbose_name = "TaskModel"
        verbose_name_plural = "TaskModel"
        