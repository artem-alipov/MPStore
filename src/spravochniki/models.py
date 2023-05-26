from django.db import models

# Create your models here.

class Oblast(models.Model):
 name = models.CharField(   
        verbose_name="Oblast name",
        max_length=20
    )
def __str__(self):
        return self.name

class Region(models.Model):
    Oblast = models.ForeignKey(
        "spravochniki.Oblast",
        on_delete=models.PROTECT,
        verbose_name="Oblast",
        default=1,
        related_name="regions"
    )
    name = models.CharField(   
        verbose_name="Region name",
        max_length=20
    )
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    region = models.ForeignKey(
        "spravochniki.Region",
        on_delete=models.PROTECT,
        verbose_name="Region",
        related_name="cities"
    )
    name = models.CharField(   
        verbose_name="City name",
        max_length=20
    )

    description = models.TextField(
        verbose_name="City description",
        null=True,
        blank=True
)
    
    def __str__(self):
        return self.name

class PublicHollydays(models.Model):
    name = models.CharField(
        verbose_name="Hollyday name",
        max_length=255
    )
    holliday_date = models.DateField(
        verbose_name="Hollyday name",
    )
    description = models.TextField(
        verbose_name="Hollyday description",
        null=True,
        blank=True
    )
    created = models.DateTimeField(
        verbose_name="Created datetimed",
        auto_now=False,
        auto_now_add=True
       )
    update = models.DateField(
        verbose_name="Updated datetime",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return self.name

