# -*- coding: utf-8 -*-

import logging

from miraelogger import Logger
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

import urllib3.exceptions
import selenium.common.exceptions

LOGGER = Logger(log_name=__name__, stream_log_level=logging.DEBUG)

# Please input the device name of your android phone.
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='R54T3022FVH',
    appPackage='com.android.settings',
    appActivity='.Settings'
)


if __name__ == "__main__":
    """Run basic test."""
    try:
        _driver = webdriver.Remote(r"http://localhost:4723", capabilities)
    except urllib3.exceptions.MaxRetryError:
        LOGGER.warn(f"could not connect {capabilities['deviceName']}. Please run the appium server before run it.")
        exit()

    LOGGER.info(f"{capabilities['deviceName']} is connected.")

    try:
        _driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        LOGGER.info("find the text is Battery.")
    except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.NoSuchElementException):
        LOGGER.warn("could not find the text is Battery.")

    try:
        _driver.find_element(by=AppiumBy.XPATH, value='//*[@text="연결"][@resource-id="android:id/title"]')
        LOGGER.info("find the text is 연결.")
    except selenium.common.exceptions.NoSuchElementException:
        LOGGER.warn("could not find the text is 연결.")

    _driver.quit()
    LOGGER.info(f"{capabilities['deviceName']} is disconnected.")

