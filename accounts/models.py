from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from PIL import Image
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, phone_number,email,other_name,user_type, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            other_name = other_name,
            phone_number=phone_number,
            user_type = user_type
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    first_name          = models.CharField(max_length=50)
    last_name           = models.CharField(max_length=50)
    other_name           = models.CharField(max_length=50,blank=True,null=True)
    username            = models.CharField(max_length=50, unique=True)
    email               = models.EmailField(max_length=100, unique=True)
    phone_number        = models.CharField(max_length=50)

    # required
    date_joined         = models.DateTimeField(auto_now_add=True)
    last_login          = models.DateTimeField(auto_now_add=True)
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=False)
    is_superadmin       = models.BooleanField(default=False)
    user_type_choices   = ((1,'is_employee'),
                            (2,'is_admin'),
                            (3,'is_auditor'),
                            (4,'is_accountant'),
                            (5,'is_director')
                            
                            )
    user_type           = models.PositiveSmallIntegerField(choices = user_type_choices,default=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

#custom user review name
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    
    
    

# For otp codes authentications 

import random

class OtpCode(models.Model):
    otp             = models.CharField(max_length=6,)
    user            = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.otp)

    # modifying the default save method 

    def save(self, *args,**kwargs):
        otp_list = [x for x in range(10)]
        code_items = []

        for i in range(6):
            num = random.choice(otp_list)
            code_items.append(num)

        code_string = "".join(str(item) for item in code_items)    
        self.otp = code_string
        super().save(*args,**kwargs)       
        
# # Profile models for different user types 


class Profile(models.Model):
    user                = models.OneToOneField(User,on_delete=models.DO_NOTHING,blank=True,null=True)
    
    image               = models.FileField(default='avatar.png',upload_to = "media/")                        
    
    
    date_created        = models.DateTimeField(auto_now_add=True)
    date_updated        = models.DateTimeField()

    # removing contact address
    @property
    def email(self):
        return "%s"%(self.user.email)


    @property
    def full_name(self):
        return "%s"%f'{self.user.first_name} {self.user.last_name}'


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    # def save(self,*args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    