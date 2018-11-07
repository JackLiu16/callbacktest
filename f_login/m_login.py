#coding=utf-8
from myflask.ctx import ctx

class Mylogin(object):

    def __init__(self):
        self.user_callback = None
        # self.user = None

    def user_loader(self, callback):
        self.user_callback = callback
        return callback
 
    def reload_user(self):
        user_id = ctx.ses_stack.keys()[-1]
        user = self.user_callback(user_id)
        ctx.ctx_stack.setdefault(user)
        return user

    def _get_user(self):
        reload_user()

