# system modules
from PyQt5.QtCore import pyqtSignal, QThread
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import html
import pandas as pd
import threading
import datetime
import time
import csv

#自訂模組
sleepBreak = threading.Event()

global times

class StartThreadFunc(QThread):
    countChanged = pyqtSignal(int)

    def __init__(self, uiObj):
        QThread.__init__(self)
        self.mainUI = uiObj

    def run(self):
        companyName = []
        companyNum = []
        companyMarket = []

        doFolder = "./stock_up"
        doCSV = "./stocklist_up.csv"

         # 取得現在年月
        date_s = format(datetime.datetime.now().strftime('%Y/%m'))
        date_string = '/'.join(date_s.split("/")[0::])

        selYear = str(date_string[0:4]) # 取得年
        if int(date_string[5:7]) < 10:
            selMonth  = str(date_string[6:7]) # 取得月
            selMonth0 = '0' + str(date_string[6:7])
        else:
            selMonth, selMonth0 = str(date_string[5:7])  # 取得月

        selMonth = '7'
        selMonth0 = '07'
        # 取得股票列表
        openPath = open(doCSV, 'rb')
        foundStockTotal = pd.read_csv(openPath)

        for x in range(len(foundStockTotal)):
            companyNum.append(str(foundStockTotal['代號'][x]))
            companyName.append(foundStockTotal['名稱'][x])
            companyMarket.append(foundStockTotal['市場'][x])

        for count in range(len(companyNum)):
            stockName = companyNum[count] + companyName[count]
            print(stockName)
            data = ["", "", "", "", "", "", "", "", ""]
            url = "http://www.tse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"

            isAccess = False
            while isAccess == False:
                try:
                    driver = webdriver.Chrome()
                    driver.implicitly_wait(4)

                    driver.get(url)

                    stockCode = driver.find_element_by_class_name("stock-code-autocomplete")
                    stockCode.clear()
                    stockCode.send_keys(companyNum[count])

                    sYear = Select(driver.find_element_by_name('yy'))
                    sYear.select_by_value(selYear)

                    sleepBreak.wait(timeout=1)
                    sMonth = Select(driver.find_element_by_name('mm'))
                    sMonth.select_by_value(selMonth)

                    driver.find_element_by_link_text("查詢").click()

                    sleepBreak.wait(timeout=1)
                    driver.current_url
                    html.encoding = "CP950"
                    soup = BeautifulSoup(driver.page_source, "html.parser")
                    table = soup.findAll('table', {'id': "report-table"})

                    isAccess = True
                except:
                    print("test1")
                    isAccess = False
                    sleepBreak.wait(timeout=3)


            sleepBreak.wait(timeout=2)

            for row in table:
                cells = row.findAll("td")
                num = 0
                tempTotal = {}
                dfStock = pd.DataFrame()

                num = len(cells) - (times*9)
                if (len(cells) != 0):
                    while num < len(cells):
                        date_string = cells[num].find(text=True).split("/")[0::]
                        data[0] = str(int(date_string[0]) + 1911) + "/" + date_string[1] + "/" + date_string[2]

                        vol_string = cells[num + 1].find(text=True).split(",")[0::]
                        if len(vol_string) == 2:
                            data[1] = str(int(int(vol_string[0] + vol_string[1]) / 1000))
                        elif len(vol_string) == 3:
                            data[1] = str(int(int(vol_string[0] + vol_string[1] + vol_string[2]) / 1000))

                        data[2] = cells[num + 2].find(text=True)
                        data[3] = cells[num + 3].find(text=True)
                        data[4] = cells[num + 4].find(text=True)
                        data[5] = cells[num + 5].find(text=True)
                        data[6] = cells[num + 6].find(text=True)
                        data[7] = cells[num + 7].find(text=True)
                        data[8] = cells[num + 8].find(text=True)

                        for num1 in range(9):
                            tempTotal[num1] = data[num1]
                        num = num + 9

                        dfStock = dfStock.append(tempTotal, ignore_index=True)

            newList = dfStock.values.tolist()

            filePath = doFolder + "/" + stockName + "/Price/Price-" + selYear + "-" + selMonth0 + ".csv"

            f1 = open(filePath, encoding='utf-8')
            foundCSV1 = pd.read_csv(f1)

            sleepBreak.wait(timeout=1)

            with open(filePath, "a", newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f, delimiter=',')
                for num2 in range(len(newList)):
                    numExist = len(foundCSV1[foundCSV1['日期'].isin([newList[num2][0]])])
                    if numExist == 0:
                        writer.writerow(newList[num2])

            nowProgrss = ((count + 1) / len(companyNum)) * 100
            self.mainUI.progressBar_loadUP.setValue(nowProgrss)

            MSG = str(count + 1) + ". " + stockName
            self.mainUI.listWidget_loadDOWN.addItem(MSG)
            sleepBreak.wait(timeout=2)

        self.mainUI.progressBar_loadUP.setValue(100)
        self.mainUI.listWidget_loadUP.addItem("===END===")

        return