from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        response = self._create_user(email, password, **extra_fields)

        return response

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=30, blank=True, default="")
    last_name = models.CharField(max_length=100, blank=True, default="")
    phone = models.EmailField(blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(blank=False, default=False)
    delete_at = models.DateTimeField(null=True, default=None)




    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Url(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT, blank=True, null=True)
    long_url = models.CharField(max_length=255, blank=True, null=True)
    short_url = models.CharField(max_length=255, blank=True, null=True)

import pyshorteners
from tkinter import *
from tkinter import ttk, messagebox

def short():
    s = pyshorteners.Shortener()
    shor = beforeLink.get()
    afterLink.delete(0,END)
    afterLink.insert(0, s.tinyurl.short(shor))

root = Tk()
root.title('Сократитель ссылок')
root.geometry('400x150')
root.resizable(width=False, height=False)

beforeLinkLabel = Label(root, text ='Оставьте сылку')
beforeLinkLabel.place(x = 10 , y = 10)

beforeLink = ttk.Entry(root,width=40,font='Arial 13')
beforeLink.place(x = 10, y = 30)

btn =ttk.Button(root, text ='Сократить', command = short)
btn.place(relx=0.5, y =80, anchor = CENTER)

afterLinkLabel = Label(root, text ='Результат')
afterLinkLabel.place(x=10 , y = 105)

afterLink= ttk.Entry(root, width = 40, font='Arial 13')
afterLink.place(x = 10, y = 105)

root.mainloop()


