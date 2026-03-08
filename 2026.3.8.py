import requests
import json
import pandas
li=[727,728,729,730,731,936,1219]
d2=[]
for j in li:
    url=f"https://act-api-takumi-static.mihoyo.com/content_v2_user/app/16471662a82d418a/getContentList?iAppId=43&iChanId={j}&iPageSize=50&iPage=1&sLangKey=zh-cn&iOrder=6"
    headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
    res=requests.get(url=url,headers=headers)
    datajson=json.loads(res.text)

    for i in datajson["data"]["list"]:
        d={}
        d["名字"]=i["sTitle"].strip()
        d["中文配音"]=json.loads(i["sExt"])["732_5"]
        d["日语配音"]=json.loads(i["sExt"])["732_6"]
        d2.append(d)
d1_=pandas.DataFrame(d2)
d1_.to_excel("day3.8.3.xlsx",index=False)

