{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import schedule\n",
    "import re\n",
    "import nltk\n",
    "from nltk.corpus import stopwords\n",
    "from nltk.tokenize import word_tokenize\n",
    "from nltk.probability import FreqDist\n",
    "import pandas as pd\n",
    "import os\n",
    "import requests \n",
    "from bs4 import BeautifulSoup\n",
    "import mysql.connector\n",
    "import datetime\n",
    "from datetime import datetime\n",
    "import time\n",
    "\n",
    "hindustanUrl=\"https://www.hindustantimes.com/rss/business/rssfeed.xml\"\n",
    "toiUrl=\"https://timesofindia.indiatimes.com/rssfeeds/1898055.cms\"\n",
    "economicTimesUrl=\"https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms\"\n",
    "hindubusUrl=\"https://www.thehindubusinessline.com/markets/feeder/default.rss\"\n",
    "bsUrl = \"https://www.business-standard.com/rss/markets-106.rss\"\n",
    "lmUrl = \"https://www.livemint.com/rss/markets\"\n",
    "bloomUrl = \"https://www.bloombergquint.com/stories.rss\"\n",
    "moneytopnewsUrl=\"http://www.moneycontrol.com/rss/MCtopnews.xml\"\n",
    "moneylatestnewsUrl=\"http://www.moneycontrol.com/rss/latestnews.xml\"\n",
    "moneymostpopularUrl=\"http://www.moneycontrol.com/rss/mostpopular.xml\"\n",
    "moneybusinessUrl=\"http://www.moneycontrol.com/rss/business.xml\" #description \n",
    "moneybrokerageUrl=\"http://www.moneycontrol.com/rss/brokeragerecos.xml\"\n",
    "moneybuzzingUrl=\"http://www.moneycontrol.com/rss/buzzingstocks.xml\"\n",
    "moneyecoUrl=\"http://www.moneycontrol.com/rss/economy.xml\"\n",
    "moneymrUrl=\"http://www.moneycontrol.com/rss/marketreports.xml\"\n",
    "moneyglobeUrl=\"http://www.moneycontrol.com/rss/internationalmarkets.xml\"\n",
    "moneymeUrl=\"http://www.moneycontrol.com/rss/marketedge.xml\"\n",
    "moneyoutUrl=\"http://www.moneycontrol.com/rss/marketoutlook.xml\"\n",
    "moneyrUrl=\"http://www.moneycontrol.com/rss/results.xml\"\n",
    "#tickertapeUrl=\"https://api.tickertape.in/stocks/feed/+\"TCS\"+?count=11&offset=0&types=news-article,opinion-article\"\n",
    "\n",
    "\n",
    "\n",
    "def loop():\n",
    "            global a\n",
    "            a=datetime.now().time()\n",
    "            mydb = mysql.connector.connect(host = \"localhost\",user=\"root\",passwd=\"root\",database=\"news\")\n",
    "            mycursor = mydb.cursor()\n",
    " \n",
    "\n",
    "            hindResp=requests.get(hindustanUrl)\n",
    "            toiResp=requests.get(toiUrl)\n",
    "            economicResp = requests.get(economicTimesUrl)\n",
    "            hindubusResp = requests.get(hindubusUrl)\n",
    "            bsResp = requests.get(bsUrl) \n",
    "            lmResp = requests.get(lmUrl)\n",
    "            bloomResp = requests.get(bloomUrl)\n",
    "            moneytopResp = requests.get(moneytopnewsUrl)\n",
    "            moneylatestResp = requests.get(moneylatestnewsUrl)\n",
    "            moneympResp = requests.get(moneymostpopularUrl)\n",
    "            moneybusResp = requests.get(moneybusinessUrl)\n",
    "            moneybrokResp = requests.get(moneybrokerageUrl)\n",
    "            moneybuzzResp = requests.get(moneybuzzingUrl)\n",
    "            moneyecoResp = requests.get(moneyecoUrl)\n",
    "            moneymrResp = requests.get(moneymrUrl)\n",
    "            moneyglobeResp = requests.get(moneyglobeUrl)\n",
    "            moneymeResp = requests.get(moneymeUrl)\n",
    "            moneyoutResp = requests.get(moneyoutUrl)\n",
    "            moneyrResp = requests.get(moneyrUrl)\n",
    "            \n",
    "   \n",
    "            soup1=BeautifulSoup(hindResp.content,features=\"xml\")\n",
    "            soup2=BeautifulSoup(toiResp.content,features=\"xml\")\n",
    "            soup3=BeautifulSoup(economicResp.content,features=\"xml\")\n",
    "            soup4=BeautifulSoup(hindubusResp.content,features=\"xml\")\n",
    "            soup5=BeautifulSoup(bsResp.content,features=\"xml\")        \n",
    "            soup6=BeautifulSoup(lmResp.content,features=\"xml\")   \n",
    "            soup7=BeautifulSoup(bloomResp.content,features=\"xml\")   \n",
    "            soup8=BeautifulSoup(moneytopResp.content,features=\"xml\")\n",
    "            soup9=BeautifulSoup(moneylatestResp.content,features=\"xml\")\n",
    "            soup10=BeautifulSoup(moneympResp.content,features=\"xml\")\n",
    "            soup11=BeautifulSoup(moneybusResp.content,features=\"xml\")\n",
    "            soup12=BeautifulSoup(moneybrokResp.content,features=\"xml\")\n",
    "            soup13=BeautifulSoup(moneybuzzResp.content,features=\"xml\")\n",
    "            soup14=BeautifulSoup(moneyecoResp.content,features=\"xml\")\n",
    "            soup15=BeautifulSoup(moneymrResp.content,features=\"xml\")\n",
    "            soup16=BeautifulSoup(moneyglobeResp.content,features=\"xml\")\n",
    "            soup17=BeautifulSoup(moneymeResp.content,features=\"xml\")\n",
    "            soup18=BeautifulSoup(moneyoutResp.content,features=\"xml\")\n",
    "            soup19=BeautifulSoup(moneyrResp.content,features=\"xml\")\n",
    "           \n",
    "            hindustan=soup1.findAll('item')\n",
    "            timesOfIndia=soup2.findAll('item')\n",
    "            economicTimes=soup3.findAll('item')\n",
    "            hindubus=soup4.findAll('item')\n",
    "            businessStandard=soup5.findAll('item')\n",
    "            liveMint=soup6.findAll('item')\n",
    "            bloomberg = soup7.findAll('item')\n",
    "            moneytopnews = soup8.findAll('item')\n",
    "            moneylatestnews = soup9.findAll('item')\n",
    "            moneympnews = soup10.findAll('item')\n",
    "            moneybusnews = soup11.findAll('item')\n",
    "            moneybroknews = soup12.findAll('item')\n",
    "            moneybuzznews = soup13.findAll('item')\n",
    "            moneyeconews = soup14.findAll('item')\n",
    "            moneymrnews = soup15.findAll('item')\n",
    "            moneyglobenews = soup16.findAll('item')\n",
    "            moneymenews = soup17.findAll('item')\n",
    "            moneyoutnews = soup18.findAll('item')\n",
    "            moneyrnews = soup19.findAll('item')\n",
    "   \n",
    "            hindustanTitle=[]\n",
    "            hindustanDescr=[]\n",
    "            hindustanLink=[]\n",
    "\n",
    "            hindubusTitle=[]\n",
    "            hindubusDescr=[]\n",
    "            hindubusLink=[]\n",
    "\n",
    "            toiTitle=[]\n",
    "            toiDescr=[]\n",
    "            toiLink=[]\n",
    "                        \n",
    "\n",
    "            economicTitle=[]\n",
    "            economicDescr=[]\n",
    "            economicLink=[]\n",
    "            \n",
    "            bsTitle=[]\n",
    "            bsDescr=[]\n",
    "            bsLink=[]\n",
    "\n",
    "            lmTitle=[]\n",
    "            lmDescr=[]\n",
    "            lmLink=[]\n",
    "            \n",
    "            bloomTitle=[]\n",
    "            bloomDescr=[]\n",
    "            bloomLink=[]\n",
    "            \n",
    "            moneytopTitle = []\n",
    "            moneytopDescr = []\n",
    "            moneytopLink=[]\n",
    "            \n",
    "            moneylatestTitle=[]\n",
    "            moneylatestDescr=[]\n",
    "            moneylatestLink=[]\n",
    "            \n",
    "            \n",
    "            moneympTitle=[]\n",
    "            moneympDescr=[]\n",
    "            moneympLink=[]\n",
    "            \n",
    "            moneybusTitle=[]\n",
    "            moneybusDescr=[]\n",
    "            moneybusLink=[]\n",
    "            \n",
    "            moneybrokTitle=[]\n",
    "            moneybrokDescr=[]\n",
    "            moneybrokLink=[]\n",
    "            \n",
    "            moneybuzzTitle=[]\n",
    "            moneybuzzDescr=[]\n",
    "            moneybuzzLink=[]\n",
    "            \n",
    "            moneyecoTitle=[]\n",
    "            moneyecoDescr=[]\n",
    "            moneyecoLink=[]\n",
    "            \n",
    "            moneymrTitle=[]\n",
    "            moneymrDescr=[]\n",
    "            moneymrLink=[]\n",
    "            \n",
    "            moneyglobeTitle=[]\n",
    "            moneyglobeDescr=[]\n",
    "            moneyglobeLink=[]\n",
    "            \n",
    "            moneymeTitle=[]\n",
    "            moneymeDescr=[]\n",
    "            moneymeLink=[]\n",
    "            \n",
    "            moneyoutTitle=[]\n",
    "            moneyoutDescr=[]\n",
    "            moneyoutLink=[]\n",
    "            \n",
    "            moneyrTitle=[]\n",
    "            moneyrDescr=[]\n",
    "            moneyrLink=[]\n",
    "            \n",
    "            \n",
    "            hindustanNews=[]\n",
    "            hindubusinessNews=[]\n",
    "            timesOfIndiaNews=[]\n",
    "            economicTimesNews=[]\n",
    "            businessStandardNews=[]\n",
    "            liveMintNews=[]\n",
    "            bloombergNews=[]\n",
    "            moneycontroltopNews=[]\n",
    "            moneycontrollatestNews=[]\n",
    "            moneycontrolmpNews=[]\n",
    "            moneycontrolbusNews=[]\n",
    "            moneycontrolbrokerage=[]\n",
    "            moneytopNews=[]\n",
    "            moneybuzzNews=[]\n",
    "            moneyeconomyNews=[]\n",
    "            moneymrNews=[]\n",
    "            moneyglobeNews=[]\n",
    "            moneymeNews=[]\n",
    "            moneyoutNews=[]\n",
    "            moneyrNews=[]\n",
    "\n",
    "            data1=[]\n",
    "            data2=[]\n",
    "            data3=[]\n",
    "            data4=[]\n",
    "            data5=[]\n",
    "            data6=[]\n",
    "            data7=[]\n",
    "            data8=[]\n",
    "            data9=[]\n",
    "            data10=[]\n",
    "            data11=[]\n",
    "            data12=[]\n",
    "            data13=[]\n",
    "            data14=[]\n",
    "            data15=[]\n",
    "            data16=[]\n",
    "            data17=[]\n",
    "            data18=[]\n",
    "            data19=[]\n",
    "            \n",
    "            \n",
    "            name1=\"HindustanTimes\"\n",
    "            name2=\"TimesOfIndia\"\n",
    "            name3=\"EconomicTimes\"\n",
    "            name4=\"HinduBusiness\"\n",
    "            name5=\"BusinessStandard\"\n",
    "            name6=\"LiveMint\"\n",
    "            name7=\"BloomBerg\"\n",
    "            name8=\"MoneyControl-Top-News\"\n",
    "            name9=\"MoneyControl-Latest-News\"\n",
    "            name10=\"MoneyControl-Most-Popular\"\n",
    "            name11=\"MoneyControl-Business\"\n",
    "            name12=\"MoneyControl-Brokerage-Recos\"\n",
    "            name13=\"MoneyControl-Buzzing-Stocks\"\n",
    "            name14=\"MoneyControl-ECONOMY\"\n",
    "            name15=\"MoneyControl-Market-Reports\"\n",
    "            name16=\"MoneyControl-Global-Market\"\n",
    "            name17=\"MoneyControl-Market-Edge\"\n",
    "            name18=\"MoneyControl-Market-Outlook\"\n",
    "            name19=\"MoneyControl-Results\"\n",
    "\n",
    "            \n",
    "            \n",
    "                        \n",
    "            for i in range(len(hindustan)):\n",
    "                        dum1=BeautifulSoup(hindustan[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(hindustan[i].description.text,\"html.parser\")\n",
    "                        hindustanTitle.append(dum1.text)\n",
    "                        hindustanDescr.append(dum2.text)\n",
    "                        hindustanLink.append(hindustan[i].link.text)\n",
    "\n",
    "            for i in range(len(timesOfIndia)):\n",
    "                        dum1=BeautifulSoup(timesOfIndia[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(timesOfIndia[i].description.text,\"html.parser\")\n",
    "                        toiTitle.append(dum1.text)\n",
    "                        toiDescr.append(dum2.text)\n",
    "                        toiLink.append(timesOfIndia[i].link.text)\n",
    "                        \n",
    "\n",
    "            for i in range(len(economicTimes)):\n",
    "                        dum1=BeautifulSoup(economicTimes[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(economicTimes[i].description.text,\"html.parser\")                \n",
    "                        economicTitle.append(dum1.text)\n",
    "                        economicDescr.append(dum2.text)\n",
    "                        economicLink.append(economicTimes[i].link.text)\n",
    "                        \n",
    "            for i in range(len(hindubus)):\n",
    "                        dum1=BeautifulSoup(hindubus[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(hindubus[i].description.text,\"html.parser\")                \n",
    "                        hindubusTitle.append(dum1.text)\n",
    "                        hindubusDescr.append(dum2.text)\n",
    "                        hindubusLink.append(hindubus[i].link.text)\n",
    "\n",
    "            for i in range(len(businessStandard)):\n",
    "                        dum1=BeautifulSoup(businessStandard[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(businessStandard[i].description.text,\"html.parser\")                \n",
    "                        bsTitle.append(dum1.text)\n",
    "                        bsDescr.append(dum2.text)\n",
    "                        bsLink.append(businessStandard[i].link.text)\n",
    "                        \n",
    "            for i in range(len(liveMint)):\n",
    "                        dum1=BeautifulSoup(liveMint[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(liveMint[i].description.text,\"html.parser\")                \n",
    "                        lmTitle.append(dum1.text)\n",
    "                        lmDescr.append(dum2.text)\n",
    "                        lmLink.append(liveMint[i].link.text)\n",
    "                        \n",
    "            for i in range(len(bloomberg)):\n",
    "                        dum1=BeautifulSoup(bloomberg[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(bloomberg[i].description.text,\"html.parser\")                \n",
    "                        bloomTitle.append(dum1.text)\n",
    "                        bloomDescr.append(dum2.text)\n",
    "                        bloomLink.append(bloomberg[i].link.text)\n",
    "  \n",
    "            for i in range(len(moneytopnews)):\n",
    "                        dum1=BeautifulSoup(moneytopnews[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(moneytopnews[i].description.text,\"html.parser\")                \n",
    "                        moneytopTitle.append(dum1.text)\n",
    "                        moneytopDescr.append(dum2.text)\n",
    "                        moneytopLink.append(moneytopnews[i].link.text)\n",
    "            \n",
    "\n",
    "            for i in range(len(moneylatestnews)):\n",
    "                        dum1=BeautifulSoup(moneylatestnews[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(moneylatestnews[i].description.text,\"html.parser\")                \n",
    "                        moneylatestTitle.append(dum1.text)\n",
    "                        moneylatestDescr.append(dum2.text)\n",
    "                        moneylatestLink.append(moneylatestnews[i].link.text)\n",
    "\n",
    "            for i in range(len(moneympnews)):\n",
    "                        dum1=BeautifulSoup(moneympnews[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(moneympnews[i].description.text,\"html.parser\")                \n",
    "                        moneympTitle.append(dum1.text)\n",
    "                        moneympDescr.append(dum2.text)\n",
    "                        moneympLink.append(moneympnews[i].link.text)\n",
    "\n",
    "            for i in range(len(moneybusnews)):\n",
    "                        dum1=BeautifulSoup(moneybusnews[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(moneybusnews[i].description.text,\"html.parser\")                \n",
    "                        moneybusTitle.append(dum1.text)\n",
    "                        moneybusDescr.append(dum2.text)\n",
    "                        moneybusLink.append(moneybusnews[i].link.text)\n",
    "                        \n",
    "            for i in range(len(moneybroknews)):\n",
    "                        dum1=BeautifulSoup(moneybroknews[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(moneybroknews[i].description.text,\"html.parser\")                \n",
    "                        moneybrokTitle.append(dum1.text)\n",
    "                        moneybrokDescr.append(dum2.text)\n",
    "                        moneybrokLink.append(moneybroknews[i].link.text)\n",
    "                        \n",
    "            for i in range(len(moneybuzznews)):\n",
    "                        dum1=BeautifulSoup(moneybuzznews[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(moneybuzznews[i].description.text,\"html.parser\")                \n",
    "                        moneybuzzTitle.append(dum1.text)\n",
    "                        moneybuzzDescr.append(dum2.text)\n",
    "                        moneybuzzLink.append(moneybuzznews[i].link.text)\n",
    "                        \n",
    "            for i in range(len(moneyeconews)):\n",
    "                        dum1=BeautifulSoup(moneyeconews[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(moneyeconews[i].description.text,\"html.parser\")                \n",
    "                        moneyecoTitle.append(dum1.text)\n",
    "                        moneyecoDescr.append(dum2.text)\n",
    "                        moneyecoLink.append(moneyeconews[i].link.text)\n",
    "\n",
    "            for i in range(len(moneymrnews)):\n",
    "                        dum1=BeautifulSoup(moneymrnews[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(moneymrnews[i].description.text,\"html.parser\")                \n",
    "                        moneymrTitle.append(dum1.text)\n",
    "                        moneymrDescr.append(dum2.text)\n",
    "                        moneymrLink.append(moneymrnews[i].link.text)\n",
    "                        \n",
    "            for i in range(len(moneyglobenews)):\n",
    "                        dum1=BeautifulSoup(moneyglobenews[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(moneyglobenews[i].description.text,\"html.parser\")                \n",
    "                        moneyglobeTitle.append(dum1.text)\n",
    "                        moneyglobeDescr.append(dum2.text)\n",
    "                        moneyglobeLink.append(moneyglobenews[i].link.text)\n",
    "\n",
    "            for i in range(len(moneymenews)):\n",
    "                        dum1=BeautifulSoup(moneymenews[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(moneymenews[i].description.text,\"html.parser\")                \n",
    "                        moneymeTitle.append(dum1.text)\n",
    "                        moneymeDescr.append(dum2.text)\n",
    "                        moneymeLink.append(moneymenews[i].link.text)\n",
    "\n",
    "            for i in range(len(moneyoutnews)):\n",
    "                        dum1=BeautifulSoup(moneyoutnews[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(moneyoutnews[i].description.text,\"html.parser\")                \n",
    "                        moneyoutTitle.append(dum1.text)\n",
    "                        moneyoutDescr.append(dum2.text)\n",
    "                        moneyoutLink.append(moneyoutnews[i].link.text)\n",
    "\n",
    "            for i in range(len(moneyrnews)):\n",
    "                        dum1=BeautifulSoup(moneyrnews[i].title.text,\"html.parser\")\n",
    "                        dum2=BeautifulSoup(moneyrnews[i].description.text,\"html.parser\")                \n",
    "                        moneyrTitle.append(dum1.text)\n",
    "                        moneyrDescr.append(dum2.text)\n",
    "                        moneyrLink.append(moneyrnews[i].link.text)\n",
    "                        \n",
    "            for i in range(len(hindustanTitle)):\n",
    "                        hindustanNews.append([])\n",
    "                        hindustanNews[i].append(name1)\n",
    "                        hindustanNews[i].append(hindustanTitle[i])\n",
    "                        hindustanNews[i].append(hindustanDescr[i])\n",
    "                        hindustanNews[i].append(hindustanLink[i])\n",
    "                        hindustanNews[i].append(a)\n",
    "            for i in range(len(hindustanNews)):\n",
    "                        data1.append(tuple(hindustanNews[i]))\n",
    "                                  \n",
    "            for i in range(len(toiTitle)):\n",
    "                        timesOfIndiaNews.append([])\n",
    "                        timesOfIndiaNews[i].append(name2)\n",
    "                        timesOfIndiaNews[i].append(toiTitle[i])\n",
    "                        timesOfIndiaNews[i].append(toiDescr[i])\n",
    "                        timesOfIndiaNews[i].append(toiLink[i])\n",
    "                        timesOfIndiaNews[i].append(a)\n",
    "            for i in range(len(timesOfIndiaNews)):\n",
    "                        data2.append(tuple(timesOfIndiaNews[i]))\n",
    "  \n",
    "            for i in range(len(economicTitle)):\n",
    "                        economicTimesNews.append([])\n",
    "                        economicTimesNews[i].append(name3)\n",
    "                        economicTimesNews[i].append(economicTitle[i])\n",
    "                        economicTimesNews[i].append(economicDescr[i])\n",
    "                        economicTimesNews[i].append(economicLink[i])\n",
    "                        economicTimesNews[i].append(a)\n",
    "            for i in range(len(economicTimesNews)):\n",
    "                        data3.append(tuple(economicTimesNews[i]))\n",
    "\n",
    "            for i in range(len(hindubusTitle)):\n",
    "                        hindubusinessNews.append([])\n",
    "                        hindubusinessNews[i].append(name4)\n",
    "                        hindubusinessNews[i].append(hindubusTitle[i])\n",
    "                        hindubusinessNews[i].append(hindubusDescr[i])\n",
    "                        hindubusinessNews[i].append(hindubusLink[i])\n",
    "                        hindubusinessNews[i].append(a)\n",
    "            for i in range(len(hindubusinessNews)):\n",
    "                        data4.append(tuple(hindubusinessNews[i]))\n",
    "\n",
    "            for i in range(len(bsTitle)):\n",
    "                        businessStandardNews.append([])\n",
    "                        businessStandardNews[i].append(name5)\n",
    "                        businessStandardNews[i].append(bsTitle[i])\n",
    "                        businessStandardNews[i].append(bsDescr[i])\n",
    "                        businessStandardNews[i].append(bsLink[i])\n",
    "                        businessStandardNews[i].append(a)\n",
    "            for i in range(len(businessStandardNews)):\n",
    "                        data5.append(tuple(businessStandardNews[i]))\n",
    "\n",
    "            for i in range(len(lmTitle)):\n",
    "                        liveMintNews.append([])\n",
    "                        liveMintNews[i].append(name6)\n",
    "                        liveMintNews[i].append(lmTitle[i])\n",
    "                        liveMintNews[i].append(lmDescr[i])\n",
    "                        liveMintNews[i].append(lmLink[i])\n",
    "                        liveMintNews[i].append(a)\n",
    "            for i in range(len(liveMintNews)):\n",
    "                        data6.append(tuple(liveMintNews[i]))\n",
    "\n",
    "            for i in range(len(bloomTitle)):\n",
    "                        bloombergNews.append([])\n",
    "                        bloombergNews[i].append(name7)\n",
    "                        bloombergNews[i].append(bloomTitle[i])\n",
    "                        bloombergNews[i].append(bloomDescr[i])\n",
    "                        bloombergNews[i].append(bloomLink[i])\n",
    "                        bloombergNews[i].append(a)\n",
    "            for i in range(len(bloombergNews)):\n",
    "                        data7.append(tuple(bloombergNews[i]))\n",
    "\n",
    "            for i in range(len(moneytopTitle)):\n",
    "                        moneycontroltopNews.append([])\n",
    "                        moneycontroltopNews[i].append(name8)\n",
    "                        moneycontroltopNews[i].append(moneytopTitle[i])\n",
    "                        moneycontroltopNews[i].append(moneytopDescr[i])\n",
    "                        moneycontroltopNews[i].append(moneytopLink[i])\n",
    "                        moneycontroltopNews[i].append(a)\n",
    "            for i in range(len(moneycontroltopNews)):\n",
    "                        data8.append(tuple(moneycontroltopNews[i]))\n",
    " \n",
    "            \n",
    "            for i in range(len(moneylatestTitle)):\n",
    "                        moneycontrollatestNews.append([])\n",
    "                        moneycontrollatestNews[i].append(name9)\n",
    "                        moneycontrollatestNews[i].append(moneylatestTitle[i])\n",
    "                        moneycontrollatestNews[i].append(moneylatestDescr[i])\n",
    "                        moneycontrollatestNews[i].append(moneylatestLink[i])\n",
    "                        moneycontrollatestNews[i].append(a)\n",
    "            for i in range(len(moneycontrollatestNews)):\n",
    "                        data9.append(tuple(moneycontrollatestNews[i]))\n",
    "\n",
    "            for i in range(len(moneympTitle)):\n",
    "                        moneycontrolmpNews.append([])\n",
    "                        moneycontrolmpNews[i].append(name10)\n",
    "                        moneycontrolmpNews[i].append(moneympTitle[i])\n",
    "                        moneycontrolmpNews[i].append(moneympDescr[i])\n",
    "                        moneycontrolmpNews[i].append(moneympLink[i])\n",
    "                        moneycontrolmpNews[i].append(a)\n",
    "            for i in range(len(moneycontrolmpNews)):\n",
    "                        data10.append(tuple(moneycontrolmpNews[i]))\n",
    "\n",
    "            for i in range(len(moneybusTitle)):\n",
    "                        moneycontrolbusNews.append([])\n",
    "                        moneycontrolbusNews[i].append(name11)\n",
    "                        moneycontrolbusNews[i].append(moneybusTitle[i])\n",
    "                        moneycontrolbusNews[i].append(moneybusDescr[i])\n",
    "                        moneycontrolbusNews[i].append(moneybusLink[i])\n",
    "                        moneycontrolbusNews[i].append(a)\n",
    "            for i in range(len(moneycontrolbusNews)):\n",
    "                        data11.append(tuple(moneycontrolbusNews[i]))\n",
    "\n",
    "            for i in range(len(moneybrokTitle)):\n",
    "                        moneycontrolbrokerage.append([])\n",
    "                        moneycontrolbrokerage[i].append(name12)\n",
    "                        moneycontrolbrokerage[i].append(moneybrokTitle[i])\n",
    "                        moneycontrolbrokerage[i].append(moneybrokDescr[i])\n",
    "                        moneycontrolbrokerage[i].append(moneybrokLink[i])\n",
    "                        moneycontrolbrokerage[i].append(a)\n",
    "            for i in range(len(moneycontrolbrokerage)):\n",
    "                        data12.append(tuple(moneycontrolbrokerage[i]))\n",
    "\n",
    "            for i in range(len(moneybuzzTitle)):\n",
    "                        moneybuzzNews.append([])\n",
    "                        moneybuzzNews[i].append(name13)\n",
    "                        moneybuzzNews[i].append(moneybuzzTitle[i])\n",
    "                        moneybuzzNews[i].append(moneybuzzDescr[i])\n",
    "                        moneybuzzNews[i].append(moneybuzzLink[i])\n",
    "                        moneybuzzNews[i].append(a)\n",
    "            for i in range(len(moneybuzzNews)):\n",
    "                        data13.append(tuple(moneybuzzNews[i]))\n",
    "\n",
    "            for i in range(len(moneyecoTitle)):\n",
    "                        moneyeconomyNews.append([])\n",
    "                        moneyeconomyNews[i].append(name14)\n",
    "                        moneyeconomyNews[i].append(moneyecoTitle[i])\n",
    "                        moneyeconomyNews[i].append(moneyecoDescr[i])\n",
    "                        moneyeconomyNews[i].append(moneyecoLink[i])\n",
    "                        moneyeconomyNews[i].append(a)\n",
    "            for i in range(len(moneyeconomyNews)):\n",
    "                        data14.append(tuple(moneyeconomyNews[i]))\n",
    "\n",
    "            for i in range(len(moneymrTitle)):\n",
    "                        moneymrNews.append([])\n",
    "                        moneymrNews[i].append(name15)\n",
    "                        moneymrNews[i].append(moneymrTitle[i])\n",
    "                        moneymrNews[i].append(moneymrDescr[i])\n",
    "                        moneymrNews[i].append(moneymrLink[i])\n",
    "                        moneymrNews[i].append(a)\n",
    "            for i in range(len(moneymrNews)):\n",
    "                        data15.append(tuple(moneymrNews[i]))\n",
    "\n",
    "            for i in range(len(moneyglobeTitle)):\n",
    "                        moneyglobeNews.append([])\n",
    "                        moneyglobeNews[i].append(name16)\n",
    "                        moneyglobeNews[i].append(moneyglobeTitle[i])\n",
    "                        moneyglobeNews[i].append(moneyglobeDescr[i])\n",
    "                        moneyglobeNews[i].append(moneyglobeLink[i])\n",
    "                        moneyglobeNews[i].append(a)\n",
    "            for i in range(len(moneyglobeNews)):\n",
    "                        data16.append(tuple(moneyglobeNews[i]))\n",
    "\n",
    "            for i in range(len(moneymeTitle)):\n",
    "                        moneymeNews.append([])\n",
    "                        moneymeNews[i].append(name17)\n",
    "                        moneymeNews[i].append(moneymeTitle[i])\n",
    "                        moneymeNews[i].append(moneymeDescr[i])\n",
    "                        moneymeNews[i].append(moneymeLink[i])\n",
    "                        moneymeNews[i].append(a)\n",
    "            for i in range(len(moneymeNews)):\n",
    "                        data17.append(tuple(moneymeNews[i]))\n",
    "\n",
    "            for i in range(len(moneyoutTitle)):\n",
    "                        moneyoutNews.append([])\n",
    "                        moneyoutNews[i].append(name18)\n",
    "                        moneyoutNews[i].append(moneyoutTitle[i])\n",
    "                        moneyoutNews[i].append(moneyoutDescr[i])\n",
    "                        moneyoutNews[i].append(moneyoutLink[i])\n",
    "                        moneyoutNews[i].append(a)\n",
    "            for i in range(len(moneyoutNews)):\n",
    "                        data18.append(tuple(moneyoutNews[i]))\n",
    "\n",
    "            for i in range(len(moneyrTitle)):\n",
    "                        moneyrNews.append([])\n",
    "                        moneyrNews[i].append(name19)\n",
    "                        moneyrNews[i].append(moneyrTitle[i])\n",
    "                        moneyrNews[i].append(moneyrDescr[i])\n",
    "                        moneyrNews[i].append(moneyrLink[i])\n",
    "                        moneyrNews[i].append(a)\n",
    "            for i in range(len(moneyrNews)):\n",
    "                        data19.append(tuple(moneyrNews[i]))\n",
    "                    \n",
    "                    \n",
    "            sqlform1 = \"Insert into data(name,title,descr,link,time) values(%s,%s,%s,%s,%s)\"\n",
    "            mycursor.executemany(sqlform1,data1)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data2)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data3)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data4)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data5)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data6)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data7)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data8)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data9)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data10)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data11)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data12)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data13)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data14)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data15)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data16)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data17)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data18)\n",
    "            mydb.commit()\n",
    "            mycursor.executemany(sqlform1,data19)\n",
    "            mydb.commit() \n",
    "            \n",
    "            \n",
    "            a=datetime.now().time()\n",
    "            mydb2 = mysql.connector.connect(host = \"localhost\",user=\"root\",passwd=\"root\",database=\"news\")\n",
    "            mycursor2 = mydb2.cursor()\n",
    "            freq = FreqDist()\n",
    "            stop_words = stopwords.words(\"english\")\n",
    "            punctuation = re.compile(r'[-.?!,:;()|0-9]')\n",
    "            mycursor.execute(\"select distinct title from data\")\n",
    "            myResult1= mycursor.fetchall()\n",
    "            my=[]\n",
    "            for i in range(len(myResult1)):\n",
    "                my.append(myResult1[i][0].lower())\n",
    "            dum=[]\n",
    "            tokenize=[]\n",
    "            for i in range(len(my)):\n",
    "                dum.append(word_tokenize(my[i]))\n",
    "                tokenize.extend(dum[i])\n",
    "            stopWordFilter=[]\n",
    "            for word in tokenize:\n",
    "                if word not in stop_words:\n",
    "                    stopWordFilter.append(word)        \n",
    "            post_punctuation=[]\n",
    "            for words in stopWordFilter:\n",
    "                word = punctuation.sub(\"\",words)\n",
    "                if(len(word)>0):\n",
    "                    post_punctuation.append(word)    \n",
    "            filtered=[]\n",
    "            for word in post_punctuation:\n",
    "                if(len(word)>2):\n",
    "                    filtered.append(word)\n",
    "            for word in filtered: \n",
    "                freq[word.lower()]+=1   \n",
    "            b=freq.most_common(200)\n",
    "            new=[\"sensex\",\"market\",\"crore\",\"stock\",\"stocks\",\"markets\",\"crores\",\"rupees\",\"rupee\",\"gold\",\"golds\",\"january\"\n",
    "                ,\"febrauary\",\"march\",\"april\",\"may\",\"june\",\"july\",\"august\",\"september\",\"october\",\"november\",\"december\",\n",
    "                \"lakhs\",\"lakh\",\"thousand\",\"thousands\",\"hundred\",\"hundreds\",\"share\",\"shares\",\"net\",\"price\",\"prices\",\"million\",\"billion\"]\n",
    "            c=[]\n",
    "            for i in b:\n",
    "                if(i[0] not in new):\n",
    "                    c.append(i)    \n",
    "            li=[]\n",
    "            for i in range(len(c)):\n",
    "                li.append([])\n",
    "                li[i].append(c[i][0])\n",
    "                li[i].append(c[i][1])\n",
    "            for i in range(len(li)):\n",
    "                li[i].insert(0,a)            \n",
    "            data=[]        \n",
    "            for i in range(len(li)):\n",
    "                data.append(tuple(li[i]))\n",
    "                \n",
    "            sqlform2 = \"Insert into dummy(time,name,frequency) values(%s,%s,%s)\"\n",
    "            mycursor2.executemany(sqlform2,data)\n",
    "            mydb2.commit() \n",
    "            \n",
    "            \n",
    "loop()\n",
    "\n",
    "\n",
    "schedule.every(5).minutes.do(loop)\n",
    "\n",
    "while 1:\n",
    "    schedule.run_pending()\n",
    "    time.sleep(1)\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import mysql.connector\n",
    "mydb = mysql.connector.connect(host = \"localhost\",user=\"root\",passwd=\"root\",database=\"news\")\n",
    "mycursor = mydb.cursor()\n",
    "sqlform1 = \"drop table dummy\"\n",
    "mycursor.execute(sqlform1)\n",
    "mydb.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
