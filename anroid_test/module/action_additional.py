# -*- coding: utf-8 -*-
"""Additional action (e.g. Keyboard, back, shake, lock, rotate) of Interactions.
(https://milktea0614.tistory.com/76)
"""

import logging

from appium.webdriver.common.appiumby import AppiumBy
from miraelogger import Logger

LOGGER = Logger(log_name=__name__, stream_log_level=logging.DEBUG)


# Keyboard
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


# Back
def back(driver) -> None:
    """Go back.

    :param WebDriver driver: WebDriver obj.
    """
    driver.back()


# HW actions
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
    if driver.is_locked:
        driver.unlock()


def authenticate_fingerprint(driver, finger_id):
    """Authenticate users by using their fingerprint scans on supported 'Android emulators'.

    :param WebDriver driver: WebDriver obj.
    :param int finger_id: Fingerprints stored in Android Keystore system (from 1 to 10)
    """
    driver.finger_print(finger_id)
