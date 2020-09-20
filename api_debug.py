import requests
r = requests.get(
    'https://douban.lovemefan.top/api/v2/search/movie?udid=a4684a67c5db66436da276d582163766f927d703&apikey=054022eaeae0b00e0fc068c0c0a2102a&channel=Douban&q='
    + 'Forever')

r_json = r.json()
print(r_json['items'])