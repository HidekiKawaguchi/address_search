import requests

zipcode = "7984101"
# zipcode = input("郵便番号<ハイフン無し7桁>は?")
url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

response = requests.get(url)
print(response)
print(response.text)
