import requests

url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=2660005"

response = requests.get(url)
print(response)
print(response.text)
