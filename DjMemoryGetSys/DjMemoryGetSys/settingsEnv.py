# -*-coding:utf-8-*-
'''
    
'''
import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjMemoryGetSys.settings')

profile = os.environ.get('DjMemoryGetSys_PROFILE', 'develop')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjMemoryGetSys.settings.%s" % profile)
