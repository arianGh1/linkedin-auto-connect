def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import os
try:
    import time
except:
    install("time")
    import time
try:
    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
except:
    install("selenium")
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
try:
    import warnings

except:
    install("warnings")
    import warnings
try:
    import subprocess
except:
    install("subprocess")
    import subprocess
try:
    import sys
except:
    install("sys") 
    import sys

os.system('cls')
warnings.filterwarnings("ignore", category=DeprecationWarning) 
def follow():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    login_email = input("Enter your login email or phone number:")
    password = input("Enter you password:")
    searching_text = input("In which category you like to add people:")
    url = "https://www.linkedin.com/checkpoint/lg/sign-in-another-account"

    try:
        driver = webdriver.Chrome("chromedriver.exe",chrome_options=options)
        driver.get(url)
    except:
        print("\nYour chromeriver.exe version is not same as your Chrome browser version.First check your chrome version then download matching chromedriver.exe from https://chromedriver.chromium.org/downloads .\n After downloaded chromedriver,inplace that in project directory")
        return

    #Enter email and password:
    #driver.get(url)
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='username']").send_keys(login_email)
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
    time.sleep(2)

    #Login:
    driver.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button").click()

    #Search the input text
    driver.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input').send_keys(searching_text)
    driver.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input').send_keys(Keys.ENTER)


    #Start following
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        buttons = driver.find_elements_by_class_name('artdeco-button__text')
        connect_or_follow = [button for button in buttons if (button.text=="Connect" or button.text =="Follow")]
        next = [button for button in buttons if button.text=="Next"]
        for button in connect_or_follow:

            driver.execute_script("arguments[0].click();", button)

            time.sleep(1)
            if button.text == "Connect":
                #'Send' and 'Add a note' buttons
                buttons2 = driver.find_elements_by_class_name('artdeco-button__text')

                #Click on send button
                for button2 in buttons2:
                    if button2.text == 'Send':
                        button2.click()

        #Go to the next page       
        for button in next:
            driver.execute_script("arguments[0].click();", button)
follow()