
import pytest
import allure
import csv
import os
from page_objects.test_aichat_page import TestChatPage

@allure.feature("AI聊天处理")
@pytest.mark.usefixtures("session_logged_in_driver")
class TestAIChatProcessing:
    """自动化处理CSV中的问题并获取AI回答"""

    @pytest.fixture(autouse=True)
    def _inject_driver(self, session_logged_in_driver):
        self.driver = session_logged_in_driver

    def read_questions(self, csv_path='data/example.csv'):
        """读取CSV文件中的问题"""
        with open(csv_path, 'r', encoding='utf-8') as f:
            return [row['问题'] for row in csv.DictReader(f) if row.get('问题')]

    def write_answers(self, questions, answers, csv_path='data/example.csv'):
        """将问题和答案写回CSV文件"""
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['问题', '答案'])
            writer.writeheader()
            writer.writerows([{'问题': q, '答案': a} for q, a in zip(questions, answers)])

    @allure.story("AI 聊天")
    @allure.description("验证用户能否成功发送消息")
    def test_process_ai_chat_questions(self):
        test_aichat = TestChatPage(self.driver)
        questions = self.read_questions()
        
        answers = []
        for question in questions:
            with allure.step(f"处理问题: {question[:30]}..."):
                answer = test_aichat.get_answer(question)
                answers.append(answer)
        
        self.write_answers(questions, answers)
        
        # 断言所有问题都得到了回答
        assert all(answers), "部分问题未获取到答案"
        assert len(questions) == len(answers), "问题与答案数量不匹配"