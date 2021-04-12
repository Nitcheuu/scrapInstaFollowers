from scrapfollowers import ScrapFollowers

sf = ScrapFollowers("webdriver/chromedriver.exe", "ph.favrellle", "filip2003", "quentin.1701t", 10)
sf.scrapfollowers()

for i in range(10):
    print(sf.followers_list[i])
