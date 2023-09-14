# -*- coding: utf-8 -*-
"""
Keycode of Interactions. ()
Refer to https://developer.android.com/reference/android/view/KeyEvent#constants_1
"""

import logging
from miraelogger import Logger

LOGGER = Logger(log_name=__name__, stream_log_level=logging.DEBUG)


def go_to_back(driver):
    """Go back screen using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(4)


def go_to_home(driver):
    """Go home screen using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(3)


def go_to_app_history(driver):
    """Go to App history screen using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(187)


def go_to_call(driver):
    """Go to Call screen using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(5)


def end_call(driver):
    """End Call screen using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(6)


def go_to_camera(driver):
    """Go to Camera screen using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(27)


def go_to_contacts(driver):
    """Go to Contacts screen using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(207)


def go_to_music(driver):
    """Go to Music(e.g. YouTube Music) screen using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(209)


def volume_mute(driver):
    """Set volume to mute using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(164)


def volume_up(driver):
    """Set volume up using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(24)


def volume_down(driver):
    """Set volume down using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(25)


def open_notification(driver):
    """Open notification using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(83)


def control_powerkey(driver, mode="sleep"):
    """Control the powerkey using keycode.

    :param WebDriver driver: WebDriver obj.
    :param str mode: Target mode (sleep, on, off)
    """
    if mode == "sleep":
        driver.press_keycode(223)
    elif mode == "on":
        LOGGER.warn("If the previous state was the power off, it may not work as you want.")
        driver.press_keycode(224)
    elif mode == "off":
        LOGGER.warn("You can see the power options. Be careful when using it.")
        driver.long_press_keycode(26)


def go_to_settings(driver):
    """Go to Settings screen using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(176)


def open_voice_assist(driver):
    """Open the voice assist(e.g. Bixby) using keycode.

    :param WebDriver driver: WebDriver obj.
    """
    driver.press_keycode(231)
