# -*- coding: utf-8 -*-

import pyximport;pyximport.install()
import BFFFFf
from BFFFFf.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS

cl = BFFFFf.LINE()
cl.login(token="EnQUd2wXe2EbmJL4wQA0.H1Lk+IJvLIQ3rMMmhznPGa.BEtvYoI4Nq9XbYXVzdWdBm7ETml6nthZBOLW8po2/o0=")
cl.loginResult()




print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""

    [คำสั่งทั่วไป.....]

✈[ขอเพลง *ตามด้วยชื่อเพลง* ]
✈[เช็คริส = ดูรายชื่อที่ถูกแบน]
✈[เช็คแบน = เช็ค Mid คนที่ถูกแบน]
✈[ยกเชิญ1 = ยกค้างเชิญที่ละ1คน]
✈[ยกเชิญ = ยกเลิกค้างเชิญทั้งหมด]
✈[Test = ทดสอบบอทว่าใช้ได้ไหม]
✈[speed= เช็คความเร็วบอท]
✈[คท = Mid ของบอท]
✈[กลุ่ม = ข้อมูลกลุ่ม]
✈[ปิดลิ้ง = ปิดลิ้งกลุ่ม]
✈[set = ตรวจดูคำสั่ง]
✈[Bf@=แท๊กคนทั้งกลุ่ม]
✈[ใครแอบ=ตั้งเวลาปัญจุบัน]
✈[ออกมา=ดูรายชื่อคนเข้ามาอ่าน]


[[[[[คำสั่งเฉพาะ..[คนเขียน]**--]]]]]


✈[ขอเพลง *ตามด้วยชื่อเพลง* ]
✈[Bf@=แท๊กคนทั้งกลุ่ม]
✈[ใครแอบ=ตั้งเวลาปัญจุบัน]
✈[ออกมา=ดูรายชื่อคนเข้ามาอ่าน]
✈[เช็คริส = ดูรายชื่อที่ถูกแบน]
✈[เช็คแบน = เช็ค Mid คนที่ถูกแบน]
✈[ยกเชิญ1 = ยกค้างเชิญที่ละ1คน]
✈[ยกเชิญ = ยกเลิกค้างเชิญทั้งหมด]
✈[Test = ทดสอบบอทว่าใช้ได้ไหม]
✈[speed= เช็คความเร็วบอท]
✈[คท = Mid ของบอท]
✈[กลุ่ม = ข้อมูลกลุ่ม]
✈[เปิดลิ้ง = เปิดลิ้งกลุ่ม]
✈[ปิดลิ้ง = ปิดลิ้งกลุ่ม]
✈[เปลี่ยนชื่อกลุ่ม :ตามด้วยื่อกลุ่ม]
✈[แบน @ =ใส่แบล็คริส]
✈[แก้แบน @ = แก้คนติดแบน]
✈[ลิ้งกลุ่ม = ขอลิ้งกลุ่ม]
✈[เตะ = ลบคนที่ติดแบนในกลุ่ม]
✈[เตะทั้งหมด = ลบสมาชิกทั้งหมด]
✈[เตะ:mid = เตะคนนั้นออก]

[ฺBY ==  β•`BF.บั้ม•`]

"""


KAC = [cl]

mid = cl.getProfile().mid


Bots=[mid,"u49974a7c78af9f3a8fec3e1dc7c646a9"]

admin=[cl,"u49974a7c78af9f3a8fec3e1dc7c646a9"]
staff = [""]

wait = {
    'contact':True,
    'autoJoin':False,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':True,
    "lang":"JP",
    "comment":"",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"β•`BF.บั้ม•` ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "atjointicket":False,
    "Protectgr":False,
    "Protectjoin":False,
    "Protectcancl":False,
    "protectionOn":True
}

wait2 = {
    "readPoint": {},
    "readMember": {},
    "setTime": {},
    "ROM": {}
}

mimic = {
    "copy": False,
    "copy2": False,
    "status": False,
    "target": {}
}

settings = {
    "simiSimi": {}
}

res = {
    'num': {},
    'us': {},
    'au': {},
}

setTime = {}
setTime = wait2['setTime']
mulai = time.time()

blacklistFile = 'blacklist.txt'
pendinglistFile = 'pendinglist.txt'


contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus




def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def sendImageWithURL(self, to_, url):
    path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
    else:
        raise Exception('[ @ ]   Download image failure.')
    try:
        self.sendImage(to_, path)
    except Exception as e:
        raise e


def yt(query):
    with requests.session() as s:
        isi = []
        if query == "":
            query = "S1B tanysyz"
        s.headers['user-agent'] = 'CHROMEOS\t7.18.0\tChrome_OS\t1'
        url = 'http://www.youtube.com/results'
        params = {'search_query': query}
        r = s.get(url, params=params)
        soup = BeautifulSoup(r.content, 'html5lib')
        for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
        return isi


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:  # If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"', start_line + 90)
        end_content = s.find(',"ow"', start_content - 90)
        content_raw = str(s[start_content + 6:end_content - 1])
        return content_raw, end_content


# Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)  # Append all the links in the list named 'Links'
            time.sleep(0.1)  # Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items


def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name': 'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("[ @ ]    Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("[ @ ]    Done")
    print()


def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
        akh = akh + 2
        aa += """{"S":""" + json.dumps(str(strt)) + ""","E":""" + json.dumps(str(akh)) + ""","M":""" + json.dumps(
            mm) + "},"""
        strt = strt + 6
        akh = akh + 4
        bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa) - 1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n" + bb + "\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata = {'MENTION': '{"MENTIONEES":[' + aa + ']}', 'EMTVER': '4'}
    print "[ @ ]    Tag All"
    try:
        cl.sendMessage(msg)
    except Exception as error:
        print error



