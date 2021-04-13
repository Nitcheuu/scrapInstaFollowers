from scrapfollowers import ScrapFollowers

print("Enter the username of your account : ")
username = input()
print("Enter the password of your account : ")
password= input()
print("Enter the username of the target account : ")
target = input()
print("Enter the number of followers you want to scrap (1- 1000) : ")
number = int(input())


sf = ScrapFollowers("webdriver/chromedriver.exe", username, password, target, number, True)
sf.scrapfollowers()


