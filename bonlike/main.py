import tds
import bonlike
import progress
import requests
import handle

from datetime import datetime, timedelta, timezone
import time
import logging
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# bonlike
getaccount_url = "https://bonlike.site/bonlike/server/getaccount.php"
gethandle_url = "https://bonlike.site/bonlike/server/gethandle.php"

# Cấu hình logging
log_file = 'app.log'
logger = logging.getLogger()
handler = logging.FileHandler(log_file, mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def check_account():
    logging.info("================= check_account =================:")
    response = requests.get(getaccount_url, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data is not None:
            for account in data:
                if account['cookie'] =="" or account['status'] == '1': # status 1: create
                    new_xu = tds.get_xu(account['token'], logging)
                    new_cookie = tds.get_cookie(account['accountname'],account['password'], logging)
                    if new_cookie != "":
                        bonlike.update_account(account['accountname'], new_cookie, new_xu, 2, logging)
                else:
                    createtime = datetime.strptime(account['createtime'], '%Y-%m-%d %H:%M:%S')
                    createtime = createtime.replace(tzinfo=timezone.utc)
                    current_time = datetime.now(timezone.utc)
                    if current_time - createtime > timedelta(minutes=30):
                        new_xu = tds.get_xu(account['token'], logging)
                        new_cookie = tds.get_cookie(account['accountname'],account['password'], logging)
                        if new_cookie != "": 
                            bonlike.update_account(account['accountname'], new_cookie, new_xu, 2, logging)
    else:
        logging.error("check_account error: " + str(response.status_code))
    logging.info("==================================================")


def check_handle():
    response = requests.get(gethandle_url)
    if response.status_code == 200:
        data = response.json()
        if data is not None:
            for handle_progress in data:
                status = handle_progress['status']
                username = handle_progress['username']
                realid = handle_progress['realid']
                accountname = handle_progress['accountname']

                if handle_progress['type'] == '1':
                    handle.handle_like_post(status, username, realid, accountname, logging)
                elif handle_progress['type'] == '2':
                    handle.handle_cam_xuc(status, username, realid, accountname, logging)
                elif handle_progress['type'] == '3':
                    handle.handle_like_page(status, username, realid, accountname, logging)
                elif handle_progress['type'] == '4':
                    handle.handle_share_post(status, username, realid, accountname, logging)
                elif handle_progress['type'] == '5':
                    handle.handle_follow(status, username, realid, accountname, logging)   
    else:
        logging.info("check_handle: error: " + str(response.status_code))

timeline = 9
deletefile = 0
while True:
    deletefile=deletefile+1
    logging.info("================= Timeline =================: " + str(timeline))
    timeline=timeline+1
    if(timeline==10):
        timeline=0
        check_account()
    if(deletefile==8640):
        with open(log_file, "w"):
            pass
    check_handle()
    time.sleep(60)  
# with open(log_file, "w"):
#     pass


# bonlike.add_account('xlpior838','Euqv8','TDSQfiUjclZXZzJiOiIXZ2V2ciwiI4MDOy9WawxGeiojIyV2c1Jye')
# bonlike.add_account('0u6zzo421','iDUU9b','TDSQfiYjclZXZzJiOiIXZ2V2ciwiIxIDNvpne2UHMiojIyV2c1Jye')
# bonlike.add_account('hieubantdss8','0VV62','TDSQfiEjclZXZzJiOiIXZ2V2ciwiI4M3ckRnbhJWdllGaiojIyV2c1Jye')
# bonlike.add_account('1fkcwz724','l0RApg','TDSQfiIjclZXZzJiOiIXZ2V2ciwiI0IzN6d3YrZWMiojIyV2c1Jye')
# bonlike.add_account('1egdbx990','5AMJD','TDSQfiMjclZXZzJiOiIXZ2V2ciwiIwkTO4JGZnVWMiojIyV2c1Jye')
# bonlike.add_account('1axpm5432','XstOe','TDSQficjclZXZzJiOiIXZ2V2ciwiIyMDN10Gc4FWMiojIyV2c1Jye')

# maghinho: 
# id: 559517936603342
# sl: 20
# dateTime: 2024-10-18 0:17:53

# maghinho: 
# id: 559517936603342
# sl: 20
# dateTime: 2024-10-18 0:19:47

# maghinho: 
# id: 559517936603342
# sl: 50
# dateTime: 2024-10-18 0:21:25