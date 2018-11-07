#coding=utf-8
from f_login import Mylogin

# ml1 = Mylogin()

user = {
    "1":"jack",
    "2":"bob"
}

@Mylogin.user_loader
def load_user(user_id="1"):
    # print user_id
    # print user
    return user[user_id]
    # return user.get(user_id,default="test")

# print load_user("2")
# load_user()
# print "#"*50
# try:
#     ml1.login_user("jack1")
# except Exception as e:
#     print e


