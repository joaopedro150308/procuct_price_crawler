from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait

def iniciar_driver():
    chrome_options = ChromeOptions()

    arguments = ['--lang=pt-BR', '--incognito', '--window-size=(800,600)']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(chrome_options)

    wait = WebDriverWait(
        driver,
        30,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )

    return driver, wait