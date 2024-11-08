from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the Chrome WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get('https://app-staging.qlub.cloud/qr/ae/qz-dummy-ch/5/_/_/cd460ea708')

# Maximize the browser window
driver.maximize_window()

# 1.Click on Pay now button

# Wait until the button is clickable, then click
try:
    # Set up the wait object for a max wait time of 10 seconds
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable(("xpath", "//span[text()='Pay now ']")))
    button.click()
except Exception as e:
    print("An error occurred:", e)

# Set an implicit wait of 10 seconds
driver.implicitly_wait(10)

# Scroll to the element
element = driver.find_element("xpath", "//span[normalize-space()='Split bill']")
driver.execute_script("arguments[0].scrollIntoView();", element)

# 2.Click on Split The Bill

# Wait until the button is clickable, then click
try:
    # Set up the wait object for a max wait time of 10 seconds
    wait = WebDriverWait(driver, 5)
    button = wait.until(EC.element_to_be_clickable(("xpath", "//span[normalize-space()='Split bill']")))
    button.click()
except Exception as e:
    print("An error occurred:", e)

# Wait for the bottom drawer to appear
try:
    # Set up the wait object for a max wait time of 10 seconds
    wait = WebDriverWait(driver, 5)
    drawer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "MuiPaper-root MuiPaper-elevation MuiPaper-elevation0 MuiDrawer-paper MuiDrawer-paperAnchorBottom mui-1qssk0k")))
except Exception as e:
    print("Bottom drawer did not appear:", e)

#3. Use pay a custom amount Split

try:
    # Set up the wait object for a max wait time of 10 seconds
    wait = WebDriverWait(driver, 5)
    drawer = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='SplitSelect_v2__Y4Cqz'])[3]")))
except Exception as e:
    print("Bottom drawer did not appear:", e)

