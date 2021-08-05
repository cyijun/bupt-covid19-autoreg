import requests
import re
import json
import datetime
import time
import sys
import traceback


def routine():
    
    class LoginError(Exception):
        pass
    
    login_url = "https://app.bupt.edu.cn/uc/wap/login/check"
    base_url = "https://app.bupt.edu.cn/ncov/wap/default/index"
    save_url = "https://app.bupt.edu.cn/ncov/wap/default/save"

    print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    try:
        # Create session
        session = requests.Session()

        # Generate login data
        load_f = open("userinfo.json", "r")
        login_data = json.load(load_f)

        # Post username and password
        res = session.post(url=login_url, data=login_data)

        # Check the result of login
        if "操作成功" in res.text:
            print("✔️登录成功")
        else:
            print("✖️登录失败，错误信息: " + res.text)
            raise LoginError

        # Get HTML content of the index page, which contains history information
        html_content = session.get(base_url).text

        # Get history information
        history_info_json_str = re.findall(r'oldInfo: ({[^\n]+})', html_content)[0]
        history_info_dict = json.loads(history_info_json_str)

        if history_info_dict != None:
            load_oif = open("userinfo.json", "r")
            load_oif.write(history_info_json_str)

