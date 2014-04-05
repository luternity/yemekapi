# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


# Create your models here.

class FoodCategoryManager(models.Manager):

    def active(self):
        return self.filter(active=True)


class FoodCategory(models.Model):

    name = models.CharField(_(u"İsim"), max_length=50, null=True, blank=True)
    description = models.CharField(_(u"Açıklama"), max_length=180, null=True, blank=True)
    category_type = models.CharField(_(u"Type"), max_length=30, null=True, blank=True)

    image =  models.ImageField(_("Resim"), upload_to="images/category/", null=True, blank=True)

    active = models.BooleanField(_(u"Aktif"), default=True)

    objects = FoodCategoryManager()

    class Meta:
        verbose_name = _(u"Yemek Kategorisi")
        verbose_name_plural = _(u"Yemek Kategorileri")

    def __unicode__(self):
        return "%s" % (self.name)

    def image_full_path(self):
        return self.image.url


class FoodManager(models.Manager):

    def active(self):
        return self.filter(active=True)


class Food(models.Model):

    name = models.CharField(_(u"İsim"), max_length=50, null=True, blank=True)
    description = models.CharField(_(u"Açıklama"), max_length=180, null=True, blank=True)

    foodcategory = models.ForeignKey(FoodCategory, verbose_name=_(u"Kategori"), null=True, blank=True)

    image =  models.ImageField(_("Resim"), upload_to="images/food/", null=True, blank=True)

    recipe_url = models.CharField(_(u"Tarif url'i"), max_length=200, null=True, blank=True)

    active = models.BooleanField(_(u"Aktif"), default=True)

    objects = FoodManager()

    class Meta:
        verbose_name = _(u"Yemek")
        verbose_name_plural = _(u"Yemekler")

    def __unicode__(self):
        return "%s" % (self.name)

    def image_full_path(self):
        return self.image.url
