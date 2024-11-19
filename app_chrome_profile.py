from seleniumwire import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/path_to_chrome_profile_already_logged_on_facebook_account")

driver = webdriver.Chrome(options=options)
driver.get('https://www.facebook.com/klausiohannis')
