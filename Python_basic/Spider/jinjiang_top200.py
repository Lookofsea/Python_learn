import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import shutil


def get_url(page):
    url = f"https://www.jjwxc.net/topten.php?orderstr={page}"
    return url


def parse(document):
    soup = BeautifulSoup(document, "html.parser")
    all_table = soup.find_all("table")
    table = all_table[2]
    rows = table.find_all("tr")
    data_all = []
    for row in rows[1:]:
        items = row.find_all("td")
        data = []
        for item in items:
            text = item.get_text(strip=True)
            data.append(text)
        data_all.append(data)
    return data_all


def main(save_path):

    current_work_dir = os.path.dirname(__file__)  # 当前文件所在的目录
	
	#save_path: 文件保存路径
    #sexual_orientation: 1言情2纯爱3百合4女尊5无CP
    # 3-8表示5个榜单
    for page in range(3,8):
        url = get_url(page)
        headers = {

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
            }
        html = requests.get(url, headers=headers)
        html.encoding = html.apparent_encoding
        try:
            data = parse(html.content)
        except:
            print("爬取失败：", page)
            continue
        if len(data) == 0:
            break
        df = pd.DataFrame(data)
        df.to_csv(save_path, mode='a', header=False, index=False)
        print(page)
        time.sleep(3)



if __name__ == "__main__":
    
	main("./榜单排行.txt")
