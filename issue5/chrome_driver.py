#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from typing import List
from xml.dom.minidom import Element

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

logger = logging.getLogger(__name__)


class ChromeDriver(object):
    """
    スクレイピングに関する機能はここに実装しよう！
    """

    def __init__(self) -> None:
        self.driver = self.set_driver()

    def set_driver(self):
        options = ChromeOptions()
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
        options.add_argument('--ignore-ssl-errors')
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities["acceptInsecureCerts"] = True
        options.add_argument("--window-size=1400,900")
        # options.add_argument('--incognito')
        options.add_experimental_option("detach", True)

        return Chrome(executable_path=ChromeDriverManager().install(),
                      options=options,
                      desired_capabilities=capabilities)

    def close_driver(self) -> None:
        self.driver.close()
        self.driver.quit()

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def get_elements(self, target: str, elements: List[WebElement]) -> bool:
       
        elements_ = self.driver.find_elements(By.CSS_SELECTOR, target)
        if not elements_:
            logger.error(
                f"Failed to get target. target: {target}", exc_info=True)
            return False

        elements.extend(elements_)

        return True

    def get_text(self, elem: WebElement, target: str):
        elements = elem.find_elements(By.CSS_SELECTOR, target)
        if not elements:
            logger.error(
                "Failed to get target element!", exc_info=True)
        return elements[0].text.strip()
        
    def item_get_url(self, elem: WebElement, target: str):
        elements = elem.find_elements(By.CSS_SELECTOR, target)
        if not elements:
            logger.error(
                "Failed to get target element!", exc_info=True)
        return elements[0].get_attribute("href")
    
    