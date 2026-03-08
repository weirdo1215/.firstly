"""
获取豆瓣电影新片排行榜的数据(电影名称、详细信息、评分)
豆瓣电影网址: https://movie.douban.com/chart
"""
import requests
import openpyxl
from bs4 import BeautifulSoup
import pandas
data=[]
for i in range(0,251,25):
        url=f"https://book.douban.com/top250?start=0"
        headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"
}
        res=requests.get(url=url,headers=headers)

        datares=BeautifulSoup(res.text,"html.parser")
        for tr in datares.find_all("tr",class_="item"):
            book_name=tr.find("div",class_="pl2").find("a").text.strip()
            book_score=tr.find("div",class_="star").find("span",class_="rating_nums").text
            book_word=tr.find("p",class_="quote").find("span",class_="inq").text
            d={
                "名字":book_name,
                "分数":book_score,
                "金句":book_word
             }
            data.append(d)
data_ex=pandas.DataFrame(data)
print(data_ex)
# data_ex.to_excel("豆瓣读书7.xlsx",index=False)

