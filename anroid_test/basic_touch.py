# -*- coding: utf-8 -*-

import datetime
import time

import appium.webdriver.appium_service
from appium import webdriver

from action_touch import *

import urllib3.exceptions

LOGGER = Logger(log_name=__name__, stream_log_level=logging.DEBUG)

# Please input the device name of your android phone.
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='R54T3022FVH',
    appPackage='com.android.settings',
    appActivity='.Settings',
)


def save_dump(driver):
    """Save dump file.

    :param WebDriver driver: WebDriver.
    """
    _save_time = str(datetime.datetime.now().timestamp())
    _page = driver.page_source
    with open(f"ui_dump/{_save_time}.xml", 'w', encoding='utf-8') as f:
        f.write(_page)

    driver.save_screenshot(f"ui_dump/{_save_time}.png")


if __name__ == "__main__":
    """Run basic test."""
    _appium_service = appium.webdriver.appium_service.AppiumService()
    _appium_service.start()
    LOGGER.info(f"Appium service start")

    try:
        _driver = webdriver.Remote(r"http://localhost:4723", capabilities)
    except urllib3.exceptions.MaxRetryError:
        LOGGER.warn(f"could not connect {capabilities['deviceName']}. Maybe, Appium service does not start normally.")
        exit()

    LOGGER.info(f"{capabilities['deviceName']} is connected.")

    LOGGER.info("Go to Home using keycode.")
    _driver.press_keycode(3)

    LOGGER.info("[touch_element] 지도")
    touch_element(_driver, '//*[@content-desc="지도"]')
    time.sleep(3)

    LOGGER.info("[rotate] 시계 반향으로 80도씩 5번 회전")
    rotate(_driver, 80, times=5)
    time.sleep(2)
    LOGGER.info("[rotate] 반시계 반향으로 5도씩 5번 회전")
    rotate(_driver, 5, "counterclockwise", 5)
    time.sleep(2)

    LOGGER.info("[scroll] 위로 스크롤 4회")
    scroll(_driver, times=4)
    time.sleep(2)
    LOGGER.info("[scroll] 아래로 스크롤 4회")
    scroll(_driver, "down", 4)
    time.sleep(2)

    LOGGER.info("[swipe] 오른쪽으로 스와이프 3회")
    swipe(_driver, times=3)
    time.sleep(2)
    LOGGER.info("[swipe] 왼쪽으로 스와이프 3회")
    swipe(_driver, "left", 3)
    time.sleep(2)

    LOGGER.info("[pinch_in] 확대 2회")
    pinch_in(_driver, 2)
    time.sleep(2)
    LOGGER.info("[pinch_out] 축소 2회")
    pinch_out(_driver,2)
    time.sleep(2)

    LOGGER.info("[back] 뒤로가기")
    back(_driver)
    time.sleep(2)

    # _driver.is_keyboard_shown()

    _driver.quit()
    LOGGER.info(f"{capabilities['deviceName']} is disconnected.")

    _appium_service.stop()
    LOGGER.info(f"Appium service stop")

