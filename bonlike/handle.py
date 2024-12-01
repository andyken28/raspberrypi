import bonlike
import tds
import requests
import progress
from datetime import datetime, timedelta, timezone
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

likepost_coin=370
camxuc_coin=550
likepage_coin=1000
sharepost_coin=880
follow_coin=1200

def handle_like_post(status, username, realid, accountname, logging):
    if status == '1':
        rule_like_post = bonlike.get_like_post(username, realid, logging)
        quantitypend = "0"
        album = "not"
        speed = "1"
        if rule_like_post is not None:
            quantitypend = rule_like_post['quantitypend']
            coin=likepost_coin*int(quantitypend)
            if rule_like_post['album'] == '1':
                album = "ok"
            elif rule_like_post['album'] == '2':
                album = "not"
            speed = rule_like_post['speed']
            rule_cookie = bonlike.get_cookie_coin(coin, logging)
            if rule_cookie is not None:
                accountname = rule_cookie['accountname']
                cookie = rule_cookie['cookie']
                token = rule_cookie['token']
                progress.buy_like_post(realid, quantitypend, album, speed, username, accountname, cookie, token, logging)

    elif status == '2':
        cookie = bonlike.get_cookie_accountname(accountname, logging)
        if cookie is not None and cookie != "":
            logging.info("username: " + username)
            amount = tds.get_like_post_state(realid,cookie, logging)
            if amount >= 0:
                bonlike.update_like_post(realid,username,amount, logging)
            else:
                bonlike.update_like_post(realid,username,0, logging)

def handle_cam_xuc(status, username, realid, accountname, logging):
    if status == '1':
        rule_cam_xuc = bonlike.get_cam_xuc(username, realid, logging)
        quantity = "0"
        camxuc = "LOVE"
        speed = "1"
        if rule_cam_xuc is not None:
            quantity = rule_cam_xuc['quantity']
            coin=camxuc_coin*int(quantity)
            if rule_cam_xuc['camxuc'] == '1':
                camxuc = "LOVE"
            elif rule_cam_xuc['camxuc'] == '2':
                camxuc = "CARE"
            elif rule_cam_xuc['camxuc'] == '3':
                camxuc = "HAHA"
            elif rule_cam_xuc['camxuc'] == '4':
                camxuc = "WOW"
            elif rule_cam_xuc['camxuc'] == '5':
                camxuc = "SAD"
            elif rule_cam_xuc['camxuc'] == '6':
                camxuc = "ANGRY"
            speed = rule_cam_xuc['speed']
            
            rule_cookie = bonlike.get_cookie_coin(coin, logging)
            if rule_cookie is not None:
                accountname = rule_cookie['accountname']
                cookie = rule_cookie['cookie']
                token = rule_cookie['token']
                progress.buy_cam_xuc(realid, quantity, camxuc, speed, username, accountname, cookie, token, logging)
    elif status == '2':
        cookie = bonlike.get_cookie_accountname(accountname, logging)
        if cookie is not None and cookie != "":
            amount = tds.get_cam_xuc_state(realid,cookie, logging)
            if amount >= 0:
                bonlike.update_cam_xuc(realid,username,amount, logging)
            else:
                bonlike.update_cam_xuc(realid,username,0, logging)


def handle_like_page(status, username, realid, accountname, logging):
    if status == '1':
        rule_like_page = bonlike.get_like_page(username, realid, logging)
        quantity = "0"
        if rule_like_page is not None:
            quantity = rule_like_page['quantitypend']
            coin=likepage_coin*int(quantity)

            rule_cookie = bonlike.get_cookie_coin(coin, logging)
            if rule_cookie is not None:
                accountname = rule_cookie['accountname']
                cookie = rule_cookie['cookie']
                token = rule_cookie['token']
                progress.buy_like_page(realid, quantity, username, accountname, cookie, token, logging)
    elif status == '2':
        cookie = bonlike.get_cookie_accountname(accountname, logging)
        if cookie is not None and cookie != "":
            idpost=bonlike.get_idpage(username,realid,logging)
            if idpost is not None and idpost!='' and idpost!="unknown":
                amount = tds.get_like_page_state(idpost,cookie, logging)
                if amount >= 0:
                    bonlike.update_like_page(realid,username,amount, logging)
                else:
                    bonlike.update_like_page(realid,username,0, logging)

                    
def handle_share_post(status, username, realid, accountname, logging):
    if status == '1':
        rule_share_post = bonlike.get_share_post(username, realid, logging)
        quantity = "0"
        if rule_share_post is not None:
            quantity = rule_share_post['quantitypend']
            coin=sharepost_coin*int(quantity)

            rule_cookie = bonlike.get_cookie_coin(coin, logging)
            if rule_cookie is not None:
                accountname = rule_cookie['accountname']
                cookie = rule_cookie['cookie']
                token = rule_cookie['token']
                progress.buy_share_post(realid, quantity, username, accountname, cookie, token, logging)
    elif status == '2':
        cookie = bonlike.get_cookie_accountname(accountname, logging)
        if cookie is not None and cookie != "":
            amount = tds.get_share_post_state(realid,cookie, logging)
            if amount >= 0:
                bonlike.update_share_post(realid,username,amount, logging)
            else:
                bonlike.update_share_post(realid,username,0, logging)

                    
def handle_follow(status, username, realid, accountname, logging):
    if status == '1':
        rule_follow = bonlike.get_follow(username, realid, logging)
        quantity = "0"
        if rule_follow is not None:
            quantity = rule_follow['quantitypend']
            coin=follow_coin*int(quantity)

            rule_cookie = bonlike.get_cookie_coin(coin, logging)
            if rule_cookie is not None:
                accountname = rule_cookie['accountname']
                cookie = rule_cookie['cookie']
                token = rule_cookie['token']
                progress.buy_follow(realid, quantity, username, accountname, cookie, token, logging)
    elif status == '2':
        cookie = bonlike.get_cookie_accountname(accountname, logging)
        if cookie is not None and cookie != "":
            amount = tds.get_follow_state(realid,cookie, logging)
            if amount >= 0:
                bonlike.update_follow(realid,username,amount, logging)
            else:
                bonlike.update_follow(realid,username,0, logging)