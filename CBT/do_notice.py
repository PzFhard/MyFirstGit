from class_69.CBT.common import Common

class Donotice():
    def __init__(self):
        self.com = Common()
        self.dr = self.com.dr
    def get_notice(self):
        return self.dr.find_element_by_partial_link_text('')

    def get_headline(self):
        return self.dr.find_element_by_id('headline')

    def get_add(self):
        return self.dr.find_element_by_id('add')

    def do_notice(self,headline):

        self.get_notice().click()
        self.get_headline().send_keys(headline)
        self.get_add().click()
