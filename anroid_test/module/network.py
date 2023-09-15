# -*- coding: utf-8 -*-
"""Related on the Network function.
()
"""
import logging

from miraelogger import Logger

LOGGER = Logger(log_name=__name__, stream_log_level=logging.DEBUG)


# Network (appium/webdriver/extensions/android/network.py)
def get_network_type(driver):
    """Return current network type.

    :param WebDriver driver: WebDriver obj.
    :return: Network type.
    :rtype: int.
    """
    # WIFI = 0b010, DATA = 0b100, AIRPLANE_MODE = 0b001
    return driver.network_connection


def set_network_connection(driver, network_type="all"):
    """Sets the network connection type. Android only.
    
    :param WebDriver driver: WebDriver obj.
    :param str network_type: Target Network type string (all, data, wifi, airplane, none)
    """
    if network_type.lower() == "none":
        driver.set_network_connection(0)
    elif network_type.lower() == "airplane":
        driver.set_network_connection(1)
    elif network_type.lower() == "wifi":
        driver.set_network_connection(2)
    elif network_type.lower() == "data":
        driver.set_network_connection(4)
    elif network_type.lower() == "all":
        driver.set_network_connection(6)


def set_network_speed(driver, network_speed_type="full"):
    """Set the network speed emulation. Android Emulator only.

    :param WebDriver driver: WebDriver obj.
    :param str network_speed_type: Target Network speed (gsm, scsd, gprs, edge, umts, hsdpa,lte, evdo, full)
    """
    driver.set_network_speed(network_speed_type.lower())


# SMS (appium/webdriver/extensions/android/sms.py)
def send_sms(driver, to_number, msg):
    """Emulate send SMS event on the connected emulator. Android only.

    :param WebDriver driver: WebDriver obj.
    :param str to_number: Phone number to send.
    :param str msg: SMS message.
    """
    driver.send_sms(to_number, msg)


# GSM (appium/webdriver/extensions/android/gsm.py)
def gsm_call(driver, to_number, action="call"):
    """Make GSM(Global System for Mobile Communications) call. Android Emulator only.

    :param WebDriver driver: WebDriver obj.
    :param str to_number: Phone number to call.
    :param str action: Call action option (call, accept, cancel, hold)
    """
    driver.make_gsm_call(to_number, action.lower())


def gsm_set_siginal(driver, strength="great"):
    """Set GSM signal strength. Android Emulator only.

    :param WebDriver driver: WebDriver obj.
    :param str strength: GSM Signal strength option (none, poor, moderate, good, great)
    """
    if strength.lower() == "none":
        driver.set_gsm_signal(0)
    elif strength.lower() == "poor":
        driver.set_gsm_signal(1)
    elif strength.lower() == "moderate":
        driver.set_gsm_signal(2)
    elif strength.lower() == "good":
        driver.set_gsm_signal(3)
    elif strength.lower() == "great":
        driver.set_gsm_signal(4)


def gsm_set_voice(driver, state="home"):
    """Set GSM voice state. Android Emulator only.

    :param WebDriver driver: WebDriver obj.
    :param str state: State of GSM voice (unregistered, home, roaming, searching, denied, off, on)
    """
    driver.set_gsm_voice(state.lower())
