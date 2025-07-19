import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page_objects.base_page import BasePage
from utils.log_manager import logger

class LoginPage(BasePage):
    """登录页面操作封装"""

    # 正常登录元素定位
    USERNAME_INPUT = (By.CSS_SELECTOR, '.el-input__inner[type="text"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '.el-input__inner[type="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.el-button--primary')
    # AI聊天标题
    AI_CHAT_TITLE = (By.XPATH, '//div[@class="header"]//div[@class="content"]')

    @allure.step("执行正常登录操作")
    def login(self, username: str, password: str, timeout: int = 30) -> bool:
        try:
            logger.info(f"登录操作: {username}")
            self.open()
            # 先等待loading遮罩消失
            self.wait_loading_disappear(timeout=20)

            time.sleep(2)  # 等待页面加载稳定
            # 输入账号密码
            self.input_text(self.USERNAME_INPUT, username)
            self.input_text(self.PASSWORD_INPUT, password)
            # 点击登录按钮
            self.click(self.LOGIN_BUTTON)
            # 等待 AI 聊天标题出现
            self.wait_for_element(self.AI_CHAT_TITLE, timeout=timeout)
            logger.info("登录成功")
            return True
        except Exception as e:
            logger.error(f"登录失败: {e}")
            return self.handle_exception(e, "登录失败")