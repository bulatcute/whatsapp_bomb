from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
)
import time


def bomb():
    search = None
    target = input('Enter target:\n> ')
    count = input('Enter count of messages:\n> ')
    message = input('Enter message:\n> ')
    if target == "":
        print('target exc')
        return None

    try:
        count = int(count)
    except:
        print('count exc')
        return None

    if message == "":
        print('message exc')
        return None

    driver = webdriver.Chrome('chromedriver.exe') # path to the chromedriver
    driver.maximize_window()
    driver.get("https://web.whatsapp.com")
    while True:
        try:
            search = driver.find_element_by_xpath(
                "/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/label[1]/input[1]"
            )
            print("search box found")
            break
        except Exception:
            print("search box not found")
    search.clear()
    search.send_keys(target)
    i = 0
    while True:
        try:
            if i == 15:
                break
            user = driver.find_element_by_xpath(
                '//span[@title = "{}"]'.format(target)
            )
            i += 1
            user.click()
            break
        except:
            continue
    time.sleep(2)
    msg_box = driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[2]/div[1]/div[2]"
    )

    for i in range(count):
        msg_box.send_keys(message.replace("\n", Keys.SHIFT + Keys.ENTER))
        msg_box.send_keys(Keys.ENTER)
        print(f"sent {i + 1} messages", end="\r")
    
    time.sleep(2)
    driver.quit()
    print('bombed succesfully')
    pass


if __name__ == "__main__":
    import sys

    bomb()

    sys.exit()