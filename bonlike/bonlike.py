import requests
from datetime import datetime, timedelta, timezone
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

addaccount_url = "https://bonlike.site/bonlike/server/addaccount.php"
updateaccount_url = "https://bonlike.site/bonlike/server/updateaccount.php"
getlikepost_url = "https://bonlike.site/bonlike/server/getlikepost.php"
getcookiecoin_url = "https://bonlike.site/bonlike/server/getcookiecoin.php"
updatehandle_url = "https://bonlike.site/bonlike/server/updatehandle.php"
updatemoney_url = "https://bonlike.site/bonlike/server/updatemoney.php"
getcookieaccountname_url = "https://bonlike.site/bonlike/server/getcookieaccountname.php"
updatelikepost_url = "https://bonlike.site/bonlike/server/updatelikepost.php"
addhistory_url = "https://bonlike.site/bonlike/server/addhistory.php"
getcamxuc_url = "https://bonlike.site/bonlike/server/getcamxuc.php"
getlikepage_url = "https://bonlike.site/bonlike/server/getlikepage.php"
getsharepost_url = "https://bonlike.site/bonlike/server/getsharepost.php"
getfollow_url = "https://bonlike.site/bonlike/server/getfollow.php"
updatecamxuc_url = "https://bonlike.site/bonlike/server/updatecamxuc.php"
updatelikepage_url = "https://bonlike.site/bonlike/server/updatelikepage.php"
updatesharepost_url = "https://bonlike.site/bonlike/server/updatesharepost.php"
updatefollow_url = "https://bonlike.site/bonlike/server/updatefollow.php"
updateidpage_url = "https://bonlike.site/bonlike/server/updateidpage.php"
getidpage_url = "https://bonlike.site/bonlike/server/getidpage.php"

def add_account(accountname, password, token, logging):
    data = {
        'accountname': accountname,  
        'password': password,  
        'token': token
    }
    logging.info("add_account: accountname=" + accountname + ", password=" + password + ", token=" + token)
    response = requests.post(addaccount_url, data=data, verify=False)

    if response.status_code == 200:
        logging.info("add_account response: " + str(response.json()))
    else:
        logging.error("add_account error: " + str(response.status_code) + ", message=" + response.text)

def update_account(accountname, cookie, xu, status, logging):
    
    data = {
        'accountname': accountname,  
        'coin': xu,  
        'cookie': cookie,  
        'status': status
    }
    logging.info("update_account: accountname=" + accountname + ", cookie=" + cookie + ", xu=" + str(xu) + ", status=" + str(status))
    response = requests.post(updateaccount_url, data=data, verify=False)

    if response.status_code == 200:
        logging.info("update_account response: " + str(response.json()))
    else:
        logging.error("update_account error: " + str(response.status_code) + ", message=" + response.text)

def add_history(username, realid, type, money, quantity, logging):
    data = {
        'username': username,  
        'realid': realid,  
        'type': type,  
        'money': money,
        'quantity': quantity
    }
    logging.info("add_history: username=" + username + ", realid=" + realid + ", type=" + str(type) + ", money=" + str(money)+ ", quantity=" + str(quantity))
    response = requests.post(addhistory_url, data=data, verify=False)

    if response.status_code == 200:
        logging.info("add_history response: " + str(response.json()))
    else:
        logging.error("add_history error: " + str(response.status_code) + ", message=" + response.text)

def get_like_post(username, realid, logging):
    data = {
        'username': username,  
        'realid': realid
    }
    response = requests.post(getlikepost_url, data=data, verify=False)
    
    logging.info("get_like_post: username=" + username + ", realid=" + realid)
    if response.status_code == 200:
        logging.info("get_like_post response: " + str(response.json()))
    else:
        logging.error("get_like_post error: " + str(response.status_code) + ", message=" + response.text)
    return response.json()

def update_like_post(realid,username,amount,logging): 
    data = {
        'realid': realid,
        'username': username,
        'amount': amount  
    }
    response = requests.post(updatelikepost_url, data=data, verify=False)
    logging.info("update_like_post: username=" + username + ", realid="+ realid + ", amount="+str(amount))
    if response.status_code == 200:
        logging.info("update_like_post response: " + str(response.json()))
    else:
        logging.error("update_like_post error: " + str(response.status_code) + ", message=" + response.text)


def get_cam_xuc(username, realid, logging):
    data = {
        'username': username,  
        'realid': realid
    }
    response = requests.post(getcamxuc_url, data=data, verify=False)
    logging.info("get_cam_xuc: username=" + username +", realid="+ realid)
    if response.status_code == 200:
        logging.info("get_cam_xuc response: " + str(response.json()))
    else:
        logging.error("get_cam_xuc error: " + str(response.status_code) + ", message=" + response.text)
    return response.json()

def get_like_page(username, realid, logging):
    data = {
        'username': username,  
        'realid': realid
    }
    response = requests.post(getlikepage_url, data=data, verify=False)
    logging.info("get_like_page: username=" + username +", realid="+ realid)
    if response.status_code == 200:
        logging.info("get_like_page response: " + str(response.json()))
    else:
        logging.error("get_like_page error: " + str(response.status_code) + ", message=" + response.text)
    return response.json()

def get_share_post(username, realid, logging):
    data = {
        'username': username,  
        'realid': realid
    }
    response = requests.post(getsharepost_url, data=data, verify=False)
    logging.info("get_share_post: username=" + username +", realid="+ realid)
    if response.status_code == 200:
        logging.info("get_share_post response: " + str(response.json()))
    else:
        logging.error("get_share_post error: " + str(response.status_code) + ", message=" + response.text)
    return response.json()

