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
        load_oif = open("oldinfo.json", "r")
        history_info_dict = json.loads(load_oif.read())

        # Generate new information
        new_info_dict = history_info_dict.copy()
        today = datetime.date.today()
        new_info_dict.update({
            "id": json.loads(re.findall(r'def = ({[^\n]+})', html_content)[0])['id'],
            "name": re.findall(r'realname: "([^\"]+)",', html_content)[0],
            "number": re.findall(r"number: '([^\']+)',", html_content)[0],
            "date": "%4d%02d%02d" % (today.year, today.month, today.day),
            "created": round(time.time())
        })

        # Try to post new information
        res = session.post(url=save_url, data=new_info_dict)

        # Check the result from posted new information
        if "成功" in res.text:
            print("✔️打卡成功")
        elif "今天已经填报了" in res.text:
            print("✔️今日已打卡")
        else:
            print("✖️打卡失败，错误信息: " + res.text)

    except LoginError:
        pass
    except:
        print("其他错误，错误信息如下")
        traceback.print_exc()

    print("\n\n")
    sys.stdout.flush()


print("程序已成功运行\n\n")
sys.stdout.flush()

start_time='00:01'
end_time='12:00'

# 范围时间
d_time = datetime.datetime.strptime(str(datetime.datetime.now().date())+start_time, '%Y-%m-%d%H:%M')
d_time1 =  datetime.datetime.strptime(str(datetime.datetime.now().date())+end_time, '%Y-%m-%d%H:%M')

routine()
while True:
    # 当前时间
    n_time = datetime.datetime.now()
    # 判断当前时间是否在范围时间内
    if n_time > d_time and n_time<d_time1:
        routine()
    time.sleep(3600)
