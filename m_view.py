#coding=utf-8
from m_login import Mylogin

ml = Mylogin()
ml1 = Mylogin()
@ml.user_load
def load_user(username):
    print "login {}".format(username)

load_user()

# ml.login_user("jack1")
# print "#"*50
# try:
#     ml1.login_user("jack1")
# except Exception as e:
#     print e


