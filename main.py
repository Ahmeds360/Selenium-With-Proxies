from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import threading
import time


def read_proxy_list():
    with open('proxies.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def open_browser(url, proxy, delay):
    options = webdriver.ChromeOptions()
    options.headless = False
    options.add_argument("--window-size=400,400")
    options.add_argument(f"--proxy-server=http://{proxy}")
    driver = webdriver.Chrome(
        executable_path="./chromedriver.exe", options=options)
    driver.get(url)
    time.sleep(delay)
    driver.quit()


if __name__ == "__main__":
    DELAY = int(input("Enter delay: "))
    URL = input("Enter url: ")
    proxyList = read_proxy_list()

    if len(proxyList) == 0:
        input("No proxies found. Please add proxies to proxies.txt and press Enter.")
        proxyList = read_proxy_list()
    elif len(proxyList) != 0:

        for proxy in proxyList:
            thread = threading.Thread(
                target=open_browser, args=(URL, proxy, DELAY))
            thread.start()
