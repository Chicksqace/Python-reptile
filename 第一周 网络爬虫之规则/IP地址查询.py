import requests
url="https://www.ip138.com/iplookup.php?ip="
# url="https://www.ip138.com/ip.asp?ip="
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
try:
    r=requests.get(url+'36.152.44.95',headers=headers)
    r.status_code=r.raise_for_status()
    print(r.text[-500:])
except:
    print('失败')
