import bonlike
import tds
import requests
from datetime import datetime, timedelta, timezone
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#tds
likepost_url = "https://traodoisub.com/mua/like/themid.php"
likepage_url = "https://traodoisub.com/mua/fanpage/themid.php"
sharepost_url = "https://traodoisub.com/mua/share/themid.php"
follow_url = "https://traodoisub.com/mua/follow/themid.php"
camxuc_url = "https://traodoisub.com/mua/reaction/themid.php"

likepost_money=20
camxuc_money=30
likepage_money=55
sharepost_money=48
follow_money=66

def buy_like_post(realid, quantitypend, album, speed, username, accountname, cookie, token, logging):
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "PHPSESSID="+cookie,
        "origin": "https://traodoisub.com",
        "referer": "https://traodoisub.com/mua/like/",
        # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    payload = {
        "id": realid, 
        "sl": quantitypend,  
        "is_album": album,  
        "speed": speed, 
        "dateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    response = requests.post(likepost_url, headers=headers, data=payload, verify=False)
    logging.info("buy_like_post response: "+ username + " - "+ str(quantitypend) + " - "+ realid)
    money=int(quantitypend)*likepage_money
    if response.status_code == 200:
        if "Mua th" in response.text: #0 cookie
            logging.info("buy_like_post success!: ")
            bonlike.update_money(username, money, 1, logging)
            bonlike.update_handle(accountname, username, realid, 1, 2, logging)
            new_xu = tds.get_xu(token, logging)
            bonlike.update_account(accountname, cookie, new_xu, 2, logging)
            bonlike.add_history(username, realid, 1, money, quantitypend, logging)
        else:
            logging.info("buy_like_post error"+ str(response.status_code))
            bonlike.update_handle(accountname, username, realid, 1, 4, logging)
            bonlike.update_money(username, money, 2, logging)
    else:
        bonlike.update_money(username, money,2, logging)
        bonlike.update_handle(accountname, username, realid, 1, 4, logging)
        logging.error("buy_like_post error: " + str(response.status_code))

def buy_cam_xuc(realid, quantity, camxuc, speed, username, accountname, cookie, token, logging):
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
        "dateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "loaicx": camxuc,  
        "speed": speed
    }
    response = requests.post(camxuc_url, headers=headers, data=payload, verify=False)
    logging.info("buy_cam_xuc: username="+ username + ", realid="+ realid + ", quantity="+ str(quantity)+ ", accountname=" + accountname)
    money=int(quantity)*camxuc_money
    if response.status_code == 200:
        if "Mua th" in response.text: #0 cookie
            logging.info("buy_cam_xuc success!:")
            bonlike.update_money(username, money, 1, logging)
            bonlike.update_handle(accountname, username, realid, 2, 2, logging)
            new_xu = tds.get_xu(token, logging)
            bonlike.update_account(accountname, cookie, new_xu, 2, logging)
            bonlike.add_history(username, realid, 2, money, quantity, logging)
        else:
            logging.info("buy_cam_xuc fail!:")
            bonlike.update_handle(accountname, username, realid, 2, 4, logging)
            bonlike.update_money(username, money, 2, logging)

    else:
        bonlike.update_handle(accountname, username, realid, 2, 4, logging)
        bonlike.update_money(username, money, 2, logging)
        logging.error("buy_cam_xuc error: " + str(response.status_code))

def buy_like_page(realid, quantity, username, accountname, cookie, token, logging):
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
    response = requests.post(likepage_url, headers=headers, data=payload, verify=False)
    logging.info("buy_like_page: username="+ username + ", realid="+ realid + ", quantity="+ str(quantity)+ ", accountname=" + accountname)
    money=int(quantity)*likepage_money
    if response.status_code == 200:
        if "Mua th" in response.text: #0 cookie
            logging.info("buy_like_page success!:")
            bonlike.update_money(username, money, 1, logging)
            idpost=tds.update_like_page_state(cookie, logging)
            bonlike.update_handle(accountname, username, realid, 3, 2, logging)
            bonlike.update_idpage(username,realid,idpost,logging)
            new_xu = tds.get_xu(token, logging)
            bonlike.update_account(accountname, cookie, new_xu, 2, logging)
            bonlike.add_history(username, realid, 3, money, quantity, logging)

        else:
            logging.info("buy_like_page fail!:")
            bonlike.update_handle(accountname, username, realid, 3, 4, logging)
            bonlike.update_money(username, money, 2, logging)

    else:
        bonlike.update_handle(accountname, username, realid, 3, 4, logging)
        bonlike.update_money(username, money, 2, logging)
        logging.error("buy_like_page error: " + str(response.status_code))

def buy_share_post(realid, quantity, username, accountname, cookie, token, logging):
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
    response = requests.post(sharepost_url, headers=headers, data=payload, verify=False)
    logging.info("buy_share_post: username="+ username + ", realid="+ realid + ", quantity="+ str(quantity)+ ", accountname=" + accountname)
    money=int(quantity)*sharepost_money
    if response.status_code == 200:
        if "Mua th" in response.text: #0 cookie
            logging.info("buy_share_post success!:")
            bonlike.update_money(username, money, 1, logging)
            bonlike.update_handle(accountname, username, realid, 4, 2, logging)
            new_xu = tds.get_xu(token, logging)
            bonlike.update_account(accountname, cookie, new_xu, 2, logging)
            bonlike.add_history(username, realid, 4, money, quantity, logging)

        else:
            logging.info("buy_share_post fail!:")
            bonlike.update_handle(accountname, username, realid, 4, 4, logging)
            bonlike.update_money(username, money, 2, logging)

    else:
        bonlike.update_handle(accountname, username, realid, 4, 4, logging)
        bonlike.update_money(username, money, 2, logging)
        logging.error("buy_share_post error: " + str(response.status_code))

def buy_follow(realid, quantity, username, accountname, cookie, token, logging):
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
    logging.info("buy_follow: username="+ username + ", realid="+ realid + ", quantity="+ str(quantity)+ ", accountname=" + accountname)
    money=int(quantity)*follow_money
    if response.status_code == 200:
        if "Mua th" in response.text: #0 cookie
            logging.info("buy_follow success!:")
            bonlike.update_money(username, money, 1, logging)
            bonlike.update_handle(accountname, username, realid, 5, 2, logging)
            new_xu = tds.get_xu(token, logging)
            bonlike.update_account(accountname, cookie, new_xu, 2, logging)
            bonlike.add_history(username, realid, 5, money, quantity, logging)

        else:
            logging.info("buy_follow fail!:")
            bonlike.update_handle(accountname, username, realid, 5, 4, logging)
            bonlike.update_money(username, money, 2, logging)

    else:
        bonlike.update_handle(accountname, username, realid, 5, 4, logging)
        bonlike.update_money(username, money, 2, logging)
        logging.error("buy_follow error: " + str(response.status_code))

