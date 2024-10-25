import subprocess
import requests
import time

# 连接到特定的WiFi网络
def connect_to_wifi(ssid):
    command = f'netsh wlan connect name="{ssid}"'
    subprocess.run(command, shell=True)

# 登录校园网
def login_to_campus_network(user_account, user_password):
    login_url = "https://wxrz.ouc.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&jsVersion=4.1&terminal_type=1&lang=zh-cn&v=4049"
    login_data = {
        "user_account": user_account,
        "user_password": user_password,
        "wlan_user_ip": "10.118.210.68",
        "wlan_user_mac": "000000000000"
    }
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "wxrz.ouc.edu.cn:802",
        "Referer": "https://wxrz.ouc.edu.cn/",
        "Sec-Ch-Ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }
    response = requests.post(login_url, data=login_data, headers=headers)
    print(response.text)

# 主函数
def main():
    ssid = "OUC-AUTO"  # WiFi名称
    user_account = "24020007064"  # 替换为您的用户名
    user_password = "01302x"  # 替换为您的密码

    # 连接到WiFi
    connect_to_wifi(ssid)
    print("Connected to WiFi")

    # 等待几秒钟，以确保网络连接稳定
    time.sleep(10)

    # 登录校园网
    login_to_campus_network(user_account, user_password)
    print("Logged in to campus network")

# 运行主函数
if __name__ == "__main__":
    main()
