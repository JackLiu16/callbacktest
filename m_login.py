#coding=utf-8
import os
from functools import wraps
class Mylogin(object):
    def __init__(self):
        self.callback = None

    def user_load(self, func):
        @wraps(func)
        def inner_load(*args,**kwargs):
            # print func
            self.callback = func
            return func
        return inner_load
    
    def login_user(self, username, password=None):
        loginuser = self.callback
        # print loginuser
        loginuser(username)

