from class_69.CBT.common import Common
import time

class Login():
    def __init__(self):
        self.com = Common()
        self.dr = self.com.get_dr()
        self.dr.implicitly_wait(5)
    def login_user(self):
        return self.dr.find_element_by_id('username')
    def login_pwd(self):
        return self.dr.find_element_by_id('password')
    def login_click(self):
        return self.dr.find_element_by_id('login')

    def login_go(self,username,password):

        # for li in self.com.get_data(file):
            # print(li['username'])
        self.login_user().send_keys(username)
        self.login_pwd().send_keys(password)
        self.login_click().click()
        time.sleep(2)


if __name__ == '__main__':
    a = Login()
    # a.login_go('data.csv')