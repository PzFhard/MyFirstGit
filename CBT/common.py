from selenium import webdriver
import csv,pymysql
from pymysql.cursors import DictCursor

class Common():
    # @classmethod
    # def get_dr(cls):
    #     cls.dr = webdriver.Chrome()
    #     cls.dr.get('http://192.168.13.128:8081/agileone/')
    #     return cls.dr


    def get_data(self,file):
        with open(file,mode='r+',encoding='utf-8') as f:
            dicred = csv.DictReader(f)
            lis = []
            for i in dicred:
                lis.append(dict(i))
        return lis

    def asert_login(self):
        a = self.dr.find_element_by_link_text('注销').is_displayed()
        if a == True:
            print('ok')
        else:
            print('NO')

    def asert_logfil(self):
        a = self.dr.find_element_by_xpath('//*[@id="msg"]').text
        if a == '出错啦: 密码输入错误 ...':
            print('错误密码登陆 测试成功')

        elif self.dr.find_element_by_link_text('注销').is_displayed():
            print('错误密码登陆 测试失败')

    def asert_text_equa(self,element,exp):
        mation = self.dr.find_element_by_xpath(element).text
        if exp in mation:
            print('E_test_suites ok')
            return True
        else:
            print('E_test_suites ko')
            return False

    def get_db(self, sql):
        cone = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='woniuboss',
                               charset='utf8')
        cus = cone.cursor(cursor=DictCursor)
        sql = sql
        cus.execute(sql)
        res = cus.fetchall()  # 返回列表
        return res[0]['customer_id']
if __name__ == '__main__':
    c = Common()