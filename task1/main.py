# -*- encoding: utf-8 -*-

import pandas as pd
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
import re
import time
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        press = request.form['press']
        startDate = request.form['sday']
        endDate = request.form['eday']
        pageNum = request.form['num']
        pageSize = request.form['size']
        param = [startDate, endDate]

        data = work(param)

        Data = data.copy()

        if press == '':
            final = Data
        else:
            Data = Data[Data['press'] == press]
        if pageNum == '' or pageSize == '':
            final = Data
        else:
            pageNum = int(pageNum)
            pageSize = int(pageSize)
            final = Data[(pageNum - 1) * pageSize:pageSize*pageNum]

        if len(final) != 0:
            return render_template('result.html',
                                   dateData=final['date'], categoryData=final['category'],
                                   pressData=final['press'], titleData=final['title'],
                                   documentData=final['document'], linkData=final['link'],
                                   length=len(final))
        else:
            return render_template('web.html')
    return render_template('web.html')


def work(param):
    """
    :param param:
    """
    column = ['date', 'category', 'press', 'title', 'document', 'link']
    result = pd.DataFrame(columns=column)

    # param : 시작 날짜, 종료 날짜
    if param[1] == '' or param[0] == '':
        period = 3
        periods = list(pd.date_range(datetime.today(), periods=period, freq='-1D').strftime('%Y%m%d'))
    else:
        sTime = datetime.strptime(param[0], '%Y-%m-%d')
        eTime = datetime.strptime(param[1], '%Y-%m-%d')
        periods = list(pd.date_range(sTime, eTime, freq='1D').strftime('%Y%m%d'))

    try:
        for target in periods:
            page = 1
            while True:
                source, Data = Crawling(target, page)
                result = makeDF(result, Data)

                print(f'{target}, {page} 페이지 완료')

                page += 1

                lastPage = source.find_all('a', {'class': 'nclicks(fls.page)'})[-1].get_text()

                if lastPage != '다음':
                    if lastPage == '이전' or int(lastPage) == page - 2:
                        break

    except Exception as ex:
        print(f'{ex}')

    result.to_csv('result.csv', index=False, encoding="utf-8-sig")
    print(f'CSV 추출 완료 {periods[0]} ~ {periods[-1]}')

    return result


def Crawling(target, page):
    column = ['date', 'category', 'press', 'title', 'document', 'link']
    pageData = pd.DataFrame(columns=column)

    url_main = f"https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=230&sid1=105&date={target}&page={page}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36'}
    web = requests.get(url_main, headers=headers).content

    source = BeautifulSoup(web, 'html.parser')

    urlList = source.find('div', {'class': 'list_body newsflash_body'})

    urls_list = []

    for urls in urlList.find_all('a'):
        if urls["href"].startswith("https://n.news.naver.com") and urls["href"] not in urls_list:
            urls_list.append(urls["href"])

    for url in urls_list:
        web_news = requests.get(url, headers=headers).content
        source_news = BeautifulSoup(web_news, 'html.parser')

        # 기사 날짜
        date = source_news.find('span', {'class': 'media_end_head_info_datestamp_time _ARTICLE_DATE_TIME'}).get_text()
        date = modDate(date)

        # 기사 분류
        category = source_news.find_all('em', {'class': 'media_end_categorize_item'})
        text = []
        for i in range(len(category)):
            text.append(category[i].get_text())
        category = ', '.join(text)

        # 발행 기관
        press = source_news.find('img', {'class': 'media_end_head_top_logo_img light_type'})['alt']

        # 기사 제목
        title = source_news.find('h2', {'class': 'media_end_head_headline'}).get_text()

        # 기사 내용
        article = source_news.find('div', {'id': 'newsct_article'}).get_text()

        article = modArticle(article)

        form = pd.DataFrame({
            'date': [date],
            'category': [category],
            'press': [press],
            'title': [title],
            'document': [article],
            'link': [url]
        })
        pageData = makeDF(pageData, form)

        time.sleep(5)

    return source, pageData


def modArticle(article):
    article = article.replace("\n", "")
    article = article.replace("// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}", "")
    article = article.replace("동영상 뉴스       ", "")
    article = article.replace("동영상 뉴스", "")
    article = article.strip()
    pattern = re.compile(r'\'')
    article = pattern.sub('', article)

    return article


def modDate(date):
    date = date.replace(" ", "")
    date1 = date[:11]
    date2 = date[13:]
    date3 = (lambda x: 'am' if x == '오전' else 'pm')(date[11:13])
    date4 = date1 + date2 + date3
    date = str(pd.Timestamp(date4))
    return date


def makeDF(a, b):
    if len(a) == 0:
        a = b
    else:
        a = pd.concat([a, b], ignore_index=True)
    return a


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')


if __name__ == '__main__':
    app.run(debug=True)
