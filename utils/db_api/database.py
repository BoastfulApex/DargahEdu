import datetime
from typing import List, Any
from asgiref.sync import sync_to_async
from backend.models import *

@sync_to_async
def add_user(user_id, lang):
    try:
        user, created = User.objects.get_or_create(user_id=user_id)
        user.lang = lang

        user.save()
        return user
    except Exception as exx:
        print(exx)
        return None
    

@sync_to_async
def get_user(user_id):
    try:
        user = User.objects.filter(user_id=user_id).first()
        return user    
    except:
        return None


@sync_to_async
def get_lang(user_id):
    try:
        user = User.objects.filter(user_id=user_id).first()
        return user.lang
    except Exception as exx:
        print(exx)
        return None


@sync_to_async 
def get_cource_by_name(name):
    try:
        cources = Cource.objects.all()
        for i in cources:
            if i.name_lat == name or i.name_kril == name:
                return i
        return None
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_cource(id):
    try:
        cource = Cource.objects.filter(id=id).first()
        return cource    
    except:
        return None

