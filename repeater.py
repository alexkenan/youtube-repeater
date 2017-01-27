"""
Infinite youtube repeater script
"""
import os
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def startup() -> webdriver:
    """
    Startup a selenium webdriver with uBlock installed
    :return: Selenium webdriver with uBlock Origin installed and ready to go
    """
    chrome_options = Options()
    ext_dir = r'/Users/Alex/Library/Application Support/' \
              'Google/Chrome/Default/Extensions/cjpalhdlnbpafiamejdnhcphjbkeiagm/'
    ext1 = ''
    for item in os.listdir(ext_dir):
        try:
            ext1 = re.compile(r'\d.(\d)+.(\d)+_(\d)+').search(item).group()
        except:
            pass
    ext = '{}{}'.format(ext_dir, ext1)
    chrome_options.add_argument('load-extension={}'.format(ext))
    driver = webdriver.Chrome('/Users/Alex/Documents/Python/dailies/chromedriver1',
                              chrome_options=chrome_options)
    driver.create_options()
    driver.set_window_position(0, 0)
    driver.set_window_size(10, 10)
    return driver


def youtube(url: str, driver: webdriver) -> None:
    """
    Run the YouTube URL forever
    :param url: Website URL
    :param driver: Selenium Webdriver
    :return: None (infinite loop)
    """
    count = 1
    try:
        driver.get(url)
        while True:
            status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")

            if status == 0:
                count += 1
                driver.refresh()
            else:
                sleep(1)

    except KeyboardInterrupt:
        if count == 1:
            toprint = ''
        else:
            toprint = 's'
        print('Song played {} time{}!'.format(count, toprint))
        driver.quit()


def main() -> None:
    """
    Main program
    :return: None
    """
    link = input('YouTube link: ')
    wdriver = startup()
    youtube(link, wdriver)


if __name__ == '__main__':
    main()
