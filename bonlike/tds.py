import requests
from datetime import datetime, timedelta, timezone
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pytz
# URL traodoisub
login_url = "https://traodoisub.com/scr/login.php"
likepostfetch_url = "https://traodoisub.com/mua/like/fetch.php"
camxucfetch_url = "https://traodoisub.com/mua/reaction/fetch.php"
likepagefetch_url = "https://traodoisub.com/mua/fanpage/fetch.php"
sharepostfetch_url = "https://traodoisub.com/mua/share/fetch.php"
followfetch_url = "https://traodoisub.com/mua/follow/fetch.php"
def get_cookie(accountname, password, logging):
    payload = {
        "username": accountname,
        "password": password
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-requested-with": "XMLHttpRequest"
    }
    phpsessid = ""
    logging.info("get_cookie: accountname=" + accountname +", password=" + password)
    with requests.Session() as session:
        response = session.post(login_url, data=payload, headers=headers)
        if response.status_code == 200:
            cookies = session.cookies.get_dict()
            phpsessid = cookies.get('PHPSESSID', None)
            logging.info("get_cookie response: " + str(cookies))
        else:
            logging.info("get_cookie error: " + str(response.status_code) + ", message=" + response.text)
    return phpsessid

def get_xu(token, logging):
    url = "https://traodoisub.com/api/?fields=profile&access_token="+token
    response = requests.get(url, verify=False)
    xu = -1
    logging.info("get_xu: token=" + token)
    if response.status_code == 200:
        data = response.json()
        if data is not None:
            xu = data['data']['xu']
        logging.info("get_xu response: " + str(response.json()))
    else:
        logging.error("get_xu error: " + str(response.status_code) + ", message=" + response.text)
    return xu

def get_like_post_state(realid, cookie, logging):
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
    response = requests.post(likepostfetch_url, headers=headers, data=data, verify=False)
    logging.info("get_like_post_state: realid=" + realid + ", cookie="+cookie)
    amount = -1
    if response.status_code == 200:
        response_data = response.json()
        if response_data is not None:
            if "data" in response_data:
                for post in response_data["data"]:
                    if post['real_id'] == realid:
                        amount =  post['sl'] - post['datang']
                        logging.info("get_like_post_state: " + str(post['sl']) +" - "+ str(post['datang']) + " = "+ str(amount))
    else:
        logging.error("get_like_post_state error: " + str(response.status_code) + ", message=" + response.text)
    return amount


def get_cam_xuc_state(realid, cookie, logging):
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
    response = requests.post(camxucfetch_url, headers=headers, data=data, verify=False)
    logging.info("get_cam_xuc_state: realid=" + realid + ", cookie="+cookie)
    amount = -1
    if response.status_code == 200:
        response_data = response.json()
        if response_data is not None:
            if "data" in response_data:
                for post in response_data["data"]:
                    if post['real_id'] == realid:
                        amount =  post['sl'] - post['datang']
                        logging.info("get_cam_xuc_state response: " + str(post['sl']) +" - "+ str(post['datang']) + " = "+ str(amount))
    else:
        logging.info("get_cam_xuc_state error: " + str(response.status_code) + ", message=" + response.text)
    return amount


def get_like_page_state(realid, cookie, logging):
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
    logging.info("get_like_page_state: realid=" + realid + ", cookie="+cookie)
    amount = -1
    if response.status_code == 200:
        response_data = response.json()
        if response_data is not None:
            if "data" in response_data:
                for post in response_data["data"]:
                    if post['real_id'] == realid:
                        amount =  post['sl'] - post['datang']
                        logging.info("get_like_page_state response: " + str(post['sl']) +" - "+ str(post['datang']) + " = "+ str(amount))
    else:
        logging.info("get_like_page_state error: " + str(response.status_code) + ", message=" + response.text)
    return amount


def update_like_page_state(cookie, logging):
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
    logging.info("update_like_page_state: cookie="+cookie)
    idpost = "unknown"
    if response.status_code == 200:
        response_data = response.json()
        if response_data is not None:
            if "data" in response_data:
                for post in response_data["data"]:
                    utc_plus_7 = pytz.timezone('Asia/Ho_Chi_Minh')
                    post_date = datetime.strptime(post['date'], "%Y-%m-%d %H:%M:%S")
                    post_date = utc_plus_7.localize(post_date)

                    current_time = datetime.now(pytz.utc).astimezone(utc_plus_7)
                    time_difference = timedelta(minutes=5)
                    if current_time - post_date <= time_difference:
                        logging.info("update_like_page_state time: start=" + str(post_date) +", now="+ str(current_time))
                        idpost = post['real_id']
                        break
    else:
        logging.info("update_like_page_state error: " + str(response.status_code) + ", message=" + response.text)
    return idpost


def get_share_post_state(realid, cookie, logging):
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
    logging.info("get_share_post_state: realid=" + realid + ", cookie="+cookie)
    amount = -1
    if response.status_code == 200:
        response_data = response.json()
        if response_data is not None:
            if "data" in response_data:
                for post in response_data["data"]:
                    if post['real_id'] == realid:
                        amount =  post['sl'] - post['datang']
                        logging.info("get_share_post_state response: " + str(post['sl']) +" - "+ str(post['datang']) + " = "+ str(amount))
    else:
        logging.info("get_share_post_state error: " + str(response.status_code) + ", message=" + response.text)
    return amount


def get_follow_state(realid, cookie, logging):
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
    response = requests.post(followfetch_url, headers=headers, data=data, verify=False)
    logging.info("get_follow_state: realid=" + realid + ", cookie="+cookie)
    amount = -1
    if response.status_code == 200:
        response_data = response.json()
        if response_data is not None:
            if "data" in response_data:
                for post in response_data["data"]:
                    if post['real_id'] == realid:
                        amount =  post['sl'] - post['datang']
                        logging.info("get_follow_state response: " + str(post['sl']) +" - "+ str(post['datang']) + " = "+ str(amount))
    else:
        logging.info("get_follow_state error: " + str(response.status_code) + ", message=" + response.text)
    return amount

