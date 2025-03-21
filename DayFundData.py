import requests
from bs4 import BeautifulSoup

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 目标网页的 URL
url = 'https://danjuanfunds.com/djmodule/value-center?channel=1300100141'

try:
    # 发送 HTTP 请求
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 检查请求是否成功

    # 使用 BeautifulSoup 解析 HTML 内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取文本内容并分行输出
    all_text = soup.get_text()
    lines = all_text.splitlines()
    for line in lines:
        if line.strip():  # 过滤掉空行
            print(line)

except requests.RequestException as e:
    print(f'请求出错: {e}')
except Exception as e:
    print(f'发生错误: {e}')