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
            print("search box found")
            break
        except Exception:
            print("search box not found", end='\r')
    search.clear()
    total = 0

    for _ in range(count//20 + 1):
        for i in range(cofg + 1):
            if i == 0:
                trg = target
            else:
                trg = f'{S_ID}_{i}_{target}'
            search.send_keys(trg)
            search.send_keys(Keys.ENTER)

            time.sleep(1)

            for k in range(20):
                driver.find_element_by_xpath(
                    '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
                driver.find_element_by_xpath(
                    '//*[@id="main"]/footer/div[1]/div[3]/button').click()
                print(f"sent {k + 1} messages", end="\r")
                total += 1

            print('total sent', total, 'messages')


def create_group():
    for i in range(cofg):
        while True:
            try:
                driver.find_element_by_xpath(
                    '//*[@id="side"]/header/div[2]/div/span/div[3]/div').click()
            except:
                continue
            try:
                driver.find_element_by_xpath(
                    '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div').click()
            except:
                continue
            try:
                driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input').send_keys(target)
            except:
                continue
            try:
                driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input').send_keys(Keys.ENTER)
            except:
                continue
            try:
                driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/span').click()
            except:
                continue
            try:
                driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]').send_keys(f'{S_ID}_{i+1}_{target}')
            except:
                continue
            try:
                driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/div/span').click()
                print('created', f'{S_ID}_{i+1}_{target}', 'group')
                break
            except:
                continue


def leave_group():
    while True:
        try:
            search = driver.find_element_by_xpath(
                '//*[@id="side"]/div[1]/div/label/div/div[2]'
            )
            print("search box found")
            break
        except Exception:
            print("search box not found", end='\r')
    search.clear()

    for i in range(1, cofg + 1):
        search.send_keys(f'{S_ID}_{i}_{target}')
        search.send_keys(Keys.ENTER)
        driver.find_element_by_xpath(
            '//*[@id="main"]/header/div[3]/div/div[3]/div').click()
        time.sleep(0.3)
        driver.find_element_by_xpath(
            '//*[@id="main"]/header/div[3]/div/div[3]/span/div/ul/li[5]/div').click()
        time.sleep(0.3)
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="main"]/header/div[3]/div/div[3]/div').click()
        time.sleep(0.3)
        driver.find_element_by_xpath(
            '//*[@id="main"]/header/div[3]/div/div[2]/span/div/ul/li[4]/div').click()
        time.sleep(0.3)
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]').click()
        print('deleted', f'{S_ID}_{i+1}_{target}', 'group')


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

    # path to the chromedriver
    driver = webdriver.Edge('D:/Projects/msedgedriver.exe')
    driver.maximize_window()
    driver.get("https://web.whatsapp.com")

    create_group()
    bomb()
    print('DO NOT CLOSE THE TAB')
    time.sleep(20)
    leave_group()

    time.sleep(2)
    driver.quit()
    print('bombed succesfully')
