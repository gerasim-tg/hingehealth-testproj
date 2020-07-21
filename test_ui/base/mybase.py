import os
from selenium import webdriver

class MyBase:

    def __init__(self, driver="chrome"):
        if driver == "chrome":
            chromedriver = "/usr/local/bin/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.driver = webdriver.Chrome(chromedriver)

    def open_page(self, url):
        # driver.get("http://skyscanner.com")
        self.driver.get(url)

    def close_all(self):
        self.driver.quit()

#
# if __name__ == '__main__':
#     base = MyBase()
#     base.open_page("http://localhost:3000")
#     base.close_all()