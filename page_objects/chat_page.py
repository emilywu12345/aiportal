import logging
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from page_objects.base_page import BasePage
from utils.log_manager import logger

class ChatPage(BasePage):
    """聊天页面对象，包含所有聊天相关操作"""

    #知识库下拉框
    KNOWLEDGE_BOX= (By.XPATH, '//div[@class="el-select__selection" or contains(@class, "el-select__selection")][.//span[normalize-space()="知识库"]]')
   
    # 选值
    SELECT_KNOWLEDGE = (By.XPATH, '//li[contains(@class, "el-select-dropdown__item")]//*[normalize-space()="简历"]')
    
    # 消息输入框
    MESSAGE_INPUT = (By.XPATH, '//div[@class="ant-sender-content"]//textarea[@class="ant-input ant-input-borderless ant-sender-input css-1p3hq3p"]')
    
    # 提交按钮
    SUBMIT_BUTTON = (By.XPATH, '//div[@class="ant-sender-actions-list"]//button[@type="button"]//span[@class="anticon anticon-arrow-up"]')

    # 定位所有P标签
    ALL_PARAGRAPHS = (By.XPATH, '//div[@class="list"]//div[@class="ant-bubble css-1r7p0rg ant-bubble-start"]//div[@class="ant-bubble-content ant-bubble-content-filled"]//div[@id="md-editor-v-0-preview"]/p')

    @allure.step("AI 聊天")
    def send_message(self, message):
        """AI 聊天页面"""
        try:
            # 先等待loading遮罩消失
            self.wait_loading_disappear(timeout=20)
            
            # 点击知识库下拉框
            self.wait_and_click(self.KNOWLEDGE_BOX)
            
            # 等待知识库下拉选项出现并选择
            self.wait_for_element(self.SELECT_KNOWLEDGE, timeout=self.timeout)
            self.wait_and_click(self.SELECT_KNOWLEDGE)
            
            time.sleep(5)
            # 输入消息内容
            self.input_text(self.MESSAGE_INPUT, message)

            time.sleep(5)
            
            # 点击提交按钮
            self.wait_and_click(self.SUBMIT_BUTTON)
            
            # 等待消息发送完成 - 使用显式等待检查消息是否出现
            self.wait_for_element(self.ALL_PARAGRAPHS, timeout=30)
            logger.info("消息已发送")
            time.sleep(10)
            # 獲取P标签文本
            p_elements = self.find_element(self.ALL_PARAGRAPHS)
            time.sleep(5)
            logger.info(f"AI 聊天结果: {p_elements.text}")
            time.sleep(5)  # 等待消息处理完成
            return True
        except Exception as e:
            logger.error(f"AI聊天失败: {e}")
            return self.handle_exception(e, "AI聊天失败")
        
    