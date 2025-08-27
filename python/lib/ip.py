import requests

def get_location_by_ip(ip):
    url = f'http://ip-api.com/json/{ip}'
    response = requests.get(url)
    data = response.json()

    # 提取相关信息
    if data['status'] == 'fail':
        return None
    else:
        return {
            'country': data.get('country'),
            'region': data.get('regionName'),  # 省份
            'city': data.get('city'),          # 城市
            'district': data.get('district'),  # 区域（如果有）
        }

ip = "112.64.52.236"  # 替换为你要查询的 IP 地址
location = get_location_by_ip(ip)

if location:
    print(location)
else:
    print("无法解析 IP 地址位置")
