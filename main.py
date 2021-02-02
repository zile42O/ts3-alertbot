import ts3
import time
import requests
import json

#TEAMSPEAK_IP - Your server IP
#CLIENT_NAME - Name of your query client
#CLIENT_PASSWORD - Password of your query client

with ts3.query.TS3Connection("TEAMSPEAK_IP") as ts3conn:
    try:
        ts3conn.login(
            client_login_name="CLIENT_NAME",
            client_login_password="CLIENT_PASSWORD"
        )
    except ts3.query.TS3QueryError as err:
        print("Login failed:", err.resp.error["msg"])
        exit(1)
         
    ts3conn.use(sid=1)
    detected = False
    while True:        
        r = requests.get('localhost/layer4.php') # Our own API (dstat) on this VPS where is Ts3
        if r.status_code == 200:
            result = r.json()
            print (result[1])
            if result[1] > 100.0:
                if detected  == False:
                    ts3conn.gm(msg="[b][!]Security[/b] - [I]We detected an [b]DDoS[/b] attack![/I]")
                    detected = True
                    print("DDoS Detected!")
            elif detected == True and result[1] < 2.0:
                    ts3conn.gm(msg="[b][!]Security - [I]The DDoS attack is [B][COLOR=#ff0000]Stopped[/COLOR][/B][/I]")
                    detected = False
                    print("DDoS Stopped!")
        time.sleep(15.0) #15 seconds is okay, less of that is shit don't speed up the proccess..