#coding=utf-8
# from callbacktest.ctx import ctx
from myflask.ctx import ctx

from m_login import Mylogin

def login_required():
    try:
        if ctx.ctx_stack.keys()[-1] is not None:
            return ctx.ctx_stack.values()[-1]
        else:
            Mylogin._get_user()
    except Exception as e:
        pass
    return "not user"

def login_user(user_id, username):
    ctx.ctx_stack.setdefault(user_id, username)
    # print loginuser
    # username = loginuser(username)
    # print result
