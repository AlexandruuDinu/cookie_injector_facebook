# Facebook Cookies Manager

This script demonstrates how to save and load cookies for a web browser using Selenium and the Selenium Wire library. It allows users to manually log in to a Facebook page, save the authentication cookies, and reuse them later without needing to log in again.

## Features

- Save browser cookies after logging into a website.
- Load cookies into the browser to restore session state.
- Uses Selenium and Selenium Wire for enhanced browser interaction.

## Prerequisites

1. **Python**: Ensure Python 3.7 or higher is installed on your system.
2. **Google Chrome**: Install Google Chrome for the WebDriver.
3. **ChromeDriver**: Download and install the compatible version of ChromeDriver for your Chrome browser.
4. **Libraries**:
   - Selenium
   - Selenium Wire
   - Pickle (built-in Python library)

Install Selenium and Selenium Wire using pip:

```bash
pip install selenium selenium-wire
```

## How to use

1. Clone or download this repository.
2. Ensure all required Python libraries are installed using the command above.
3. Place the chromedriver executable in your system's PATH or in the same directory as the script.
4. Run the script using the following command:

```bash
python script_name.py
```

## Saving cookies

1. The script will open a Chrome browser and navigate to the specified Facebook page.
2. Manually log in to Facebook.
3. Once logged in, return to the console and press Enter to save the cookies.

Cookies will be saved to a file named facebook_cookies.pkl.

## Loading cookies

To use the saved cookies in a different session:

1. Modify the script to include the load_cookies(driver, 'facebook_cookies.pkl') function before navigating to the Facebook page.
2. Run the script, and the session will load with the saved cookies.

## Functions 

```save_cookies(driver, filepath)```
- Saves the cookies from the browser session to a file.

```load_cookies(driver, filepath)```
- Loads cookies from a file into the browser session.


## Important

- **Privacy**: The saved cookies file may contain sensitive authentication tokens. Keep the file secure and avoid sharing it.
- **Expiry**: Cookies may expire over time, requiring re-login and cookie saving.
- **Compatibility**: Ensure the same version of the browser and WebDriver is used for saving and loading cookies.









