# -*- coding: utf-8 -*-
"""Touch of Interactions. (https://milktea0614.tistory.com/74)"""

import logging
import math
from typing import Union

from miraelogger import Logger
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

import selenium.common.exceptions


LOGGER = Logger(log_name=__name__, stream_log_level=logging.DEBUG)


def touch(driver, xpath: Union[str, dict], timeout=1.0) -> None:
    """Touch an element or position in current screen.

    :param WebDriver driver: WebDriver obj.
    :param Union[str, dict] xpath: Target element's xpath expression or Target position dictionary {"x": x, "y": y}.
    :param float timeout: Waiting the timeout value to find element.
    """
    if isinstance(xpath, str):
        driver.implicitly_wait(timeout)
        try:
            _target = driver.find_element(by=AppiumBy.XPATH, value=xpath)
            TouchAction(driver).tap(_target).perform()
            LOGGER.debug(f"Touch the '{xpath}' is success.")
        except (selenium.common.exceptions.NoSuchElementException, RuntimeError) as e1:
            LOGGER.exception(msg := f"Touch the '{xpath}' is failed")
            raise e1(msg)
        except TimeoutError:
            LOGGER.exception(msg := f"Could not find the '{xpath}' within {timeout} sec.")
            raise TimeoutError(msg)
    elif isinstance(xpath, dict):
        try:
            TouchAction(driver).tap(x=xpath['x'], y=xpath['y']).perform()
            LOGGER.debug(f"Touch the '({xpath})' is success.")
        except Exception:
            LOGGER.exception(msg := f"Touch the '({xpath})' is failed.")
            raise Exception(msg)
    else:
        LOGGER.exception(msg := "Please check xpath parameter type is string or dict.")
        raise Exception(msg)


def double_touch(driver, xpath: Union[str, dict], timeout=1.0) -> None:
    """Double tap an element in current screen.

    :param WebDriver driver: WebDriver obj.
    :param Union[str, dict] xpath: Target element's xpath expression or Target position dictionary {"x": x, "y": y}.
    :param float timeout: Waiting the timeout value to find element.
    """

    if isinstance(xpath, str):
        driver.implicitly_wait(timeout)
        try:
            _target = driver.find_element(by=AppiumBy.XPATH, value=xpath)
            TouchAction(driver).tap(_target, count=2).perform()
            LOGGER.debug(f"Double-touch the '{xpath}' element is success.")
        except (selenium.common.exceptions.NoSuchElementException, RuntimeError) as e1:
            LOGGER.exception(msg := f"Double-touch the '{xpath}' is failed")
            raise e1(msg)
        except TimeoutError:
            LOGGER.exception(msg := f"Could not find the '{xpath}' within {timeout} sec.")
            raise TimeoutError(msg)
    elif isinstance(xpath, dict):
        try:
            TouchAction(driver).tap(x=xpath['x'], y=xpath['y'], count=2).perform()
            LOGGER.debug(f"Double-touch the '{xpath}' position is success.")
        except Exception:
            LOGGER.exception(msg := f"Double-touch the '{xpath}' is failed")
            raise Exception(msg)
    else:
        LOGGER.exception(msg := "Please check xpath parameter type is string or dict.")
        raise Exception(msg)


def long_press(driver, xpath: Union[str, dict], timeout=1.0) -> None:
    """Long press an element in current screen.

    :param WebDriver driver: WebDriver obj.
    :param Union[str, dict] xpath: Target element's xpath expression or Target position dictionary {"x": x, "y": y}.
    :param float timeout: Waiting the timeout value to find element.
    """
    if isinstance(xpath, str):
        driver.implicitly_wait(timeout)
        try:
            _target = driver.find_element(by=AppiumBy.XPATH, value=xpath)
            TouchAction(driver).long_press(_target).release().perform()
            LOGGER.debug(f"Long-press the '{xpath}' is success.")
        except (selenium.common.exceptions.NoSuchElementException, RuntimeError) as ex:
            LOGGER.exception(msg := f"Long-press the '{xpath}' is failed")
            raise ex(msg)
        except TimeoutError:
            LOGGER.exception(msg := f"Could not find the '{xpath}' within {timeout} sec.")
            raise TimeoutError(msg)
    elif isinstance(xpath, dict):
        try:
            TouchAction(driver).long_press(x=xpath['x'], y=xpath['y']).release().perform()
            LOGGER.debug(f"Long-press the '{xpath}' is success.")
        except Exception:
            LOGGER.exception(msg := f"Long-press the {xpath} is failed.")
            raise Exception(msg)
    else:
        LOGGER.exception(msg := "Please check xpath parameter type is string or dict.")
        raise Exception(msg)


