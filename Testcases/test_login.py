# We can Write test cases in this package and try for Automating  the testcases.
# Each testcase we have to create seperate python file and write the code and automate.


from PageObjects.LoginPage import Loginpage
from Utilities.readProperties import readConfig

class Test_001_Login:
    baseUrl = readConfig.getApplicationUrl()
    useremail = readConfig.getUserEmail()
    password = readConfig.getUserPassword()

    def test_homepage(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_tittle = self.driver.title
        if act_tittle == "Your store. Login":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage.png")
            self.driver.close()

            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp=Loginpage(self.driver)
        self.lp.setuserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        exp_title = "Dashboard / nopCommerce administration"

        if act_title == exp_title:
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            self.driver.close()
            assert False