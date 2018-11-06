#coding=utf-8

def login_required():
    if user is not None:
        return user
    return "not user"

def login_user(username, password=None):
    loginuser = self.callback
    # print loginuser
    username = loginuser(username)
    # print result
