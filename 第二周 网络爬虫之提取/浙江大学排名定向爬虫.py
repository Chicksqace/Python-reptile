import requests
from bs4 import BeautifulSoup
import openpyxl
url = 'http://www.gaosan.com/gaokao/571199.html'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
response = requests.get(url,headers=headers)
response.encoding=response.apparent_encoding
soup = BeautifulSoup(response.text, 'html.parser')
# 获取省市序、学校名称、省市、类型前十名信息
table = soup.find('table', {'border': '1'})
rows = table.find_all('tr')
for row in rows[1:11]:  # 取前十名
    cols = row.find_all('td')
    rank = cols[0].text.strip()
    school_name = cols[1].text.strip()
    province_city = cols[2].text.strip()
    school_type = cols[3].text.strip()
    # 输出信息
    print(rank, school_name, province_city, school_type)
    with open("1.txt",'a',encoding='utf-8') as data:
        data.write(rank+'  ')
        data.write(school_name+'  ')
        data.write(province_city+'  ')
        data.write(school_type+'     '+'\n')