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
