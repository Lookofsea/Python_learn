import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_url(page, sexual_orientation):
    url = f"https://www.jjwxc.net/bookbase.php?fw0=0&fbsj0=0&ycx1=1&xx{sexual_orientation}={sexual_orientation}&mainview0=0&sd0=0&lx0=0&fg0=0&bq=-1&" \
          f"sortType=3&isfinish=1&collectiontypes=ors&page={page}"
    return url


def parse(document):
    soup = BeautifulSoup(document, "html.parser")
    table = soup.find("table", attrs={'class': 'cytable'})
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


def main(save_path,sexual_orientation):
	
	#save_path: 文件保存路径
    #sexual_orientation: 1言情2纯爱3百合4女尊5无CP
    
    for page in range(1, 10):
        url = get_url(page, sexual_orientation)
        headers = {

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
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
	main("言情.txt", 1)