def get_follow(username, realid, logging):
    data = {
        'username': username,  
        'realid': realid
    }
    response = requests.post(getfollow_url, data=data, verify=False)
    logging.info("get_follow: username=" + username +", realid="+ realid)
    if response.status_code == 200:
        logging.info("get_follow response: " + str(response.json()))
    else:
        logging.error("get_follow error: " + str(response.status_code) + ", message=" + response.text)
    return response.json()

def update_cam_xuc(realid,username,amount,logging): 
    data = {
        'realid': realid,
        'username': username,
        'amount': amount  
    }
    response = requests.post(updatecamxuc_url, data=data, verify=False)
    logging.info("update_cam_xuc: username=" + username + ", realid="+ realid + ", amount="+str(amount))
    if response.status_code == 200:
        logging.info("update_cam_xuc response: " + str(response.json()))
    else:
        logging.error("update_cam_xuc error: " + str(response.status_code) + ", message=" + response.text)

def update_like_page(realid,username,amount,logging): 
    data = {
        'realid': realid,
        'username': username,
        'amount': amount  
    }
    response = requests.post(updatelikepage_url, data=data, verify=False)
    logging.info("update_like_page: username=" + username + ", realid="+ realid + ", amount="+str(amount))
    if response.status_code == 200:
        logging.info("update_like_page response: " + str(response.json()))
    else:
        logging.error("update_like_page error: " + str(response.status_code) + ", message=" + response.text)

def update_share_post(realid,username,amount,logging): 
    data = {
        'realid': realid,
        'username': username,
        'amount': amount  
    }
    response = requests.post(updatesharepost_url, data=data, verify=False)
    logging.info("update_share_post: username=" + username + ", realid="+ realid + ", amount="+str(amount))
    if response.status_code == 200:
        logging.info("update_share_post response: " + str(response.json()))
    else:
        logging.error("update_share_post error: " + str(response.status_code) + ", message=" + response.text)

def update_follow(realid,username,amount,logging): 
    data = {
        'realid': realid,
        'username': username,
        'amount': amount  
    }
    response = requests.post(updatefollow_url, data=data, verify=False)
    logging.info("update_follow: username=" + username + ", realid="+ realid + ", amount="+str(amount))
    if response.status_code == 200:
        logging.info("update_follow response: " + str(response.json()))
    else:
        logging.error("update_follow error: " + str(response.status_code) + ", message=" + response.text)

def get_cookie_coin(coin,logging):
    data = {
        'coin': coin
    }
    response = requests.post(getcookiecoin_url,data=data, verify=False)
    logging.info("get_cookie_coin: coin=" + str(coin))
    if response.status_code == 200:
        logging.info("get_cookie_coin response: " + str(response.json()))
    else:
        logging.error("get_cookie_coin error: " + str(response.status_code) + ", message=" + response.text)
    return response.json()

def get_cookie_accountname(accountname,logging):
    data = {
        'accountname': accountname  
    }
    response = requests.post(getcookieaccountname_url, data=data, verify=False)
    logging.info("get_cookie_accountname: accountname=" + accountname)
    if response.status_code == 200:
        logging.info("get_cookie_accountname response: " + str(response.json()))
    else:
        logging.info("get_cookie_accountname error: " + str(response.status_code) + ", message=" + response.text)
    return response.json()

def update_money(username, money, type, logging): #type 1: update 2 delete
    data = {
        'username': username,  
        'money': money,
        'type': type
    }
    response = requests.post(updatemoney_url, data=data, verify=False)
    logging.info("update_money: username=" + username + ", money=" + str(money) +", type="+ str(type))
    if response.status_code == 200:
        logging.info("update_money response: " + str(response.json()))
    else:
        logging.error("update_money error: " + str(response.status_code) + ", message=" + response.text)

def update_handle(accountname, username, realid, type, status, logging):
    data = {
        'accountname': accountname,  
        'username': username,  
        'realid': realid,  
        'type': type,   
        'status': status
    }
    response = requests.post(updatehandle_url, data=data, verify=False)
    logging.info("update_handle: accountname="+ accountname + ", username="+ username+", realid="+ realid+", type: "+str(type)+", status: " + str(status))
    if response.status_code == 200:
        logging.info("update_handle response: " + str(response.json()))
    else:
        logging.error("update_handle error: " + str(response.status_code) + ", message=" + response.text)


def update_idpage(username,realid,idpost,logging):
    data = {
        'username': username,  
        'realid': realid, 
        'idpost': idpost
    }
    response = requests.post(updateidpage_url, data=data, verify=False)
    logging.info("update_idpage: username="+ username+", realid="+ realid+", idpost="+idpost)
    if response.status_code == 200:
        logging.info("update_idpage response: " + str(response.json()))
    else:
        logging.error("update_idpage error: " + str(response.status_code) + ", message=" + response.text)
    

def get_idpage(username,realid,logging):
    data = {
        'username': username,  
        'realid': realid
    }
    response = requests.post(getidpage_url, data=data, verify=False)
    logging.info("get_idpage: username="+ username+", realid="+ realid)
    if response.status_code == 200:
        logging.info("get_idpage response: " + str(response.json()))
    else:
        logging.error("get_idpage error: " + str(response.status_code) + ", message=" + response.text)
    return response.json()