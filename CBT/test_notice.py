from class_69.CBT.do_notice import Donotice
from class_69.CBT.common import Common

class Testnotice():
    def __init__(self):
        self.donoti = Donotice()
        self.com = Common()
    def test_notice(self,headline,exp):
        self.donoti.do_notice(headline)
        self.com.asert_text_equa('msg',exp)