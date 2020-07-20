from class_69.CBT.common import Common
from class_69.CBT.do_login import Login
class Test_login():
    def __init__(self):
        self.com =Common()
    def test_login(self):
        lists = self.com.get_data('data.csv')
        for li in lists:
            login =Login()
            login.login_go(li['username'],li['password'])
            self.com.asert_login()

    def test_login_fil(self):
        lists = self.com.get_data('data_file.csv')
        for li in lists:
            login =Login()
            login.login_go(li['username'],li['password'])
            self.com.asert_logfil()

    def test_login_success(self,username,password):

        lg = Login()
        lg.login_go(username,password)
        self.com.asert_login()