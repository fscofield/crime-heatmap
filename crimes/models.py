from django.db import models

class Crime(models.Model):

    unit_id = models.CharField(max_length=15)
    case_num = models.CharField('police case number', max_length=30)
    date = models.DateTimeField('datetime of crime')
    block = models.CharField('cross streets', max_length=100)
    iucr = models.CharField('police code', max_length=25)
    crime_type = models.CharField('type of crime', max_length=50)
    description = models.CharField('description of offence', max_length=200)
    location_type = models.CharField('type of location', max_length=50)
    arrest = models.BooleanField('1 if arrested')
    domestic = models.BooleanField('1 if domestic')
    beat = models.CharField('beat (district type) number', max_length=25)
    ward = models.IntegerField('ward number')
    fbi_code = models.CharField('FBI Code', max_length=10)
    x_cd = models.IntegerField('X Coordinate')
    y_cd = models.IntegerField('Y Coordinate')
    year = models.IntegerField('year of occurance')
    latitude = models.DecimalField('latitude', max_digits=20, decimal_places=15)
    longitude = models.DecimalField('longitude', max_digits=20, decimal_places=15)
    updated_on = models.DateTimeField('last updated datetime')


    def __unicode__(self):
        return "%s, %s, %s" % (self.crime_type, self.case_num, self.date)
