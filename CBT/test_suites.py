

from class_69.CBT.common import Common
from class_69.CBT.test_logn import Test_login
from class_69.CBT.test_notice import Testnotice

com = Common()

values = com.get_data('data.csv')
# sum = com.get_count("SELECT count(*) FROM `customer`")  #通过数据库获取数量
for value in values:
    username = value['username']
    password = value['password']
    verify = value['vrifyco']
    headline=value['headline']
    exp = value['exp']
    tl = Test_login()
    tl.test_login_success(username,password)
    tn = Testnotice()
    tn.test_notice(headline,exp)
