#coding=utf-8
# from callbacktest.ctx import ctx
from myflask.ctx import ctx

from m_login import Mylogin

def login_required():
    if Mylogin._get_user():
        return Mylogin._get_user()
    try:
        if ctx.ctx_stack.keys()[-1] is not None:
            return ctx.ctx_stack.values()[-1]
    except Exception as e:
        print e
        try:
            return Mylogin._get_user()
        except Exception as e:
            print e
    return "not user"

def login_user(user_id, username):
    ctx.ctx_stack.setdefault(user_id, username)
    ctx.ses_stack.setdefault("user_id",user_id)
    # print loginuser
    # username = loginuser(username)
    # print result
