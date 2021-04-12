from selenium import webdriver
from time import sleep


class ScrapFollowers:
    """
    path = path of the chrome webdriver
    """
    def __init__(self, path, username, password, target):
        self.__driver_path = path
        self.__driver = webdriver.Chrome(executable_path=self.__driver_path)
        self.__username = username
        self.__password = password
        self.target = target

    """
    private
    1: open the instagram login page using chrome webdriver
    """
    def __connect(self):
        self.__driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        sleep(2)

    """
    private
    This method fill up the login form, she find element with the xpath of css
    1: accept cookies
    2: send username
    3: send password
    4: click on the connect button
    """
    def __login(self):
        self.__driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
        sleep(1)
        self.__driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[1]/div/label/input").send_keys(
                                                                                                        self.__username)
        self.__driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[2]/div/label/input").send_keys(
                                                                                                        self.__password)
        sleep(1)
        self.__driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(3)

    """
    private
    This method click on pop ups windowd to acces instagram
    1: click on "later" button
    2: click on "later" button
    """
    def __later(self):
        self.__driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(2)
        self.__driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        sleep(2)

    """
    private
    This method search the username of the target on the research bar and click on his profile
    1: send the target username
    2: click on the profile of the target
    """
    def __search(self):
        self.__driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(
            self.target
        )
        sleep(2)
        self.__driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a").click()

    """
    private
    this method use three others privates methods to complete the connexxion on instagram
    """
    def __access_instagram(self):
        self.__connect()
        self.__login()
        self.__later()



    """
    public
    main function of the class
    """
    def scrapfollowers(self):
        self.__access_instagram()
        self.__search()


