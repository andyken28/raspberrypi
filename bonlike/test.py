import requests
from datetime import datetime, timedelta, timezone
import time
import urllib3
import pytz
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
likepagefetch_url = "https://traodoisub.com/mua/fanpage/fetch.php"
sharepostfetch_url = "https://traodoisub.com/mua/share/fetch.php"
follow_url = "https://traodoisub.com/mua/follow/themid.php"

def get_like_page_state(realid, cookie):
    headers = {
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "PHPSESSID="+cookie,
        "Origin": "https://traodoisub.com",
        "Referer": "https://traodoisub.com/mua/like/",
        "X-Requested-With": "XMLHttpRequest"
    }
    data = {
        "page": 1,
        "query": ""
    }
    response = requests.post(likepagefetch_url, headers=headers, data=data, verify=False)
    
    amount = -1
    if response.status_code == 200:
        response_data = response.json()
        if response_data is not None:
            if "data" in response_data:
                for post in response_data["data"]:
                    print(post['date'])
                    utc_plus_7 = pytz.timezone('Asia/Ho_Chi_Minh')

                    post_date = datetime.strptime(post['date'], "%Y-%m-%d %H:%M:%S")
                    post_date = utc_plus_7.localize(post_date)
                    
                    # current_time = datetime.now()
                    current_time = datetime.now(pytz.utc).astimezone(utc_plus_7)
                    time_difference = timedelta(minutes=2280)
                    if current_time - post_date <= time_difference:
                        print("Thời gian của post nhỏ hơn 5 phút so với thời gian hiện tại.")
                    else:
                        print("Thời gian của post lớn hơn 5 phút so với thời gian hiện tại.")
                    # print(realid)
                    # print(post['real_id'])
                    if post['real_id'] == realid:
                        amount =  post['sl'] - post['datang']
                        print(post)
    return amount

def get_share_post_state(realid, cookie):
    headers = {
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "PHPSESSID="+cookie,
        "Origin": "https://traodoisub.com",
        "Referer": "https://traodoisub.com/mua/like/",
        "X-Requested-With": "XMLHttpRequest"
    }
    data = {
        "page": 1,
        "query": ""
    }
    response = requests.post(sharepostfetch_url, headers=headers, data=data, verify=False)
    print("get_share_post_state: realid=" + realid + ", cookie="+cookie)
    amount = -1
    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
        if response_data is not None:
            if "data" in response_data:
                
                for post in response_data["data"]:
                    
                    if post['real_id'] == realid:
                        amount =  post['sl'] - post['datang']
                        print("get_share_post_state response: " + str(post['sl']) +" - "+ str(post['datang']) + " = "+ str(amount))
    else:
        print("get_share_post_state error: " + str(response.status_code) + ", message=" + response.text)
    return amount

def buy_follow(realid, quantity, username, accountname, cookie, token):
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "PHPSESSID="+cookie,
        "origin": "https://traodoisub.com",
        "referer": "https://traodoisub.com/mua/like/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    payload = {
        "id": realid, 
        "sl": quantity,  
        "dateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    response = requests.post(follow_url, headers=headers, data=payload, verify=False)
    print("buy_follow: username="+ username + ", realid="+ realid + ", quantity="+ str(quantity)+ ", accountname=" + accountname)
 
    if response.status_code == 200:
        if "Mua th" in response.text: #0 cookie
            print("buy_follow success!:")
            
        else:
            logging.info("buy_follow fail!:")
            

    else:
        bonlike.update_handle(accountname, username, realid, 5, 4, logging)
        bonlike.update_money(username, money, 2, logging)
        logging.error("buy_follow error: " + str(response.status_code))


# get_share_post_state('529605596484521','f761aa5576e1c2c84d1f8ba919011abb')
# get_like_page_state('100076354202719','6eca6458102daea40461b048e8cf1f9f')