def waktu(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d Hour %02d Minute %02d Second' % (hours, mins, secs)

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def bot(op):
    try:
        if op.type == 0:
            return
        # ------Protect Group Kick start------#
        if op.type == 11:
            if wait["Protectgr"] == True:
                if op.param2 not in Bots:
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(DEF).kickoutFromGroup(op.param1, [op.param2])
                    random.choice(DEF).updateGroup(G)
        # ------Protect Group Kick finish-----#

        # ------Cancel Invite User start------#
        if op.type == 13:
            if wait["Protectcancl"] == True:
                if op.param2 not in Bots:
                    group = ki.getGroup(op.param1)
                    gMembMids = [contact.mid for contact in group.invitee]
                    random.choice(DEF).cancelGroupInvitation(op.param1, gMembMids)
        # ------Cancel Invite User Finish------#

        # ------Joined User Kick start------#
        if op.type == 17:
            if wait["Protectjoin"] == True:
                if op.param2 not in Bots:
                    random.choice(DEF).kickoutFromGroup(op.param1, [op.param2])

        # ------Joined User Kick start------#

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        if op.type == 15:
            random.choice(cl).sendText(op.param1, "ขอไห้คุณโชคดี")
            print op.param2 + "has left the group"

        if op.type == 17:
            group = cl.getGroup(op.param1)
            cb = Message()
            cb.to = op.param1
            cb.text = cl.getContact(op.param2).displayName + " \n\n✈ยินดีต้อนรับเข้ากลุ่ม✈\n\n " + group.name
            cl.sendMessage(cb)




#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        if op.type == 13:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == admin:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1], list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to, "error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid=" + mid + "&postId=" + "new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to, "already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to, "decided not to comment")

                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to, "deleted")


                        wait["dblack"] = False

                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to, "It is not in the black list")


                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to, "already")

                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to, "aded")


                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to, "deleted")

                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to, "It is not in the black list")

                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to, msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" +msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to, "[displayName]:\n" + contact.displayName + "\n[mid]:\n" +msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to, msg.text)
            elif msg.text is None:
                return
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Key", "help", "Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage)
                else:
                    cl.sendText(msg.to, helpt)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ", "")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to, "It can't be used besides the group.")

            elif ("เปลี่ยนชื่อกลุ่ม " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("เปลี่ยนชื่อกลุ่ม ", "")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to, "It can't be used besides the group.")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "Kick " in msg.text:
                midd = msg.text.replace("Kick ", "")
                cl.kickoutFromGroup(msg.to, [midd])

            elif "เตะ " in msg.text:
                midd = msg.text.replace("เตะ ", "")
                cl.kickoutFromGroup(msg.to, [midd])


            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ", "")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to, [midd])

            elif "เชิญ " in msg.text:
                midd = msg.text.replace("เชิญ ", "")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to, [midd])

            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            elif msg.text in ["คท"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ", "Gift"]:
                msg.contentType = 9
                msg.contentMetadata = {'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                       'PRDTYPE': 'THEME',
                                       'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["cancel", "Cancel", "ยกเชิญ"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "No one is inviting")
                        else:
                            cl.sendText(msg.to, "Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group")
                    else:
                        cl.sendText(msg.to, "Not for use less than group")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Ourl", "Link on", "เปิดลิ้ง"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "ลิ้งเปิด")
                    else:
                        cl.sendText(msg.to, "already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group")
                    else:
                        cl.sendText(msg.to, "Not for use less than group")

            elif msg.text in ["Curl", "Link off", "ปิดลิ้ง"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "ลิ้งปิด")
                    else:
                        cl.sendText(msg.to, "already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group")
                    else:
                        cl.sendText(msg.to, "Not for use less than group")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "jointicket " in msg.text.lower():
                rplace = msg.text.lower().replace("jointicket ")
                if rplace == "on":
                    wait["atjointicket"] = True
                elif rplace == "off":
                    wait["atjointicket"] = False
                cl.sendText(msg.to, "Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                links = link_re.findall(msg.text)
                n_links = []
                for l in links:
                    if l not in n_links:
                        n_links.append(l)
                for ticket_id in n_links:
                    if wait["atjointicket"] == True:
                        group = cl.findGroupByTicket(ticket_id)
                        cl.acceptGroupInvitationByTicket(group.id, ticket_id)
                        cl.sendText(msg.to, "Sukses join ke grup %s" % str(group.name))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to, "[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to, "[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group")
                    else:
                        cl.sendText(msg.to, "Not for use less than group")

            elif msg.text == "กลุ่ม":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "ปิด"
                        else:
                            u = "เปิด"
                        cl.sendText(msg.to, "[ชื่อกลุ่ม]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nสมาชิก:" + str(len(ginfo.members)) + "คน\npending:" + sinvitee + "เชิญค้างอยู่\nURL:" + u + "ลิ้งกลุ่ม")
                    else:
                        cl.sendText(msg.to, "[ชื่อกลุ่ม]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group")
                    else:
                        cl.sendText(msg.to, "Not for use less than group")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Id" == msg.text:
                cl.sendText(msg.to, msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to, mid)
            elif "Mid" == msg.text:
                cl.sendText(msg.to, mid)
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "100",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                cl.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "10",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                cl.sendMessage(msg)

            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "9",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                cl.sendMessage(msg)

            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "7",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                cl.sendMessage(msg)

            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "6",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                cl.sendMessage(msg)

            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "4",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                cl.sendMessage(msg)

            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "3",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                cl.sendMessage(msg)

            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "110",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                cl.sendMessage(msg)

            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "101",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                cl.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "247",
                    "STKPKGID": "3",
                    "STKVER": "100"}
                cl.sendMessage(msg)


            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:", "")
                cl.sendText(msg.to, "line://home/post?userMid=" + mid + "&postId=" +
                            cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                string = msg.text.replace("Cn ", "")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to, "name " + string + " done")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Mic:" in msg.text:
                mmid = msg.text.replace("Mic:", "")
                msg.contentType = 13
                msg.contentMetadata = {"mid": mmid}
                cl.sendMessage(msg)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["Contact on","K on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact on already❗")
                    else:
                        cl.sendText(msg.to,"already on❗")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
            elif msg.text in ["Contact off","K off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact off already❗")
                    else:
                        cl.sendText(msg.to,"already off。")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact off already❗")
                    else:
                        cl.sendText(msg.to,"already off❗")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Joinn on", "joinn on", "เข้ากลุ่มออน"]:
                if msg.from_ in admin:
                    if wait["Protectjoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "kick Joined Group On")
                        else:
                            cl.sendText(msg.to, "done")
                    else:
                        wait["Protectjoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "kick Joined Group On")
                        else:
                            cl.sendText(msg.to, "done")

            elif msg.text in ["Joinn off", "joinn off", "เข้ากลุ่มออฟ"]:
                if msg.from_ in admin:
                    if wait["Protectjoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "kick Joined Group Off")
                        else:
                            cl.sendText(msg.to, "done")
                    else:
                        wait["Protectjoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "kick Joined Group Off")
                        else:
                            cl.sendText(msg.to, "done")

            elif msg.text in ["Cancl on", "cancl on", "เชิญออน"]:
                if msg.from_ in admin:
                    if wait["Protectcancl"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Cancel All Invited On")
                        else:
                            cl.sendText(msg.to, "done")
                    else:
                        wait["Protectcancl"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Cancel All Invited On")
                        else:
                            cl.sendText(msg.to, "done")

            elif msg.text in ["Cancl off", "cancl off", "เชิญออฟ"]:
                if msg.from_ in admin:
                    if wait["Protectcancl"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Cancel All Invited Off")
                        else:
                            cl.sendText(msg.to, "done")
                    else:
                        wait["Protectcancl"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Cancel All Invited Off")
                        else:
                            cl.sendText(msg.to, "done")

            elif msg.text in ["Gr on", "gr on", "ลบออน"]:
                if msg.from_ in admin:
                    if wait["Protectgr"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Protect Group On")
                        else:
                            cl.sendtext(msg.to, "done")
                    else:
                        wait["Protectgr"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Protect Group On")
                        else:
                            cl.sendText(msg.to, "done")

            elif msg.text in ["Gr off", "gr off", "ลบออฟ"]:
                if msg.from_ in admin:
                    if wait["Protectgr"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Protect Group Off")
                        else:
                            cl.sendText(msg.to, "done")
                    else:
                        wait["Protectgr"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Protect Group Off")
                        else:
                            cl.sendText(msg.to, "done")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Invite cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Invite cancel:", "")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "The group of people canceled off.❗")
                        else:
                            cl.sendText(msg.to, "关了邀请拒绝。要时开请指定人数发送")
                    else:
                        num = int(strnum)
                        wait["leaveRoom"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "done..❗")
                        else:
                            cl.sendText(msg.to, strnum + "使人以下的小组用自动邀请拒绝")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "al ready on。")
                    else:
                        cl.sendText(msg.to, "价值奇怪。")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "leave on already❗")
                    else:
                        cl.sendText(msg.to, "already on❗")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Done..❗")
                    else:
                        cl.sendText(msg.to, "Done..❗")

            elif msg.text in ["Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "leave off already❗")
                    else:
                        cl.sendText(msg.to, "already off❗")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Done..❗")
                    else:
                        cl.sendText(msg.to, "要了开。")

            elif msg.text in ["Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "already on❗")
                    else:
                        cl.sendText(msg.to, "Done..❗")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Done..❗")
                    else:
                        cl.sendText(msg.to, "要了开。")

            elif msg.text in ["Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "already on❗")
                    else:
                        cl.sendText(msg.to, "Done..❗")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Done..❗")
                    else:
                        cl.sendText(msg.to, "要了关断。")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["Set"]:
                md = ""
                if wait["Protectjoin"] == True:md += "[􀔃􀆑lock􏿿  Block Join]\n"
                else:md += " [Block Join Off]\n"
                if wait["Protectgr"] == True:md += "[􀔃􀆑lock􏿿   Block Group]\n"
                else:md += " [Block Group Off]\n"
                if wait["Protectcancl"] == True:md += "[􀔃􀆑lock􏿿 Cancel All Invited]\n"
                else:md += " [Cancel All Invited Off]\n"
                if wait["contact"] == True:md += " [Contact    : on]\n"
                else:md += " [Contact    : off]\n"
                if wait["autoJoin"] == True:md += " [Auto join : on]\n"
                else:md += " [Auto join : off]\n"
                if wait["autoCancel"]["on"] == True:md += " Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else:md += " [Group cancel : off]\n"
                if wait["leaveRoom"] == True:md += " [Auto leave    : on]\n"
                else:md += " [Auto leave : off]\n"
                if wait["timeline"] == True:md += " [Share   : on]\n"
                else:md += " [Share   : off]\n"
                if wait["autoAdd"] == True:md += " [Auto add : on]\n"
                else:md += " [Auto add : off]\n"
                if wait["commentOn"] == True:md += " [Comment : on]\n"
                else:md += " [Comment : off]\n"
                cl.sendText(msg.to, md)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on..❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif msg.text in ["Clock on", "Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to, "already on❗")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2, "(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to, "done。")
            elif msg.text in ["Clock off", "Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to, "already on❗")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to, "done..❗")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Message change:" in msg.text:
                wait["message"] = msg.text.replace("Massage add change:", "")
                cl.sendText(msg.to, "The message was changed。")
            elif "Massage add:" in msg.text:
                wait["message"] = msg.text.replace("Massage add:", "")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, "done..❗")
                else:
                    cl.sendText(msg.to, "变更了信息。")
            elif msg.text in ["Check add", "Com"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, "It is Massage auto add:" + wait["message"])
                else:
                    cl.sendText(msg.to, "Bot Phet hack bot\n\n" + wait["message"])
            elif msg.text in ["言語変更", "言語變更"]:
                if wait["lang"] == "JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to, "切換中國語。")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to, "言語を日本語にしました。")
            elif "Comment change:" in msg.text:
                c = msg.text.replace("Comment change:", "")
                if c in ["", " ", "\n", None]:
                    cl.sendText(msg.to, "The character string which can't be changed。")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to, "変更しました。\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:", "")
                if c in ["", " ", "\n", None]:
                    cl.sendText(msg.to, "String that can not be changed。")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to, "changed。\n\n" + c)
            elif msg.text in ["Comment on", "コメント：オン", "コメント:on", "自動首頁留言：開"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "done。")
                    else:
                        cl.sendText(msg.to, "already on❗")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "done..❗")
                    else:
                        cl.sendText(msg.to, "要了开。")
            elif msg.text in ["Comment off", "コメント：オフ", "コメント:off", "自動首頁留言：關"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "done..❗")
                    else:
                        cl.sendText(msg.to, "already off❗")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "done。")
                    else:
                        cl.sendText(msg.to, "要了关断。")
            elif msg.text in ["Comment", "留言確認"]:
                cl.sendText(msg.to, "message changed to\n\n。" + str(wait["comment"]))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["Gurl", "ลิ้งกลุ่ม"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to, "line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group❗")
                    else:
                        cl.sendText(msg.to, "Not for use less than group❗")

            elif "Gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl得到→", "")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to, "line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to, "以小组以外不能使用")


            elif "ลิ้งกลุ่ม" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl得到→", "")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to, "line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to, "以小组以外不能使用")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["Blacklist"]:
                wait["wblack"] = True
                cl.sendText(msg.to, "add to comment bl❗")
            elif msg.text in ["Whitelist"]:
                wait["dblack"] = True
                cl.sendText(msg.to, "White to comment bl❗")
            elif msg.text in ["Cblacklist"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to, "confirmed❗")
                else:
                    cl.sendText(msg.to, "It is a black list。")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" + cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to, mc)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Name clock:" in msg.text:
                n = msg.text.replace("Name clock:", "")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to, "Last name clock❗")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to, "Name clock change done.\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2, "(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to, "Update to refresh❗")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "Bf " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Bf ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"error")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"คุณไม่ได้ไปต่อ..")


            elif msg.text in ["Kill"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list += filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to, "คุณอยู่ในรายชื่อสีดำ")
                        return
                    for jj in matched_list:
                        try:
                            klist = [cl]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to, [jj])
                            print (msg.to, [jj])
                        except:
                            pass

            elif msg.text in ["เตะ"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list += filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to, "คุณอยู่ในร่ายชื่อสีดำ")
                        return
                    for jj in matched_list:
                        try:
                            klist = [cl]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to, [jj])
                            print (msg.to, [jj])
                        except:
                            pass

            elif msg.text in ["Bfลบห้อง"]:
                        if msg.toType == 2:
                            if msg.from_ in admin:
                                print "[Command]Cleanse executing"
                                _name = msg.text.replace("Cleanse", "")
                                gs = cl.getGroup(msg.to)
                                cl.sendText(msg.to, "โชคดี**")
                                targets = []
                                for g in gs.members:
                                    if _name in g.displayName:
                                        targets.append(g.mid)
                                # --------------[Bot and Admin MID]----------------
                                targets.remove(mid)
                                # --------------[Bot and Admin MID]----------------
                                if targets == []:
                                    cl.sendText(msg.to, "Not found.")
                                else:
                                    for target in targets:
                                        try:
                                            klist = [cl]
                                            kicker = random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to, [target])
                                            print (msg.to, [g.mid])
                                        except:
                                            cl.sendText(msg.to, "Group cleansed")
                                print "[Command]Cleanse executed"
                            else:
                                cl.sendText(msg.to, "Command denied.")
                                cl.sendText(msg.to, "Admin permission required.")
                                print "[Error]Command denied - Admin permission required"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ", "")
                _kicktarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "ล้มเหลว")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f = codecs.open('st2__b.json', 'w', 'utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to, "กำลังตรวจสอบ")
                                except:
                                    cl.sendText(msg.to, "สำเร็จ")

            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @", "")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "ล้มเหลว")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f = codecs.open('st2__b.json', 'w', 'utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to, "แบน.....")

                            except:
                                cl.sendText(msg.to, "สำเร็จ")

            elif "แบน @" in msg.text:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("แบน @", "")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "ล้มเหลว")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f = codecs.open('st2__b.json', 'w', 'utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to, "แบน....")
                            except:
                                cl.sendText(msg.to, "สำเร็จ")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Unban]ok"
                    _name = msg.text.replace("Unban @", "")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "ล้มเหลว")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f = codecs.open('st2__b.json', 'w', 'utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to, "แก้แบน....")
                            except:
                                cl.sendText(msg.to, "สำเร็จ")

            elif "แก้แบน @" in msg.text:
                if msg.toType == 2:
                        print "[แก้แบน]ok"
                        _name = msg.text.replace("แก้แบน @", "")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "ล้มเหลว")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f = codecs.open('st2__b.json', 'w', 'utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to, "แก้แบน....")

                                except:
                                    cl.sendText(msg.to, "สำเร็จ")


            elif msg.text in ["Gcancel"]:
                try:
                    strnum = msg.text.replace("Gcancel", "")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to, "å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                            num = int(strnum)
                            wait["autoCancel"]["on"] = True
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                            else:
                                cl.sendText(msg.to, strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Value is wrong")
                        else:
                            cl.sendText(msg.to, "Bizarre ratings")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Ban", "แบนคท"]:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to, "ลง คท ต่อ....")

            elif msg.text in ["Unban", "แก้แบนคท"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to, "ลง คท ต่อ....")

            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to, "Tidak Ada user Blacklist")
                else:
                    cl.sendText(msg.to, "Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" + cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to, mc)

            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to, "ไม่มีรายชื่อสีดำ")

                else:
                    cl.sendText(msg.to, "Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]: mc += "->" + cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to, mc)

            elif msg.text in ["Me ban"]:
                    if wait["blacklist"] == {}:
                        cl.sendText(msg.to, "nothing..❗")
                    else:
                        cl.sendText(msg.to, "It is a black list❗")
                        mc = ""
                        for mi_d in wait["blacklist"]:
                            mc += "・" + cl.getContact(mi_d).displayName + "\n"
                        cl.sendText(msg.to, mc)

            elif msg.text in ["Check ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list += filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "・" + cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to, cocoa + "รายชื่อคนที่ถูกแบน..")

            elif msg.text in ["เช็คริส"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to, "กลุ่มนี้ไม่มีรายชื่อสีดำ")

                else:
                    cl.sendText(msg.to, "รายชื่อสีดำ")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" + cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to, mc)

            elif msg.text in ["Cek ban", "เช็คแบน"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list += filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to, cocoa + "")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "ชื่อ:" in msg.text:
                    string = msg.text.replace("P1name:", "")
                    if len(string.decode('utf-8')) <= 20:
                        profile = ki.getProfile()
                        profile.displayName = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to, "name " + string + " done..❗")
                        profile = kk.getProfile()
                        profile.displayName = string
                        kk.updateProfile(profile)
                        kk.sendText(msg.to, "name " + string + " done..❗")
                        profile = kc.getProfile()
                        profile.displayName = string
                        kc.updateProfile(profile)
                        kc.sendText(msg.to, "name " + string + " done..❗")
                        profile = kd.getProfile()
                        profile.displayName = string
                        kd.updateProfile(profile)
                        kd.sendText(msg.to, "name " + string + " done..❗")
                        profile = ke.getProfile()
                        profile.displayName = string
                        ke.updateProfile(profile)
                        ke.sendText(msg.to, "name " + string + " done..❗")
                        profile = kf.getProfile()
                        profile.displayName = string
                        kf.updateProfile(profile)
                        kf.sendText(msg.to, "name " + string + " done..❗")
                        profile = kg.getProfile()
                        profile.displayName = string
                        kg.updateProfile(profile)
                        kg.sendText(msg.to, "name " + string + " done..❗")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Speed" in msg.text:
                start = time.time()
                cl.sendText(msg.to, "ตรวจความเร็วบอท...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s second" % (elapsed_time))
            elif "Sp" in msg.text:
                start = time.time()
                cl.sendText(msg.to, "ตรวจความเร็วบอท...\n")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s second" % (elapsed_time))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Bf@" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members) // 100
                for j in xrange(k + 1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s = 0
                    d = []
                    for i in group.members[j * 100: (j + 1) * 100]:
                        d.append({"S": str(s), "E": str(s + 8), "M": i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION': json.dumps({"MENTIONEES": d})}
                    cl.sendMessage(msg)
                #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


            elif msg.text == "ใครแอบ":
                cl.sendText(msg.to, "ตั้งเวลาตรวจสอบคนอ่าน")
                try:
                    del wait2['readPoint'][msg.to]
                    del wait2['readMember'][msg.to]
                except:
                    pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text == "ออกมา":
                if msg.to in wait2['readPoint']:
                    if wait2["ROM"][msg.to].items() == []:
                        chiya = ""
                    else:
                        chiya = ""
                        for rom in wait2["ROM"][msg.to].items():
                            print rom
                            chiya += rom[1] + "\n"
                    cl.sendText(msg.to,
                                "รายชื่อคนอ่าน %s\n􀜁􀅔Har Har􏿿\n\nรายชื่อคนอ่าน\n%s􀜁􀅔Har Har􏿿\n\nฺํตรวจสอบ By:BFFFf\n[%s]" % (
                                wait2['readMember'][msg.to], chiya, setTime[msg.to]))
                else:
                    cl.sendText(msg.to, "ใช้คำสั่ง [ใครแอบ]ก่อนคับ")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "#終了" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:

                    pass

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["Cancelinvite1", "ยกเชิญ1"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to, [_mid])
                    cl.sendText(msg.to, "ยกเชิญเสำเร็จ..")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Steal dp @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @", "")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to, "Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Steal home @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Test" in msg.text:
                cl.sendText(msg.to, "บอท ใช้ได้ปกติ 😁")
            elif "เทส" in msg.text:
                cl.sendText(msg.to, "บอท ใช้ได้ปกติ 😁")
# -----------------------------------------------

            elif "Hi bf" in msg.text:
                cl.sendText(msg.to, "Hi 😁")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["Reject", "ลบรัน"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, "*********")
                else:
                    cl.sendText(msg.to, "拒绝了全部的邀请。")





#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "Bff#" in msg.text:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to, Ticket)
                time.sleep(0.1)
                kk.acceptGroupInvitationByTicket(msg.to, Ticket)
                time.sleep(0.1)
                kc.acceptGroupInvitationByTicket(msg.to, Ticket)
                time.sleep(0.1)
                kd.acceptGroupInvitationByTicket(msg.to, Ticket)
                time.sleep(0.1)
                print "kicker ok"
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)



# ----------------------------------------------
            elif "Bye" in msg.text:
                if msg.from_ in staff:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        print "kicker ok"
                        try:
                            ki.leaveGroup(msg.to)
                            kk.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                            kd.leaveGroup(msg.to)
                            ke.leaveGroup(msg.to)
                        except:
                            pass


            elif msg.text in ["Like", "like"]:
                if msg.from_ in admin:
                    print "[Command]Like executed"
                    cl.sendText(msg.to, "Like post")
                    try:
                        likePost()
                    except:
                        pass

            elif msg.text.lower() == 'รีเซ็ทบอท':
                print "[Commad]restart bot"
                print "Clear"
                try:
                    cl.sendText(msg.to, "ทำการรีโปรแกรมเรียบร้อย")
                    restart_program()
                except:
                    cl.sendText(msg.to, "Please wait")
                    restart_program()
                    pass



            elif "vdo:" in msg.text.lower():
                if msg.toType == 2:
                    query = msg.text.split(":")
                    try:
                        if len(query) == 3:
                            isi = yt(query[2])
                            hasil = isi[int(query[1]) - 1]
                            cl.sendText(msg.to, hasil)
                        else:
                            isi = yt(query[1])
                            cl.sendText(msg.to, isi[0])
                    except Exception as e:
                        cl.sendText(msg.to, str(e))

            elif 'ยูทูป ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ยูทูป ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                    cl.sendText(msg.to, 'https://www.youtube.com' + results['href'])
                except:
                 cl.sendText(msg.to, "มีข้อผิดพลาด")

            elif 'ขอเพลง ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ยูทูป ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                    cl.sendText(msg.to, 'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to, "มีข้อผิดพลาด")


                    #----------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
            elif "Add staff @" in msg.text:
                    if msg.from_ in admin:
                        print "[Command]Staff add executing"
                        _name = msg.text.replace("Add staff @", "")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Contact not found")
                        else:
                            for target in targets:
                                try:
                                    staff.append(target)
                                    cl.sendText(msg.to, "Added to the staff list")
                                except:
                                    pass
                        print "[Command]Staff add executed"
                    else:
                        cl.sendText(msg.to, "Command denied.")
                        cl.sendText(msg.to, "Admin permission required.")

            elif "Add Staff @" in msg.text:
                    if msg.from_ in admin:
                        print "[Command]Staff add executing"
                        _name = msg.text.replace("Add Staff @", "")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Contact not found")
                        else:
                            for target in targets:
                                try:
                                    staff.append(target)
                                    cl.sendText(msg.to, "Added to the staff list")
                                except:
                                    pass
                        print "[Command]Staff add executed"
                    else:
                        cl.sendText(msg.to, "Command denied.")
                        cl.sendText(msg.to, "Admin permission required.")

            elif "Remove Staff @" in msg.text:
                    if msg.from_ in admin:
                        print "[Command]Staff remove executing"
                        _name = msg.text.replace("Remove Staff @", "")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Contact not found")
                        else:
                            for target in targets:
                                try:
                                    staff.remove(target)
                                    cl.sendText(msg.to, "Removed to the staff list")
                                except:
                                    pass
                        print "[Command]Staff remove executed"
                    else:
                        cl.sendText(msg.to, "Command denied.")
                        cl.sendText(msg.to, "Admin permission required.")

            elif "Remove staff @" in msg.text:
                    if msg.from_ in admin:
                        print "[Command]Staff remove executing"
                        _name = msg.text.replace("Remove staff @", "")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Contact not found")
                        else:
                            for target in targets:
                                try:
                                    staff.remove(target)
                                    cl.sendText(msg.to, "Removed to the staff list")
                                except:
                                    pass
                        print "[Command]Staff remove executed"
                    else:
                        cl.sendText(msg.to, "Command denied.")
                        cl.sendText(msg.to, "Admin permission required.")

            elif msg.text in ["Stafflist", "stafflist","สตาฟริส"]:
                    if staff == []:
                        cl.sendText(msg.to, "The stafflist is empty")
                    else:
                        cl.sendText(msg.to, "Staff list:")
                        mc = ""
                        for mi_d in staff:
                            mc += "->" + cl.getContact(mi_d).displayName + "\n"
                        cl.sendText(msg.to, mc)
                        print "[Command]Stafflist executed"

# ------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        klist = [ki, kk, kc, kd]
                        kicker = random.choice(klist)
                        kicker.kickoutFromGroup(op.param1, [op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = kicker.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)



                elif op.param3 in Amid:
                    if op.param2 in Bmid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        klist = [ki, kk, kc, kd]
                        kicker = random.choice(klist)
                        kicker.kickoutFromGroup(op.param1, [op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)



                elif op.param3 in Bmid:
                    if op.param2 in Cmid:
                        G = kc.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kc.updateGroup(G)
                        Ticket = kc.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)
                    else:
                        G = kc.getGroup(op.param1)

                        klist = [ki, kk, kc, kd]
                        kicker = random.choice(klist)
                        kicker.kickoutFromGroup(op.param1, [op.param2])

                        G.preventJoinByTicket = False
                        kc.updateGroup(G)
                        Ticket = kc.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)



                elif op.param3 in Cmid:
                    if op.param2 in Dmid:
                        G = kd.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kd.updateGroup(G)
                        Ticket = kd.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kd.updateGroup(G)
                    else:
                        G = kd.getGroup(op.param1)

                        klist = [ki, kk, kc, kd]
                        kicker = random.choice(klist)
                        kicker.kickoutFromGroup(op.param1, [op.param2])

                        G.preventJoinByTicket = False
                        kd.updateGroup(G)
                        Ticket = kd.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kd.updateGroup(G)



                elif op.param3 in Dmid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        klist = [ki, kk, kc, kd]
                        kicker = random.choice(klist)
                        kicker.kickoutFromGroup(op.param1, [op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)



                #elif op.param3 in Emid:
                    #if op.param2 in Fmid:
                        #G = kf.getGroup(op.param1)
                        #G.preventJoinByTicket = False
                        #kf.updateGroup(G)
                        #Ticket = kf.reissueGroupTicket(op.param1)
                        #cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        #ki.acceptGroupInvitationByTicket(op.param1, Ticket)
#                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
 #                       kc.acceptGroupInvitationByTicket(op.param1, Ticket)
  #                      kd.acceptGroupInvitationByTicket(op.param1, Ticket)
   #                     ke.acceptGroupInvitationByTicket(op.param1, Ticket)
    #                    kf.acceptGroupInvitationByTicket(op.param1, Ticket)
     #                   kg.acceptGroupInvitationByTicket(op.param1, Ticket)
      #                  G.preventJoinByTicket = True
       #                 kf.updateGroup(G)
        #            else:
         #               G = kf.getGroup(op.param1)
#
 #                       klist = [ki, kk, kc, kd, ke, kf, kg]
  #                      kicker = random.choice(klist)
   #                     kicker.kickoutFromGroup(op.param1, [op.param2])
#
 #                       G.preventJoinByTicket = False
  #                      kf.updateGroup(G)
   ##                    cl.acceptGroupInvitationByTicket(op.param1, Ticket)
     ##                  kk.acceptGroupInvitationByTicket(op.param1, Ticket)
       #                 kc.acceptGroupInvitationByTicket(op.param1, Ticket)
         #               kd.acceptGroupInvitationByTicket(op.param1, Ticket)
        #                ke.acceptGroupInvitationByTicket(op.param1, Ticket)
          #              kf.acceptGroupInvitationByTicket(op.param1, Ticket)
           #             kg.acceptGroupInvitationByTicket(op.param1, Ticket)
            #            G.preventJoinByTicket = True
             #           kf.updateGroup(G)



              #  elif op.param3 in Fmid:
               #     if op.param2 in Gmid:
                #        G = kg.getGroup(op.param1)
                 #       G.preventJoinByTicket = False
                  #      kg.updateGroup(G)
                   #     Ticket = kg.reissueGroupTicket(op.param1)
                    #    cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                     #   ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                      #  kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                       # kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        #kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        #ke.acceptGroupInvitationByTicket(op.param1, Ticket)
                        #kf.acceptGroupInvitationByTicket(op.param1, Ticket)
                        #kg.acceptGroupInvitationByTicket(op.param1, Ticket)
                        #G.preventJoinByTicket = True
                        #kg.updateGroup(G)
#                    else:
 #                       G = kg.getGroup(op.param1)
#
 #                       klist = [ki, kk, kc, kd, ke, kf, kg]
  #                      kicker = random.choice(klist)
   #                     kicker.kickoutFromGroup(op.param1, [op.param2])
#
 #                       G.preventJoinByTicket = False
  #                      kg.updateGroup(G)
   ##                    cl.acceptGroupInvitationByTicket(op.param1, Ticket)
     #                   ki.acceptGroupInvitationByTicket(op.param1, Ticket)
      #                  kk.acceptGroupInvitationByTicket(op.param1, Ticket)
       #                 kc.acceptGroupInvitationByTicket(op.param1, Ticket)
        #                kd.acceptGroupInvitationByTicket(op.param1, Ticket)
         #               ke.acceptGroupInvitationByTicket(op.param1, Ticket)
          #              kf.acceptGroupInvitationByTicket(op.param1, Ticket)
           #             kg.acceptGroupInvitationByTicket(op.param1, Ticket)
            #            G.preventJoinByTicket = True
             #           kg.updateGroup(G)



#                elif op.param3 in Gmid:
 #                   if op.param2 in mid:
  #                      G = kk.getGroup(op.param1)
   #                     G.preventJoinByTicket = Fals
    #                    kk.updateGroup(G)
     #                   Ticket = kk.reissueGroupTicket(op.param1)
      #                  cl.acceptGroupInvitationByTicket(op.param1, Ticket)
       #                 ki.acceptGroupInvitationByTicket(op.param1, Ticket)
        #                kk.acceptGroupInvitationByTicket(op.param1, Ticket)
         #               kc.acceptGroupInvitationByTicket(op.param1, Ticket)
          #              kd.acceptGroupInvitationByTicket(op.param1, Ticket)
           #             ke.acceptGroupInvitationByTicket(op.param1, Ticket)
            #            kf.acceptGroupInvitationByTicket(op.param1, Ticket)
             #           kg.acceptGroupInvitationByTicket(op.param1, Ticket)
              #          G.preventJoinByTicket = True
               #         kk.updateGroup(G)
                #    else:
                 #       G = kk.getGroup(op.param1)
#
 #                       klist = [ki, kk, kc, kd, ke, kf, kg]
  #                      kicker = random.choice(klist)
   #                     kicker.kickoutFromGroup(op.param1, [op.param2])
#
 #                       G.preventJoinByTicket = False
  #                      kk.updateGroup(G)
   #                     Ticket = kk.reissueGroupTicket(op.param1)
    #                    kk.acceptGroupInvitationByTicket(op.param1, Ticket)
     #                   ki.acceptGroupInvitationByTicket(op.param1, Ticket)
      ##                 kc.acceptGroupInvitationByTicket(op.param1, Ticket)
        #                kd.acceptGroupInvitationByTicket(op.param1, Ticket)
         #               ke.acceptGroupInvitationByTicket(op.param1, Ticket)
          #              kf.acceptGroupInvitationByTicket(op.param1, Ticket)
           #             kg.acceptGroupInvitationByTicket(op.param1, Ticket)
            #            G.preventJoinByTicket = True
             #           kk.updateGroup(G)

            except:
                pass

#------------------------------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・" + Name
                        wait2['ROM'][op.param1][op.param2] = "・" + Name
                else:
                    cl.sendText
            except:
                pass


        if op.type == 59:
            print op


    except Exception as error:
        print error
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
def bot2(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)



        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("postEndUrl")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")

               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")

                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")


               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")

                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")

               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))

            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
# ---------------------------------------------------------------------------------------------------
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ---------------------------------------------------------------------------------------------------
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ---------------------------------------------------------------------------------------------------
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#---------------------------------------------------------------------------------------------------







            elif msg.text in ["Set"]:
                md = " "
                if wait["contact"] == True: md+=" Contact : on\n"
                else: md+=" Contact : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share : on\n"
                else:md+=" Share : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                if wait["atjointicket"] == True: md+=" Auto Join Group by Ticket : on\n"
                else:md+=" Auto Join Group by Ticket : off\n"
                cl.sendText(msg.to,md)

            elif msg.text in ["Key", "help", "Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage)
                else:
                    cl.sendText(msg.to, helpt)


            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ", "")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to, [midd])

            elif "เชิญ " in msg.text:
                midd = msg.text.replace("เชิญ ", "")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to, [midd])

            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            elif msg.text in ["คท"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ", "Gift"]:
                msg.contentType = 9
                msg.contentMetadata = {'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                       'PRDTYPE': 'THEME',
                                       'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)


            elif msg.text in ["cancel", "Cancel", "ยกเชิญ"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "No one is inviting")
                        else:
                            cl.sendText(msg.to, "Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group")
                    else:
                        cl.sendText(msg.to, "Not for use less than group")

            elif msg.text in ["Curl","Link off","ปิดลิ้ง"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ลิ้งปิด")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif "jointicket " in msg.text.lower():
                    rplace = msg.text.lower().replace("jointicket ")
                    if rplace == "on":
                        wait["atjointicket"] = True
                    elif rplace == "off":
                        wait["atjointicket"] = False
                    cl.sendText(msg.to, "Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(msg.text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        if wait["atjointicket"] == True:
                            group = cl.findGroupByTicket(ticket_id)
                            cl.acceptGroupInvitationByTicket(group.id, ticket_id)
                            cl.sendText(msg.to, "Sukses join ke grup %s" % str(group.name))

            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text == "กลุ่ม":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "ปิด"
                        else:
                            u = "เปิด"
                        cl.sendText(msg.to,"[ชื่อกลุ่ม]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nสมาชิก:" + str(len(ginfo.members)) + "คน\npending:" + sinvitee + "เชิญค้างอยู่\nURL:" + u + "ลิ้งกลุ่ม")
                    else:
                        cl.sendText(msg.to,"[ชื่อกลุ่ม]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)


            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")

            elif msg.text in ["Contact on","K on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact on already❗")
                    else:
                        cl.sendText(msg.to,"already on❗")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
            elif msg.text in ["Contact off","K off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact off already❗")
                    else:
                        cl.sendText(msg.to,"already off。")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact off already❗")
                    else:
                        cl.sendText(msg.to,"already off❗")

            elif msg.text in ["Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"leave on already❗")
                    else:
                        cl.sendText(msg.to,"already on❗")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"Done..❗")
            elif msg.text in ["Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"leave off already❗")
                    else:
                        cl.sendText(msg.to,"already off❗")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"要了开。")

            elif msg.text in ["Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"Done..❗")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"Done..❗")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"要了关断。")

            elif msg.text in ["Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on..❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"要了关断。")

            elif msg.text in ["Comment on","コメント：オン","コメント:on","自動首頁留言：開"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done。")
                    else:
                        cl.sendText(msg.to,"already on❗")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Comment off","コメント：オフ","コメント:off","自動首頁留言：關"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"already off❗")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done。")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif msg.text in ["Comment","留言確認"]:
                cl.sendText(msg.to,"message changed to\n\n。" + str(wait["comment"]))

            elif "Gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl得到→","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"以小组以外不能使用")


            elif "ลิ้งกลุ่ม" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl得到→","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"以小组以外不能使用")

            elif msg.text in ["Clock on","Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on❗")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done。")
            elif msg.text in ["Clock off","Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already on❗")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done..❗")



            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update to refresh❗")

            elif msg.text in ["Check ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list += filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "・" + cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to, cocoa + "รายชื่อคนที่ถูกแบน..")

            elif msg.text in ["เช็คริส"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to, "กลุ่มนี้ไม่มีรายชื่อสีดำ")

                else:
                    cl.sendText(msg.to, "รายชื่อสีดำ")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" + cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to, mc)

            elif msg.text in ["Cek ban", "เช็คแบน"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list += filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to, cocoa + "")



            elif msg.text in ["Test", "เทส"]:
                cl.sendText(msg.to, "บอท ใช้ได้ปกติ 😁")

#-----------------------------------------------

            elif "Hi bf" in msg.text:
                cl.sendText(msg.to, "Hi 😁")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Speed","Sp","speed"]:
                start = time.time()
                cl.sendText(msg.to, "ตรวจความเร็วบอท...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s second" % (elapsed_time))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

          #  elif msg.text == "ใครแอบ":
             #   cl.sendText(msg.to, "ตั้งเวลาตรวจสอบคนอ่าน")
          #      try:
           #         del wait2['readPoint'][msg.to]
         #           del wait2['readMember'][msg.to]
           #     except:
         #           pass
           #     now2 = datetime.now()
        #        wait2['readPoint'][msg.to] = msg.id
        #        wait2['readMember'][msg.to] = ""
         #       wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
      #          wait2['ROM'][msg.to] = {}
      #          print wait2
        #    elif msg.text == "ออกมา":
      #          if msg.to in wait2['readPoint']:
      #              if wait2["ROM"][msg.to].items() == []:
       #                 chiya = ""
         #           else:
          #              chiya = ""
            #            for rom in wait2["ROM"][msg.to].items():
             #               print rom
             #               chiya += rom[1] + "\n"
               #     cl.sendText(msg.to,
              #                  "รายชื่อคนอ่าน %s\n􀜁􀅔Har Har􏿿\n\nรายชื่อคนอ่าน\n%s􀜁􀅔Har Har􏿿\n\nฺํตรวจสอบ By:BFFFf\n[%s]" % (
              #                  wait2['readMember'][msg.to], chiya, setTime[msg.to]))
                #else:
                    #cl.sendText(msg.to, "ใช้คำสั่ง [ใครแอบ]ก่อนคับ")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


            elif "vdo:" in msg.text.lower():
                if msg.toType == 2:
                    query = msg.text.split(":")
                    try:
                        if len(query) == 3:
                            isi = yt(query[2])
                            hasil = isi[int(query[1]) - 1]
                            cl.sendText(msg.to, hasil)
                        else:
                            isi = yt(query[1])
                            cl.sendText(msg.to, isi[0])
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
            elif 'ยูทูป ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ยูทูป ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                    cl.sendText(msg.to, 'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to, "มีข้อผิดพลาด")

            elif 'ขอเพลง ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ยูทูป ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                    cl.sendText(msg.to, 'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to, "มีข้อผิดพลาด")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


            elif "Bf@" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members) // 100
                for j in xrange(k + 1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s = 0
                    d = []
                    for i in group.members[j * 100: (j + 1) * 100]:
                        d.append({"S": str(s), "E": str(s + 8), "M": i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION': json.dumps({"MENTIONEES": d})}
                    cl.sendMessage(msg)



        if op.type == 59:
            print op


    except Exception as error:
        print error
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
def likePost():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            try:
                cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
                cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by:Bf บั้ม..")
                print "Like"
            except:
                pass
            else:
                print "Not Admin or staff"


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op),bot2(Op)