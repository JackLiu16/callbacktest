#coding=utf-8
from f_login import Mylogin

ml = Mylogin()
# ml1 = Mylogin()

user = {
    "1":"jack",
    "2":"bob"
}

@ml.user_loader
def load_user(user_id):
    return "login {}".format(user.get(user_id,"test"))

# load_user()
# print "#"*50
# try:
#     ml1.login_user("jack1")
# except Exception as e:
#     print e


