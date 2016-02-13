from django.db import models

class geoname (models.Model):
    geonameid = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200, null = True)
    asciiname = models.CharField(max_length = 200, null = True)
    alternatenames = models.TextField(null = True)
    latitude = models.FloatField(null = True)
    longitude = models.FloatField(null = True)
    fclass = models.CharField(max_length = 1, null = True)
    fcode = models.CharField(max_length = 10, null = True)
    country = models.CharField(max_length = 2, null = True)
    cc2 = models.CharField(max_length = 60, null = True)
    admin1 =  models.CharField(max_length = 20, null = True)
    admin2 =  models.CharField(max_length = 80, null = True)
    admin3 =  models.CharField(max_length = 20, null = True)
    admin4 = models.CharField(max_length = 20, null = True)
    population = models.BigIntegerField(null = True)
    elevation = models.IntegerField(null = True)
    gtopo30 = models.IntegerField(null = True)
    timezone =  models.CharField(max_length = 40, null = True)
    moddate = models.DateField(null = True)

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.country, self.elevation)

class tags (models.Model):
    tagid = models.AutoField(primary_key = True)
    tagname = models.CharField(max_length = 100, null = True)

class usertags (models.Model):
    usertagid = models.AutoField(primary_key = True)
    userid = models.IntegerField(null = True)
    tagid = models.IntegerField(null = True)
    geonameid = models.IntegerField(null = True)

class alternatename (models.Model):
    alternatenameid = models.AutoField(primary_key = True)
    geonameid = models.IntegerField(null = True)
    isolanguage = models.CharField (max_length = 7, null = True)
    alternatename = models.CharField (max_length = 200, null = True)
    ispreferredname = models.NullBooleanField(null = True)
    isshortname = models.NullBooleanField(null = True)
    iscolloquial = models.NullBooleanField(null = True)
    ishistoric = models.NullBooleanField(null = True)

class countryinfo (models.Model):
    iso_alpha2 = models.CharField(primary_key = True, max_length = 2)
    iso_alpha3 = models.CharField (max_length = 3, null = True)
    iso_numeric = models.IntegerField(null = True)
    fips_code = models.CharField (max_length = 3, null = True)
    name = models.CharField(max_length = 200, null = True)
    capital = models.CharField(max_length = 200, null = True)
    areainsqkm =  models.FloatField(null = True)
    population = models.IntegerField(null = True)
    continent = models.CharField(max_length = 2, null = True)
    tld = models.CharField(max_length = 10, null = True)
    currencycode = models.CharField (max_length = 3, null = True)
    currencyname = models.CharField (max_length = 20, null = True)
    phone = models.CharField (max_length = 20, null = True)
    postalcode = models.CharField (max_length = 100, null = True)
    postalcoderegex = models.CharField (max_length = 200, null = True)
    languages = models.CharField (max_length = 200, null = True)
    geonameid = models.IntegerField(null = True)
    #geoname = models.ForeignKey(geoname)
    neighbors = models.CharField (max_length = 50, null = True)
    equivfipscode = models.CharField (max_length = 2, null = True)

class iso_languagecodes (models.Model):
    iso_639_3 = models.CharField (max_length = 4, null = True)
    iso_639_2 = models.CharField (max_length = 50, null = True)
    iso_639_1 = models.CharField (max_length = 50, null = True)
    language_name = models.CharField (max_length = 200, null = True)

class admin1codesascii (models.Model):
    code = models.CharField (max_length = 20, null = True)
    name = models.TextField (null = True)
    nameascii = models.TextField (null = True)
    geonameid = models.IntegerField(null = True)

class admin2codesascii (models.Model):
    code = models.CharField (max_length = 80, null = True)
    name = models.TextField (null = True)
    nameascii = models.TextField (null = True)
    geonameid = models.IntegerField(null = True)

class featurecodes (models.Model):
    code = models.CharField (max_length = 7, null = True)
    name  = models.CharField (max_length = 200, null = True)
    description = models.TextField (null = True)

class timezones (models.Model):
    country = models.CharField(max_length = 2, null = True)
    timezoneid = models.CharField (max_length = 200, null = True)
    gmt_offset = models.DecimalField (max_digits = 3, decimal_places = 1)
    dst_offset = models.DecimalField (max_digits = 3, decimal_places = 1)
    raw_offset = models.DecimalField (max_digits = 3, decimal_places = 1)

class continentcodes (models.Model):
    code = models.CharField(max_length = 2, null = True)
    name   = models.CharField (max_length = 20, null = True)
    geonameid = models.IntegerField(null = True)

class postalcodes (models.Model):
    countrycode = models.CharField(max_length = 2, null = True)
    postalcode = models.CharField(max_length = 20, null = True)
    placename = models.CharField(max_length = 180, null = True)
    admin1name = models.CharField(max_length = 100, null = True)
    admin1code = models.CharField(max_length = 20, null = True)
    admin2name = models.CharField(max_length = 100, null = True)
    admin2code = models.CharField(max_length = 20, null = True)
    admin3name = models.CharField(max_length = 100, null = True)
    admin3code = models.CharField(max_length = 20, null = True)
    latitude = models.FloatField(null = True)
    longitude = models.FloatField(null = True)
    accuracy = models.IntegerField(null = True)
