from django.db import models

# Create your models here.

class Approval(models.Model):
    GENDER_CHIOCES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    MARRIED_CHIOCES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    GRADUATED_CHIOCES = (
        ('Graduated', 'Graduated'),
        ('Not_Graduated', 'Not_Graduated')
    )
    SELFEMPLOYED_CHIOCES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    PROPERTY_CHIOCES = (
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban'),
        ('Urban', 'Urban')
    )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    dependants = models.IntegerField(default=0)
    coApplicantIncome = models.IntegerField(default=0)
    loanAmt = models.IntegerField(default=0)
    loanTerm = models.IntegerField(default=0)
    creditHistory = models.IntegerField(default=0)
    gender = models.CharField(max_length=15, choices=GENDER_CHIOCES)
    married = models.CharField(max_length=15, choices=MARRIED_CHIOCES)
    graduatedEducation = models.CharField(max_length=15, choices=GRADUATED_CHIOCES)
    selfEmployed = models.CharField(max_length=15, choices=SELFEMPLOYED_CHIOCES)
    area = models.CharField(max_length=15, choices=PROPERTY_CHIOCES)
    status = models.CharField(max_length=15, choices=PROPERTY_CHIOCES)

    def __str__(self):
        return self.first_name
