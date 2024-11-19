from seleniumwire import webdriver
import pickle


def save_cookies(driver, filepath):
    """Save cookies to a file."""
    with open(filepath, 'wb') as file:
        pickle.dump(driver.get_cookies(), file)


def load_cookies(driver, filepath):
    """Load cookies from a file into the driver"""
    with open(filepath, 'rb') as cookies_file:
        cookies = pickle.load(cookies_file)

        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            driver.add_cookie(cookie)


driver = webdriver.Chrome()
driver.get('https://www.facebook.com/klausiohannis')

input("Log in manually, then press enter into the console...")

save_cookies(driver, 'facebook_cookies.pkl')

driver.quit()