def scroll(driver, direction="up", times=1, x_position=None) -> None:
    """Scroll the screen.

    :param WebDriver driver: WebDriver obj.
    :param str direction: Scroll direction string. (up, down)
    :param int times: Scroll repeat times. (default=1)
    :param int x_position: Standard X position. (default=None)
    """
    if direction.lower() not in ["up", "down"]:
        LOGGER.exception(msg := "Please check the 'direction' value. The 'direction' value must be in ['up', 'down']")
        raise ValueError(msg)

    _window_size = driver.get_window_size()
    _width = _window_size['width']
    _height = _window_size['height']

    if x_position is None:
        x_position = int(_width / 2)

    try:
        for _ in range(times):
            if direction.lower() == "up":
                TouchAction(driver).press(x=x_position, y=int(_height / 2)).wait(100).move_to(x=x_position, y=int(
                    _height / 4)).release().perform()
            elif direction.lower() == "down":
                TouchAction(driver).press(x=x_position, y=int(_height / 2)).wait(100).move_to(x=x_position, y=int(
                    _height / 4 * 3)).release().perform()
        LOGGER.debug(f"Scroll to {direction} is finish.")
    except Exception:
        LOGGER.exception(msg := f"Could not scroll to {direction}.")
        raise Exception(msg)


def swipe(driver, direction="right", times=1, y_position=None) -> None:
    """Swipe the screen.

    :param WebDriver driver: WebDriver obj.
    :param str direction: Swipe direction string. (right, left)
    :param int times: Swipe repeat times. (default=1)
    :param int y_position: Standard Y position. (default=None)
    """
    if direction.lower() not in ["right", "left"]:
        LOGGER.exception(
            msg := "Please check the 'direction' value. The 'direction' value must be in ['right', 'left']")
        raise ValueError(msg)

    _window_size = driver.get_window_size()
    _width = _window_size['width']
    _height = _window_size['height']

    if y_position is None:
        y_position = int(_height / 2)

    try:
        for _ in range(times):
            if direction.lower() == "left":
                TouchAction(driver).press(x=int(_width / 2), y=y_position).wait(100).move_to(x=int(_width / 4),
                                                                                                  y=y_position).release().perform()
            elif direction.lower() == "right":
                TouchAction(driver).press(x=int(_width / 2), y=y_position).wait(100).move_to(x=int(_width / 4 * 3),
                                                                                                  y=y_position).release().perform()

        LOGGER.debug(f"Swipe to {direction} is finish.")
    except Exception:
        LOGGER.exception(msg := f"Could not swipe to {direction}.")
        raise Exception(msg)


def pinch_in(driver, times=1) -> None:
    """Pinch-In(=to reduce) the current screen.

    :param WebDriver driver: WebDriver obj.
    :param int times: Pinch times.
    """
    _window_size = driver.get_window_size()
    standard_x = int(_window_size['width'] / 2)
    standard_y = int(_window_size['height'] / 2)

    _max_distance = int(math.sqrt(math.pow(standard_x,2) + math.pow(standard_y, 2)) / 2)
    _min_distance = int(math.sqrt(math.pow(standard_x,2) + math.pow(standard_y, 2)) / 5)

    _x1_start = int(standard_x + (_max_distance * math.cos(math.radians(45))))
    _y1_start = int(standard_y + (_max_distance * math.sin(math.radians(45))))
    _x1_end = int(standard_x + (_min_distance * math.cos(math.radians(45))))
    _y1_end = int(standard_y + (_min_distance * math.sin(math.radians(45))))

    _finger1 = TouchAction(driver)
    _finger1.press(x=_x1_start, y=_y1_start).wait(50).move_to(x=_x1_end, y=_y1_end).release()

    _x2_start = int(standard_x + (_max_distance * math.cos(math.radians(225))))
    _y2_start = int(standard_y + (_max_distance * math.sin(math.radians(225))))
    _x2_end = int(standard_x + (_min_distance * math.cos(math.radians(225))))
    _y2_end = int(standard_y + (_min_distance * math.sin(math.radians(225))))

    _finger2 = TouchAction(driver)
    _finger2.press(x=_x2_start, y=_y2_start).wait(50).move_to(x=_x2_end, y=_y2_end).release()

    _multi_touch = MultiAction(driver)
    try:
        for i in range(times):
            _multi_touch.add(_finger1, _finger2)
            _multi_touch.perform()
        LOGGER.debug(f"Pinch-In is finish.")
    except selenium.common.exceptions.WebDriverException:
        LOGGER.exception(msg := f"Could not Pinch-In.")
        raise selenium.common.exceptions.WebDriverException(msg)


