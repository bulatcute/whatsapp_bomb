from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
)
import time
import random


def bomb():
    while True:
        try:
            search = driver.find_element_by_xpath(
                '//*[@id="side"]/div[1]/div/label/div/div[2]'
            )
            print("search box found", end='\r')
            break
        except Exception:
            print("search box not found")
    search.clear()

    for _ in range(count//20 + 1):
        for i in range(cofg + 1):
            if i == 0:
                trg = target
            else:
                trg = f'{i}_{target}_{S_ID}'
            search.send_keys(trg)
            k = 0
            while True:
                try:
                    if k == 15:
                        break
                    user = driver.find_element_by_xpath(
                        '//span[@title = "{}"]'.format(trg)
                    )
                    k += 1
                    user.click()
                    break
                except:
                    continue
            time.sleep(2)
            msg_box = driver.find_element_by_xpath(
                "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[2]/div[1]/div[2]"
            )

            for k in range(20):
                msg_box.send_keys(message.replace("\n", Keys.SHIFT + Keys.ENTER))
                msg_box.send_keys(Keys.ENTER)
                print(f"sent {k + 1} messages", end="\r")
    

def create_group():
    for i in range(cofg):
        while True:
            try:
                driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div').click()
                break
            except:
                continue
        driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input').send_keys(target)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input').send_keys(Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/span').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]').send_keys(f'{i + 1}_{target}_{S_ID}')
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/div/span').click()


if __name__ == "__main__":
    S_ID = random.randint(0, 100000)
    search = None
    target = input('Enter target:\n> ')
    count = input('Enter count of messages:\n> ')
    cofg = input('Enter count of groups:\n> ')
    message = input('Enter message:\n> ')
    if target == "":
        print('target exc')
        exit(0)

    try:
        count = int(count)
    except:
        print('count exc')
        exit(0)

    try:
        cofg = int(cofg)
    except:
        print('count of groups exc')
        exit(0)

    if message == "":
        print('message exc')
        exit(0)
    
    driver = webdriver.Edge('D:/Projects/msedgedriver.exe') # path to the chromedriver
    driver.maximize_window()
    driver.get("https://web.whatsapp.com")

    create_group()
    bomb()
    
    time.sleep(2)
    driver.quit()
    print('bombed succesfully')
