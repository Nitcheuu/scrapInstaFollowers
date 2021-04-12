from selenium import webdriver
from time import sleep


class ScrapFollowers:
    """
    path = path of the chrome webdriver
    """
    def __init__(self, path, username, password):

        self.__driver_path = path
        self.__driver = webdriver.Chrome(executable_path=self.__driver_path)
        self.__username = username
        self.__password = password

    """
    private
    open the instagram login page using chrome webdriver
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

    """
    public
    main function of the class
    """
    def scrapfollowers(self):
        self.__connect()
        self.__login()


