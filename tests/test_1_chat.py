import pytest
import allure
import time
import logging
from page_objects.knowledge_page import KnowledgePage
from page_objects.chat_page import ChatPage
from utils.config_manager import ConfigManager
from data.test_data import get_ai_chat_data
from utils.log_manager import logger

@allure.feature("聊天")
# 使用类级别已登录driver夹具，保证本类所有用例共用同一浏览器会话，提升执行效率
@pytest.mark.usefixtures("session_logged_in_driver")
class TestChat:
    """
    聊天相关自动化测试用例集。
    - driver 由 class 级别 fixture 注入，所有用例共用同一浏览器会话，提升执行效率。
    - 页面对象模式(POM)业务操作全部通过 ChatPage 实现，测试用例只负责业务流程和断言。
    - 用例结构清晰，便于维护和扩展。
    """

    @pytest.fixture(autouse=True)
    def _inject_driver(self, session_logged_in_driver):
        self.driver = session_logged_in_driver
    
    # def setup_method(self):
    #     """每个测试方法执行前的设置"""
    #     logger.info("开始聊天功能测试")

    # def teardown_method(self):
    #     """每个测试方法执行后的清理"""
    #     logger.info("聊天功能测试完成")

    @allure.story("AI 聊天")
    @allure.description("验证用户能否成功发送消息")
    def test_2_send_message(self):
        """
        步骤：
        1. 发送消息
        2. 验证能否成功发送消息
        """
        chat_page = ChatPage(self.driver)
        with allure.step("发送消息"):
            logging.info("等待页面加载完成")
            assert chat_page.send_message(get_ai_chat_data()["message"]), "发送消息失败"
