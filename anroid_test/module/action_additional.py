# -*- coding: utf-8 -*-
"""Additional action (e.g. Keyboard, back, shake, lock, rotate) of Interactions. ()"""

import logging

from appium.webdriver.common.appiumby import AppiumBy
from miraelogger import Logger

LOGGER = Logger(log_name=__name__, stream_log_level=logging.DEBUG)


def enter_text(driver, xpath, text, clear=True, hide=True):
    """Enter text.

    :param WebDriver driver: WebDriver obj.
    :param str xpath: Target element's xpath expression.
    :param str text: Target text.
    :param bool clear: Clear option before input the text.
    :param bool hide: Hide keyboard option after input the text.
    """
    _target = driver.find_element(by=AppiumBy.XPATH, value=xpath)
    if clear:
        _target.clear()

    _target.send_keys(text)

    if hide and driver.is_keyboard_shown():
        driver.hide_keyboard()


def back(driver) -> None:
    """Go back.

    :param WebDriver driver: WebDriver obj.
    """
    driver.back()


def shake(driver):
    """Shake device.

    :param WebDriver driver: WebDriver obj.
    """
    driver.shake()


def lock_screen(driver, seconds):
    """Lock screen.

    :param WebDriver driver: WebDriver obj.
    :param int seconds: The duration to lock the device, in seconds.
    """
    driver.lock(seconds)


def unlock_screen(driver):
    """Unlock screen.

    :param WebDriver driver: WebDriver obj.
    """
    driver.unlock()


