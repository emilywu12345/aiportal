import logging
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page_objects.base_page import BasePage
from utils.log_manager import logger

class KnowledgePage(BasePage):
    """知识库页面对象，包含所有知识库相关操作"""
    
    # 页面元素定位器
    KNOWLEDGE = (By.XPATH, '//*[@class="title" and text()="知识库"]')  
    KNOWLEDGE_TITLE = (By.XPATH, '//*[@class="title" and text()="知识库管理"]')                                           # 知识库菜单
    # CREATE_KB_BUTTON = (By.XPATH, '//*[@class="create-knowledge-base"]')              # 创建知识库按钮
    # KB_NAME_INPUT = (By.XPATH, '//*[@placeholder="请输入知识库名称"]')         # 知识库名称输入框
    # KB_DESC_INPUT = (By.XPATH, '//*[@placeholder="请输入知识库描述"]')         # 知识库描述输入框
    # MODEL_SELECT = (By.XPATH, '//*[@class="vector-model-select"]')                          # 向量模型选择器
    # MODEL_OPTIONS = (By.XPATH, '//*[@class="el-select-dropdown__item"]')                    # 向量模型选项列表
    # CONFIRM_CREATE_BUTTON = (By.XPATH, '//*[@class="dialog-footer"]//button[text()="确认"]')        # 确认创建按钮
    # SUCCESS_MESSAGE = (By.XPATH, '//*[@class="el-message--success"]')                       # 操作成功提示
    # ERROR_MESSAGE = (By.XPATH, '//*[@class="el-message--error"]')                          # 错误提示消息

    # # 知识库列表元素
    # KB_LIST = (By.CSS_SELECTOR, '.knowledge-list')                                    # 知识库列表容器
    # KB_ITEMS = (By.CSS_SELECTOR, '.knowledge-card')                                   # 知识库卡片
    # KB_NAME = (By.CSS_SELECTOR, '.knowledge-name')                                    # 知识库名称
    # KB_DESC = (By.CSS_SELECTOR, '.knowledge-desc')                                    # 知识库描述
    
    # # 编辑相关元素
    # EDIT_BUTTON = (By.CSS_SELECTOR, 'button.edit-btn')                               # 编辑按钮
    # DELETE_BUTTON = (By.CSS_SELECTOR, 'button.delete-btn')                           # 删除按钮
    # CONFIRM_DELETE = (By.CSS_SELECTOR, '.el-message-box__btns .confirm')             # 确认删除按钮
    
    
    # # 编辑知识库元素
    # FIRST_KB_ITEM = ('xpath', '//div[contains(@class, "knowledge-card")][1]')
    # EDIT_KB_BUTTON = ('xpath', '//button[contains(@class, "edit-btn")]')
    # KB_LIST = (By.XPATH, '//*[@class="title" and text()="知识库"]')
    # SUCCESS_MESSAGE = ('xpath', '//div[contains(@class, "success-message")]')
    @allure.step("进入知识库管理页面")
    def navigate_to_knowledge(self):
        """导航到知识库管理页面"""
        try:
            logging.info('正在进入知识库管理页面')
            self.find_element(self.KNOWLEDGE).click()

            # 等待知识库管理页面加载
            logging.info('等待知识库管理页面加载...')
            WebDriverWait(self.driver, self.wait_times['medium']).until(
                    EC.presence_of_element_located(self.KNOWLEDGE_TITLE)
                )
            time.sleep(1)
            self.take_screenshot("进入知识库管理页面")
            logging.info('成功进入知识库管理页面')
            return True


        # 当使用 find_element 或 find_elements 方法尝试查找页面上的元素，但元素不存在时，会抛出此异常
        except NoSuchElementException as e:
            logger.error(f'登入失敗: 元素未找到 - {str(e)}')
            self.take_screenshot("登入失敗")
            return False

        # 当使用显式等待（如 WebDriverWait）等待某个元素或条件出现，但超过了指定的超时时间仍未满足条件时，会抛出此异常
        except TimeoutException as e:
            logger.error(f'登入失敗: 等待元素超時 - {str(e)}')
            self.take_screenshot("登入失敗")
            return False

        # 当上述两种特定异常（NoSuchElementException 和 TimeoutException）都不匹配时，会进入这个块来处理其他未知的异常
        except Exception as e:
            logger.error(f"登入失敗: 發生未知異常 - {str(e)}")
            self.take_screenshot("登入異常")
            return False

    # @allure.step("创建知识库")
    # def create_knowledge_base(self, name, description, model="OpenAI-Embedding-Azure"):
    #     """
    #     创建新的知识库
    #     Args:
    #         name: 知识库名称
    #         description: 知识库描述
    #         model: 向量模型名称，默认使用OpenAI
    #     Returns:
    #         bool: 创建是否成功
    #     """
    #     try:
    #         if not self.navigate_to_knowledge_base():
    #             return False
            
    #         logging.info(f'开始创建知识库: {name}')
    #         if not self._open_create_dialog():
    #             return False
                
    #         if not self._fill_kb_info(name, description, model):
    #             return False
                
    #         if not self._submit_and_verify():
    #             return False
                
    #         logging.info('知识库创建成功')
    #         return True
                
    #     except Exception as e:
    #         logging.error(f'创建知识库失败: {str(e)}')
    #         self.take_screenshot('create_kb_failed')
    #         return False
    
    # @allure.step("打开创建对话框")        
    # def _open_create_dialog(self):
    #     """打开创建知识库对话框"""
    #     try:
    #         if not self.wait_and_click(self.CREATE_KB_BUTTON):
    #             logging.error('找不到或无法点击创建按钮')
    #             self.take_screenshot('open_dialog_failed')
    #             return False
    #         return True
    #     except Exception as e:
    #         logging.error(f'打开创建对话框失败: {str(e)}')
    #         return False
            
    # @allure.step("填写知识库信息")
    # def _fill_kb_info(self, name, description, model):
    #     """
    #     填写知识库信息
    #     Returns:
    #         bool: 填写是否成功
    #     """
    #     try:
    #         logging.info('填写知识库信息')
    #         if not self.input_text(self.KB_NAME_INPUT, name):
    #             logging.error('输入知识库名称失败')
    #             return False
                
    #         if not self.input_text(self.KB_DESC_INPUT, description):
    #             logging.error('输入知识库描述失败')
    #             return False
                
    #         # 选择向量模型
    #         if not self._select_model(model):
    #             return False
                
    #         return True
            
    #     except Exception as e:
    #         logging.error(f'填写知识库信息失败: {str(e)}')
    #         self.take_screenshot('fill_info_failed')
    #         return False
    
    # @allure.step("选择向量模型")
    # def _select_model(self, model_name):
    #     """
    #     选择向量模型
    #     Args:
    #         model_name: 模型名称
    #     Returns:
    #         bool: 选择是否成功
    #     """
    #     try:
    #         # 点击下拉框
    #         if not self.click(self.MODEL_SELECT):
    #             logging.error('无法打开模型选择器')
    #             return False
            
    #         # 等待选项出现并选择
    #         options = self.find_elements(self.MODEL_OPTIONS)
    #         for option in options:
    #             if model_name in option.text:
    #                 option.click()
    #                 return True
                    
    #         logging.error(f'未找到指定的模型: {model_name}')
    #         return False
            
    #     except Exception as e:
    #         logging.error(f'选择模型失败: {str(e)}')
    #         return False
            
    # @allure.step("提交并验证")
    # def _submit_and_verify(self):
    #     """
    #     提交表单并验证结果
    #     Returns:
    #         bool: 是否成功
    #     """
    #     try:
    #         logging.info('提交知识库创建')
    #         if not self.click(self.CONFIRM_CREATE_BUTTON):
    #             logging.error('点击确认按钮失败')
    #             return False
            
    #         # 检查是否有错误提示
    #         if self.is_element_visible(self.ERROR_MESSAGE, timeout=3):
    #             error_text = self.get_text(self.ERROR_MESSAGE)
    #             logging.error(f'创建失败: {error_text}')
    #             self.take_screenshot('create_error')
    #             return False
            
    #         # 等待成功提示
    #         if not self.wait_for_element(self.SUCCESS_MESSAGE, timeout=self.wait_times['medium']):
    #             logging.error('未收到成功提示')
    #             self.take_screenshot('no_success_message')
    #             return False
                
    #         return True
            
    #     except Exception as e:
    #         logging.error(f'提交验证失败: {str(e)}')
    #         self.take_screenshot('submit_failed')
    #         return False
    
    # @allure.step("编辑知识库")
    # def edit_knowledge_base(self, kb_name, new_name, new_description):
    #     """
    #     编辑指定的知识库
    #     Args:
    #         kb_name: 要编辑的知识库名称
    #         new_name: 新的知识库名称
    #         new_description: 新的知识库描述
    #     Returns:
    #         bool: 编辑是否成功
    #     """
    #     try:
    #         if not self.navigate_to_knowledge_base():
    #             return False
                
    #         if not self._find_and_click_kb(kb_name):
    #             return False
                
    #         if not self._edit_kb_info(new_name, new_description):
    #             return False
                
    #         if not self._submit_and_verify():
    #             return False
                
    #         logging.info('知识库编辑成功')
    #         return True
            
    #     except Exception as e:
    #         logging.error(f'编辑知识库失败: {str(e)}')
    #         self.take_screenshot('edit_kb_failed')
    #         return False
            
    # @allure.step("查找并点击知识库")
    # def _find_and_click_kb(self, kb_name):
    #     """
    #     在列表中查找并点击指定的知识库
    #     Args:
    #         kb_name: 知识库名称
    #     Returns:
    #         bool: 是否找到并点击成功
    #     """
    #     try:
    #         logging.info(f'查找知识库: {kb_name}')
    #         # 等待知识库列表加载
    #         if not self.wait_for_element(self.KB_LIST):
    #             logging.error('知识库列表加载失败')
    #             return False
                
    #         # 遍历所有知识库卡片
    #         kb_cards = self.find_elements(self.KB_ITEMS)
    #         for card in kb_cards:
    #             name_element = card.find_element(*self.KB_NAME)
    #             if kb_name in name_element.text:
    #                 # 点击编辑按钮
    #                 edit_btn = card.find_element(*self.EDIT_BUTTON)
    #                 edit_btn.click()
    #                 return True
                    
    #         logging.error(f'未找到知识库: {kb_name}')
    #         return False
            
    #     except Exception as e:
    #         logging.error(f'查找知识库失败: {str(e)}')
    #         self.take_screenshot('find_kb_failed')
    #         return False
            
    # @allure.step("更新知识库信息")
    # def _edit_kb_info(self, new_name, new_description):
    #     """
    #     更新知识库信息
    #     Args:
    #         new_name: 新的知识库名称
    #         new_description: 新的知识库描述
    #     Returns:
    #         bool: 更新是否成功
    #     """
    #     try:
    #         logging.info('更新知识库信息')
    #         # 清除并输入新的名称
    #         if not self.input_text(self.KB_NAME_INPUT, new_name, clear=True):
    #             logging.error('更新知识库名称失败')
    #             return False
                
    #         # 清除并输入新的描述
    #         if not self.input_text(self.KB_DESC_INPUT, new_description, clear=True):
    #             logging.error('更新知识库描述失败')
    #             return False
                
    #         return True
            
    #     except Exception as e:
    #         logging.error(f'更新知识库信息失败: {str(e)}')
    #         self.take_screenshot('update_info_failed')
    #         return False
            
    # @allure.step("删除知识库")
    # def delete_knowledge_base(self, kb_name):
    #     """
    #     删除指定的知识库
    #     Args:
    #         kb_name: 要删除的知识库名称
    #     Returns:
    #         bool: 删除是否成功
    #     """
    #     try:
    #         if not self.navigate_to_knowledge_base():
    #             return False
                
    #         logging.info(f'准备删除知识库: {kb_name}')
    #         # 查找知识库
    #         kb_cards = self.find_elements(self.KB_ITEMS)
    #         for card in kb_cards:
    #             name_element = card.find_element(*self.KB_NAME)
    #             if kb_name in name_element.text:
    #                 # 点击删除按钮
    #                 delete_btn = card.find_element(*self.DELETE_BUTTON)
    #                 delete_btn.click()
                    
    #                 # 确认删除
    #                 if not self.click(self.CONFIRM_DELETE):
    #                     logging.error('确认删除失败')
    #                     return False
                        
    #                 # 验证删除成功
    #                 if not self.wait_for_element(self.SUCCESS_MESSAGE):
    #                     logging.error('未收到删除成功提示')
    #                     return False
                        
    #                 logging.info('知识库删除成功')
    #                 return True
                    
    #         logging.error(f'未找到要删除的知识库: {kb_name}')
    #         return False
            
    #     except Exception as e:
    #         logging.error(f'删除知识库失败: {str(e)}')
    #         self.take_screenshot('delete_kb_failed')
    #         return False
            
    # def get_knowledge_base_list(self):
    #     """
    #     获取知识库列表
    #     Returns:
    #         list: 知识库信息列表，每个元素包含名称和描述
    #     """
    #     result = []
    #     try:
    #         if not self.navigate_to_knowledge_base():
    #             return result
                
    #         # 等待列表加载
    #         if not self.wait_for_element(self.KB_LIST):
    #             return result
                
    #         # 获取所有知识库卡片
    #         kb_cards = self.find_elements(self.KB_ITEMS)
    #         for card in kb_cards:
    #             try:
    #                 name = card.find_element(*self.KB_NAME).text
    #                 desc = card.find_element(*self.KB_DESC).text
    #                 result.append({
    #                     'name': name,
    #                     'description': desc
    #                 })
    #             except:
    #                 continue
                    
    #         return result
            
    #     except Exception as e:
    #         logging.error(f'获取知识库列表失败: {str(e)}')
    #         self.take_screenshot('get_list_failed')
    #         return result
    
    # def wait_and_click(self, locator, timeout: int = 10) -> bool:
    #     """
    #     等待元素出现并点击
    #     Args:
    #         locator: 元素定位器
    #         timeout: 超时时间（秒）
    #     Returns:
    #         bool: 是否点击成功
    #     """
    #     try:
    #         if self.wait_for_element(locator, timeout=timeout):
    #             element = self.find_element(locator, timeout=timeout)
    #             element.click()
    #             return True
    #         else:
    #             return False
    #     except Exception as e:
    #         logging.error(f"wait_and_click 失败: {str(e)}")
    #         self.take_screenshot("wait_and_click_failed")
    #         return False
