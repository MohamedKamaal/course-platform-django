from django.db import models

# Create your models here.

class PublishStatus(models.TextChoices):
    PUBLISHED = ('Pub', 'Published')
    DRAFT = ('draft','Draft')
    COMING_SOON = ('soon', 'Coming Soon')

class AccessRequirement(models.TextChoices):
    ANYONE = ('any', 'Anyone')
    EMAIL_REQUIRED = ('email_required', 'Email Required')
    
def handle_upload(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"{filename}"    
    

class Course(models.Model):
    """ course model """
    title= models.CharField(max_length = 120)
    description = models.TextField(blank=True ,null=True)
    image = models.ImageField(
        upload_to= handle_upload,
        blank=True,
        null=True
    )
    access = models.CharField(
        max_length = 20,
        choices= AccessRequirement.choices,
        default= AccessRequirement.ANYONE
    )
    
    status = models.CharField(
        max_length = 10,
        choices = PublishStatus.choices,
        default = PublishStatus.DRAFT
    )
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED 
        