# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Image,Profile ,Comment

# Create your tests here.

class ProfileTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.anne= Profile(profile_photo = 'passion.jpeg', biography ='Passion')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.anne,Profile))

    def test_save_profile(self):
        self.james = Profile(profile_photo='travel.jpeg',biography='Travel')
        self.james.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
    
    def test_update_profile(self):
        self.ange = Profile(profile_photo='travel.jepg',biography='Awesome')
        self.ange.save_profile()
        cars =Profile.objects.filter(biography='Awesome').first()
        update= Profile.objects.filter(id=cars.id).update(biography='Journalist')
        updated = Profile.objects.filter(biography = 'Journalist').first()
        self.assertNotEqual(cars.biography , updated.biography)

    def test_delete_profile(self):
        self.fina = Profile(profile_photo='travel.jepg',biography='Awesome')
        self.fina.save_profile()
        nature = Profile.objects.filter(biography='Awesome').first()
        tree = Profile.objects.filter(id =nature.id).delete()
        trees =Profile.objects.all()
        


class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.passion= Image(image = 'passion.jpeg', name ='Passion', caption='Motivational')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.passion,Image))

    def test_save_image(self):
        self.travel = Image(image='travel.jpeg',name='Travel',caption='travel image')
        self.travel.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
    
    def test_update_image(self):
        self.bus = Image(image='travel.jepg',name='Prado',caption='Awesome')
        self.bus.save_image()
        cars =Image.objects.filter(name='Prado').first()
        update= Image.objects.filter(id=cars.id).update(name='Mercedes')
        updated = Image.objects.filter(name = 'Mercedes').first()
        self.assertNotEqual(cars.name , updated.name)

    def test_delete_image(self):
        self.forest = Image(image='travel.jepg',name='Virunga',caption='More attracive')
        self.forest.save_image()
        nature = Image.objects.filter(name='Virunga').first()
        tree = Image.objects.filter(id =nature.id).delete()
        trees =Image.objects.all()
        
