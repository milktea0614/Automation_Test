# -*- coding: utf-8 -*-

import time

import appium.webdriver.appium_service
from appium import webdriver

from anroid_test.module.action_touch import *
from anroid_test.module.action_keycode import *
from anroid_test.module.action_additional import *

import urllib3.exceptions

LOGGER = Logger(log_name=__name__, stream_log_level=logging.DEBUG)

# Please input the device name of your android phone.
galaxy_s20_capabilites = {
    "platformName": 'Android',
    "platformVersion": "13",
    "automationName": 'uiautomator2',
    "deviceName": 'RFCN30RGR3N',
    "appPackage": 'com.android.settings',
    "appActivity": '.Settings',
    "isRealMobile": True
}

galaxy_tap_s6_lite_capabilities = {
    "platformName": 'Android',
    "platformVersion": "12",
    "automationName": 'uiautomator2',
    "deviceName": 'R54T3022FVH',
    "appPackage": 'com.android.settings',
    "appActivity": '.Settings',
    "isRealMobile": True
}


if __name__ == "__main__":
    """Run basic test."""
    try:
        _appium_service = appium.webdriver.appium_service.AppiumService()
        # https://appium.io/docs/en/2.0/cli/args/
        _appium_service.start(args=["--relaxed-security", "--log-timestamp"])
        LOGGER.info(f"Appium service start")
    except appium.webdriver.appium_service.AppiumServiceError as e:
        LOGGER.exception(e)
        exit()

    try:
        _driver = webdriver.Remote(r"http://localhost:4723", galaxy_s20_capabilites)
        LOGGER.info(f"{galaxy_s20_capabilites['deviceName']} is connected.")
    except urllib3.exceptions.MaxRetryError:
        LOGGER.warn(f"could not connect {galaxy_s20_capabilites['deviceName']}. Maybe, Appium service does not start normally.")
        exit()

    try:
        LOGGER.info("Go to Home using keycode.")
        _driver.press_keycode(3)
        time.sleep(1)

        swipe(_driver, times=3)

        LOGGER.info("[touch][element] 지도")
        touch(_driver, '//*[@content-desc="지도"]')
        time.sleep(3)
        LOGGER.info("[touch][position] 600, 400")
        touch(_driver, {"x": 600, "y": 400})
        time.sleep(3)

        LOGGER.info("[back] 뒤로가기")
        back(_driver)
        time.sleep(2)

        LOGGER.info("[double_touch][position] 7000, 700")
        double_touch(_driver, {"x": 700, "y": 700})
        time.sleep(2)

        LOGGER.info("[double_touch][element] 찾기")
        double_touch(_driver,"//android.widget.FrameLayout[contains(@resource-id, 'transportation_tab_strip_button') and @content-desc='찾기']")
        time.sleep(2)

        LOGGER.info("[back] 뒤로가기")
        back(_driver)

        LOGGER.info("[rotate] 시계 반향으로 80도씩 5번 회전")
        rotate(_driver, 80, times=5)
        time.sleep(2)
        LOGGER.info("[rotate] 반시계 반향으로 15도씩 5번 회전")
        rotate(_driver, 15, "counterclockwise", 5)
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

        LOGGER.info("[pinch_in] 축소 2회")
        pinch_in(_driver, 2)
        time.sleep(2)
        LOGGER.info("[pinch_out] 확대 2회")
        pinch_out(_driver,2)
        time.sleep(2)

        LOGGER.info("Go to Home using keycode.")
        _driver.press_keycode(3)

        LOGGER.info("[long_press][element] 지도")
        long_press(_driver, '//*[@content-desc="지도"]')
        time.sleep(2)
        LOGGER.info("[back] 뒤로가기")
        back(_driver)
        LOGGER.info("[long_press][position] 600, 800")
        long_press(_driver, {"x": 600, "y": 800})
        time.sleep(2)

        LOGGER.info("[back] 뒤로가기")
        back(_driver)
        time.sleep(2)

        # _driver.is_keyboard_shown()
    except Exception as e:
        LOGGER.error(e)
    finally:
        _driver.quit()
        LOGGER.info(f"{galaxy_s20_capabilites['deviceName']} is disconnected.")

        _appium_service.stop()
        LOGGER.info(f"Appium service stop")

