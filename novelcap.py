import bs4
import requests
from bs4 import BeautifulSoup


def fetch_webpage(url):
    # 发送HTTP请求
    response = requests.get(url)
    response.encoding = "utf-8"

    # 检查请求是否成功
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

def parse_webpage(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    print(soup.select_one('#BookCon h1').get_text())
    # 假设我们要提取所有的标题标签
    booklog = soup.find('div',id = "BookCon")
    # 获取所有子元素（直接子元素）
    # for child in book.children:
    #     if isinstance(child, bs4.element.Tag):  # 检查是否为Tag对象，排除空白和换行
    #         print(child)

    # 获取标题
    titlelog = booklog.find('h1')
    book = []
    book.append(titlelog.text)

    # 正文
    contentlog = booklog.find("div",id = "BookText")
    for pagrah in contentlog.find_all("p"):
        book.append(pagrah.text)

    return book

def outtxt(book):
    path = "D:\OneDrive\桌面\爬取小说" + "\\" + book[0] +".txt"
    with open(path, 'w', encoding='utf-8') as file:
        # 将数据写入文件
        for line in book:
            file.write(line + '\n')



if __name__ == "__main__":
    url = "http://www.jianlaixiaoshuo.com/book/17.html"
    html_content = fetch_webpage(url)
    if html_content:
        book = parse_webpage(html_content)
        # outtxt(book)