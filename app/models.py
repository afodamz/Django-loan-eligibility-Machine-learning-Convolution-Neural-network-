from django.db import models

# Create your models here.
class UserLoan(models.Model):
    GENDER_CHOICES = (('MALE', 'MALE'),
                      ('FEMALE', 'FEMALE')
                      )
    EDUCATION_CHOICES = (('GRADUATE', 'GRADUATE'),
                      ('NOT-GRADUATE', 'NOT-GRADUATE')
                      )
    PROPERTY_CHOICES = (('URBAN', 'URBAN'),
                      ('RURAL', 'RURAL'),
                      ('SEMI-URBAN', 'SEMI-URBAN')
                      )
    Gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Email = models.CharField(max_length=200, unique=True)
    Phone = models.CharField(max_length=30)
    Married = models.BooleanField(default=False)
    Dependents = models.IntegerField()
    Education = models.CharField(choices=EDUCATION_CHOICES, max_length=20)
    Self_Employed = models.BooleanField(default=False)
    ApplicantIncome = models.IntegerField()
    CoapplicantIncome = models.IntegerField()
    LoanAmount = models.IntegerField()
    Loan_Amount_Term = models.IntegerField()
    Credit_History = models.BooleanField(default=False)
    Property_Area = models.CharField(choices=PROPERTY_CHOICES, max_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.Email

    class Meta:
        db_table = "user_loan"
        verbose_name = 'User Loan'
        verbose_name_plural = 'User Loans'