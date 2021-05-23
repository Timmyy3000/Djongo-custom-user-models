from typing_extensions import TypeGuard
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# BAse user manage

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_staff = False, is_admin = False, is_active = True):
        if not email or not username:
            raise ValueError("User must have email and username")
        
        if not password:
            raise ValueError("User must have password")

        user_obj = self.model(
            email = self.normalize_email(email), #normalize email
            username = username
            
        )

        user_obj.set_password(password) # set password
        user_obj.staff = is_staff # is vendor 
        user_obj.admin = is_admin# is admin 
        user_obj.active = is_active # is active 
        user_obj.save(using=self._db)

        return user_obj

    def create_vendor (self, email, username, password=None):

        vendor_obj = self.create_user(
            email,  username, password=password, is_staff=True
        )
       

        return vendor_obj
    
    def create_superuser (self, email, username, password=None):

        admin_obj = self.create_user(
              email,  username, password=password, is_admin=True, is_staff=True
        )
       

        return admin_obj

class User(AbstractBaseUser) :

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=150, unique=True)
    active = models.BooleanField(default=True) # can logged_in
    staff = models.BooleanField(default=False) # is vendor 
    admin = models.BooleanField(default=False) #superuser
    startdate = models.DateTimeField(default=timezone.now)
    
     
    USERNAME_FIELD = 'username' # username field 

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=CASCADE)

    # full_name = models.CharField(default ="",max_length=150) # full name
    # last_name = models.CharField(max_length=150)
    # start_date = models.DateTimeField(default=timezone.now)
    # bank = models.CharField(max_length=150)
    # account_number = models.CharField(max_length=50)
    # phone_number = models.CharField(max_length=50)
    # subscription = models.IntegerField(max_length=5 , default=None)
    # balance = models.IntegerField(max_length=20)
    # referal_balance = models.IntegerField(max_length=20)
    # user_referal_id = models.CharField(max_length=150)
    # user_referred = models.CharField(max_length=150)
   
    # awaiting_withdrawal = models.BooleanField(default=False)
    # day_count = models.IntegerField(max_length=10)
