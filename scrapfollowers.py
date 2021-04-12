from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class ScrapFollowers:
    """
    path = path of the chrome webdriver
    """
    def __init__(self, path, username, password, target, number_followers):
        # PRIVATE
        self.__options = webdriver.ChromeOptions()
        self.__mobile_emulation = {
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/"
                         + "535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
        }
        self.__options.add_experimental_option("mobileEmulation", self.__mobile_emulation)
        self.__driver_path = path
        self.__driver = webdriver.Chrome(executable_path=self.__driver_path, options=self.__options)
        self.__username = username
        self.__password = password
        # PUBLIC
        self.target = target
        self.followers_list = []
        self.number_followers = number_followers

    """
    ==========================================
    = First rank methods =====================
    ==========================================
    """

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
        self.__driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/div/label/input').send_keys(
                                                                                                        self.__username)

        self.__driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[4]/div/label/input').send_keys(
                                                                                                        self.__password)
        sleep(1)
        self.__driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[6]/button').click()
        sleep(3)

    """
    private
    This method click on pop ups windowd to acces instagram
    1: click on "later" button
    2: click on "later" button
    """
    def __later(self):
        self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/section/div/button').click()
        sleep(7)
        self.__driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        sleep(2)

    """
    private
    This method search the username of the target on the research bar and click on his profile
    1: click on search button
    2: send the target username
    3: click on the profile of the target
    """
    def __search(self):
        self.__driver.find_element_by_css_selector(
            '#react-root > section > nav.NXc7H.f11OC > div > div > div.KGiwt > div > div > div:nth-child(2) > a > svg'
        ).click()
        sleep(2)
        self.__driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav[1]/div/header/div/h1/div/div/div/div[1]/label/input').send_keys(
            self.target)
        sleep(2)
        self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/ul/li[1]/a').click()

    """
    private
    This methhod click on the followers button of the target to load his followers
    !!! this method only work on public account or if you follow the private target's account
    1: click on the followers button
    """
    def __followers(self):
        self.__driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        ).click()
        sleep(2)

    """
    """
    def __load_followers(self):
        self.__driver.execute_script("window.scrollTo(0, 500)")

    """
    private
    This method get the followers of the target and append element by elements in the followers lists
    """
    def __get_followers(self):
        for i in range(self.number_followers + 1):
            self.followers_list.append(self.__driver.find_element_by_xpath(
                "/html/body/div[5]/div/div/div[2]/ul/div/li[" + str(i+1) + "]/div/div[2]/div[1]/div/div/span/a"
            ).text)

    """
    ==========================================
    = Second rank methods ====================
    ==========================================
    """

    """
        private
        this method use three others privates methods to complete the connexxion on instagram
        """
    def __access_instagram(self):
        self.__connect()
        self.__login()
        self.__later()

    """
    ==========================================
    = Third rank methods =====================
    ==========================================
    """

    """
    public
    main function of the class
    """
    def scrapfollowers(self):
        self.__access_instagram()
        self.__search()
        self.__followers()
        self.__load_followers()
        self.__get_followers()
