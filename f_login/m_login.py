#coding=utf-8
import os
from functools import wraps

class Mylogin(object):

    def __init__(self):
        self.user_callback = None
        # self.user = None

    def user_loader(self, callback):
            self.user_callback = callback
        return callback
 
    def reload_user(self, user_id):
        user = self.user_callback(user_id)
        return user