def pinch_out(driver, times=1) -> None:
    """Pinch-Out(=to large) the current screen.

    :param WebDriver driver: WebDriver obj.
    :param int times: Pinch times.
    """
    _window_size = driver.get_window_size()
    standard_x = int(_window_size['width'] / 2)
    standard_y = int(_window_size['height'] / 2)

    _max_distance = int(math.sqrt(math.pow(standard_x, 2) + math.pow(standard_y, 2)) / 2)
    _min_distance = int(math.sqrt(math.pow(standard_x, 2) + math.pow(standard_y, 2)) / 5)

    _x1_start = int(standard_x + (_min_distance * math.cos(math.radians(45))))
    _y1_start = int(standard_y + (_min_distance * math.sin(math.radians(45))))
    _x1_end = int(standard_x + (_max_distance * math.cos(math.radians(45))))
    _y1_end = int(standard_y + (_max_distance * math.sin(math.radians(45))))

    _finger1 = TouchAction(driver)
    _finger1.press(x=_x1_start, y=_y1_start).wait(50).move_to(x=_x1_end, y=_y1_end).release()

    _x2_start = int(standard_x + (_min_distance * math.cos(math.radians(225))))
    _y2_start = int(standard_y + (_min_distance * math.sin(math.radians(225))))
    _x2_end = int(standard_x + (_max_distance * math.cos(math.radians(225))))
    _y2_end = int(standard_y + (_max_distance * math.sin(math.radians(225))))

    _finger2 = TouchAction(driver)
    _finger2.press(x=_x2_start, y=_y2_start).wait(50).move_to(x=_x2_end, y=_y2_end).release()

    _multi_touch = MultiAction(driver)
    try:
        for _ in range(times):
            _multi_touch.add(_finger1, _finger2)
            _multi_touch.perform()
        LOGGER.debug(f"Pinch-Out is finish.")
    except selenium.common.exceptions.WebDriverException:
        LOGGER.exception(msg := f"Could not Pinch-Out.")
        raise selenium.common.exceptions.WebDriverException(msg)


def rotate(driver, degree=45, direction="clockwise", times=1) -> None:
    """Rotate degree gesture.

    :param WebDriver driver: WebDriver obj.
    :param int degree: Rotation degree value which is from 5 to 180 and must be divisible by 5. (default=45).
    :param str direction: Rotation direction (clockwise, counterclockwise).
    :param int times: Rotate times.
    """
    if direction.lower() not in ["clockwise", "counterclockwise"]:
        LOGGER.exception(msg := "Please check the 'direction' value. "
                                      "The 'direction' must be in ['clockwise', 'counterclockwise']")
        raise ValueError(msg)

    if ((5 <= degree <= 180) and (degree % 5 == 0)) is False:
        LOGGER.exception(msg := "Please check the 'degree' value. "
                                      "The 'degree' must be from 5 to 180 and must be divisible by 5.")
        raise ValueError(msg)

    _window_size = driver.get_window_size()
    standard_x = int(_window_size['width'] / 2)
    standard_y = int(_window_size['height'] / 2)

    _distance = (standard_x / 4 * 3) if (standard_x / 4 * 3) < (standard_y / 4 * 3) else (standard_y / 4 * 3)

    # create move position
    _x_list = []
    _y_list = []
    _move_times = int(degree / 5) + 1
    for i in range(_move_times):
        if direction == "clockwise":
            _x_list.append(int(standard_x + (_distance * math.cos(math.radians(5 * i + 45)))))
            _y_list.append(int(standard_y + (_distance * math.sin(math.radians(5 * i + 45)))))
        elif direction == "counterclockwise":
            _x_list.append(int(standard_x - (_distance * math.cos(math.radians(225 - 5 * i)))))
            _y_list.append(int(standard_y - (_distance * math.sin(math.radians(225 - 5 * i)))))

    # Init TouchActions
    _finger1 = TouchAction(driver)
    _finger2 = TouchAction(driver)

    _finger1.press(x=standard_x, y=standard_y).release()
    _finger2.press(x=_x_list[0], y=_y_list[0]).wait(50)
    for i in range(1, _move_times):
        _finger2.move_to(x=_x_list[i], y=_y_list[i])
    _finger2.release()

    _multi_touch = MultiAction(driver)
    try:
        for _ in range(times):
            _multi_touch.add(_finger1, _finger2)
            _multi_touch.perform()
        LOGGER.debug(f"Rotate {degree} degrees ({direction}) is finish.")
    except selenium.common.exceptions.WebDriverException:
        LOGGER.exception(msg := f"Could not Rotate {degree} degrees ({direction}).")
        raise selenium.common.exceptions.WebDriverException(msg)

