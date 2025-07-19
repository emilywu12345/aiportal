import logging
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page_objects.base_page import BasePage
from utils.log_manager import logger

class TestChatPage(BasePage):
    """聊天页面对象，包含所有聊天相关操作"""

    # 知识库下拉框
    KNOWLEDGE_BOX = (By.XPATH, '//div[@class="el-select__selection" or contains(@class, "el-select__selection")][.//span[normalize-space()="知识库"]]')
   
    # 选值
    SELECT_KNOWLEDGE = (By.XPATH, '//li[contains(@class, "el-select-dropdown__item")]//*[normalize-space()="简历"]')
    
    # 消息输入框
    MESSAGE_INPUT = (By.XPATH, '//div[@class="ant-sender-content"]//textarea[@class="ant-input ant-input-borderless ant-sender-input css-1p3hq3p"]')
    
    # 提交按钮
    SUBMIT_BUTTON = (By.XPATH, '//div[@class="ant-sender-actions-list"]//button[@type="button"]//span[@class="anticon anticon-arrow-up"]')

    # 定位回答内容
    ANSWER_CONTENT = (By.XPATH, '//div[@class="list"]//div[contains(@class, "ant-bubble")]//div[contains(@class, "ant-bubble-content")]//div[@id="md-editor-v-0-preview"]')

    def get_answer(self, message):
        """发送消息并获取AI回答 - 新版本"""
        try:
            # 选择知识库
            self.wait_and_click(self.KNOWLEDGE_BOX)
            self.wait_and_click(self.SELECT_KNOWLEDGE)
            time.sleep(2)
            
            # 输入消息
            self.input_text(self.MESSAGE_INPUT, message)
            self.wait_and_click(self.SUBMIT_BUTTON)
            logger.info(f"已发送消息: {message}")
            
            # 获取回答
            self.wait_for_element(self.ANSWER_CONTENT, timeout=30)
            time.sleep(5)
            answer_element = self.find_element(self.ANSWER_CONTENT)
            time.sleep(5)
            answer = answer_element.text
            logger.info(f"获取到回答: {answer}")
            return answer
        except Exception as e:
            logger.error(f"获取答案失败: {e}")
            return f"获取答案失败: {str(e)}"
        
    