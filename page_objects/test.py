# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time


# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# options = Options()
# # 忽略 SSL 相关报错，提升兼容性
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# options.add_argument('--allow-insecure-localhost')
# options.add_argument('--disable-web-security')
# # 可选：复用本地 Chrome 用户数据目录（如需更快加载体验可取消注释并填写实际路径）
# # options.add_argument(r'--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data')


# # 设置 pageLoadStrategy 为 'none'，只等主文档加载完毕（新版写法）
# options.set_capability('pageLoadStrategy', 'none')


# start = time.time()
# driver = webdriver.Chrome(options=options)
# print(f"[INFO] Chrome 启动耗时: {time.time() - start:.2f}s")

# start = time.time()
# driver.get('http://57.158.72.194/csdc-ai-portal/#/login')

# print(f"[INFO] 页面加载请求耗时: {time.time() - start:.2f}s")

# # 显式等待登录输入框出现，保证页面可交互
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# try:
#     WebDriverWait(driver, 20).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, '.el-input__inner[type="text"]'))
#     )
#     print("[INFO] 登录输入框已加载，可进行后续操作")
# except Exception as e:
#     print(f"[ERROR] 等待登录输入框超时: {e}")


import csv
# 读取data目录下的example.csv文件的问题列，打印每个问题
# def process_csv(self, csv_path):
#     with open(csv_path, mode='r', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             print(row['问题'])
#             return row['问题']

# 读取data目录下的example.csv文件的问题列，返回所有问题
def get_questions():
    questions = []
    with open('data/example.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            questions.append(row['问题'])
    for question in questions:
        print(question)
    return questions

get_questions()

# 将回复写入到data目录下的example.csv文件的答案列
def write_answers(answers):
    questions = get_questions()
    with open('data/example.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['问题', '答案'])
        writer.writeheader()
        for question, answer in zip(questions, answers):
            writer.writerow({'问题': question, '答案': answer})
            print(f"问题：{question}，答案：{answer}")
write_answers(['今天天气晴朗', '今天天气晴朗还好啊']) 