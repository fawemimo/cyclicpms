from django.db import models
from django.shortcuts import reverse

# Create your models here.

class BankDetail(models.Model):

    user_id                 = models.IntegerField()
    full_name               = models.CharField(max_length=255)
    bank_name               = models.CharField(max_length=255)
    account_number          = models.CharField(max_length=255)
    bvn                     = models.CharField(max_length=255)
    sort_code               = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Bank Detail")
        verbose_name_plural = ("Bank Details")

    def __str__(self):
        return self.full_name

    # def get_absolute_url(self):
    #     return reverse("BankDetail_detail", kwargs={"pk": self.pk})


class PersonalInfo(models.Model):

    user_id                     = models.IntegerField()    
    full_name                   = models.CharField(max_length=255)
    dob                         = models.DateField(blank=True,null=True)    
    # dob_attach                  = models.FileField(upload_to='confidentials',blank=True,null=True)
    dob_verify                  = models.IntegerField(default = 0)
    parmanent_home_address      = models.CharField(max_length=200)
    parmanent_address_verify    = models.IntegerField(default = 0)
    contact_address             = models.CharField(max_length=255)
    contact_verify              = models.IntegerField(default = 0)
    phone_number                = models.CharField(max_length=100)
    phone_number_2              = models.CharField(max_length=100)    
    pension_house               = models.CharField(max_length=200)
    pension_number              = models.CharField(max_length=200)
    PAYEE_ID                    = models.CharField(max_length=200)
    NHF_ID                      = models.CharField(max_length=200)
    employment_date             = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Personal Info")
        verbose_name_plural = ("Personal Infos")

    def __str__(self):
        return self.full_name


class Education(models.Model):

    user_id                     = models.IntegerField()    
    full_name                   = models.CharField(max_length=255)
    institution                 = models.CharField(max_length=200)
    date_from                   = models.DateTimeField()
    date_to                     = models.DateTimeField(blank=True,null=True)
    
    date_current                = models.BooleanField(default = False)
    degree                      = models.CharField(max_length=200)
    degree_authenticate         = models.IntegerField(default = 0)
    # degree_attach               = models.FileField(upload_to='confidentials')
    course                      = models.CharField(max_length=200)
    # bool 
    nysc_current                = models.BooleanField(default = False)
    nysc_ongoing                = models.BooleanField(default = False)
    nysc_authenticate           = models.IntegerField(default = 0)
    # nysc_attach                 = models.FileField(upload_to='confidentials')
    members_body                = models.CharField(max_length=200)
    membership_number           = models.CharField(max_length=100)
    membership_class            = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("Education")
        verbose_name_plural = ("Educations")

    def __str__(self):
        return str(self.full_name)

    def get_absolute_url(self):
        return reverse("Education_detail", kwargs={"pk": self.pk})


class FileUpload(models.Model):

    user_id                 = models.PositiveIntegerField()
    file1                    = models.FileField(upload_to="uploads/%Y/%m/%d") 
    file2                    = models.FileField(upload_to="uploads/%Y/%m/%d",blank=True,null=True) 
    file3                    = models.FileField(upload_to="uploads/%Y/%m/%d",blank=True,null=True) 
    uploaded_at             = models.DateTimeField(auto_now_add=True)   

    class Meta:
        verbose_name = ("FileUpload")
        verbose_name_plural = ("File Uploads")

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("file-upload_detail", kwargs={"pk": self.pk})
  