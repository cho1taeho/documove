# class Giving(models.Model):
    id = models.IntegerField(primary_key=True)
    organization = models.JSONField()
    active = models.BooleanField()
    title = models.CharField(max_length=500)
    summary = models.TextField()
    # contactName = models.CharField(max_length=200)
    # contactAddress = models.CharField(max_length=200)
    # contactCity = models.CharField(max_length=200)
    # contactState = models.CharField(max_length=200)
    # contactPostal = models.CharField(max_length=200)
    # contactCountry = models.CharField(max_length=200)
    # contactUrl = models.URLField()
    # projectLink = models.URLField()
    # progressReportLink = models.URLField()
    themeName = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    # iso3166CountryCode = models.CharField(max_length=10)
    region = models.CharField(max_length=200)
    # goal = models.FloatField()
    funding = models.FloatField()
    remaining = models.FloatField()
    numberOfDonations = models.IntegerField()
    status = models.CharField(max_length=200)
    # need = models.TextField()
    # longTermImpact = models.TextField()
    activities = models.TextField()
    # additionalDocumentation = models.URLField()
    imageLink = models.URLField()
    imageGallerySize = models.IntegerField()
    videos = models.JSONField()
    # longitude = models.FloatField()
    # latitude = models.FloatField()
    approvedDate = models.DateTimeField()
    # donationOptions = models.JSONField()
    # modifiedDate = models.DateTimeField()
    # numberOfReports = models.IntegerField()
    # dateOfMostRecentReport = models.DateTimeField()
    themes = models.ManyToManyField(Theme)
    image = models.JSONField()
    # countries = models.ManyToManyField(Country)
    type = models.CharField(max_length=200)