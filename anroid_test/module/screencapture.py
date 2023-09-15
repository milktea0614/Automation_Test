# -*- coding: utf-8 -*-
"""Screencapture
()
"""
import os
import logging
import datetime

from miraelogger import Logger

LOGGER = Logger(log_name=__name__, stream_log_level=logging.DEBUG)


def save_ui_dump(driver, directory_path, is_mobile=True):
    """Save Screenshot and XML into local.

    :param WebDriver driver: WebDriver obj.
    :param str directory_path: Directory path to save files.
    :param bool is_mobile: Is mobile option. (default=True)
    """
    _current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Web: page source, Mobile: XML
    _page_source = driver.page_source
    if is_mobile:
        _page_path = os.path.join(directory_path, f"{_current_time}.xml")
    else:
        _page_path = os.path.join(directory_path, f"{_current_time}.html")

    with open(_page_path, 'w', encoding='utf-8') as f:
        f.write(_page_source)

    _screenshot_path = os.path.join(directory_path, f"{_current_time}.png")
    _screenshot = driver.save_screenshot(_screenshot_path)


# ScreenRecord (appium/webdriver/extensions/screen_record.py)
def start_recording(driver):
    """Start recording screen.

    :param WebDriver driver: WebDriver obj.
    """
    driver.start_recording_screen()


def stop_recording(driver, path):
    """Stop recording and save video file into local.

    :param WebDriver driver: WebDriver obj.
    :param str path: Directory path or file path (which include the .mp4) to save files.
    """
    _current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if ".mp4" not in path:
        _path = os.path.join(path, f"{_current_time}.mp4")
    else:
        _path = path

    _video_data = driver.stop_recording_screen()
    with open(_path, 'wb') as f:
        f.write(_video_data)
