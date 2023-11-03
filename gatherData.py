import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def readFinance(tick, file = "Data\\Data.csv", agent = UserAgent().random):
    URL = f"https://finance.yahoo.com/quote/{tick}/history"
    agent = {"User-Agent" : agent}
    opt = Options()
    opt.add_argument("--headless")
    opt.add_argument('--log-level=3')
    
    driver = webdriver.Chrome(options=opt)
    driver.get(URL)

    driver.find_element("xpath", "//div[@class='M(0) O(n):f D(ib) Bd(0) dateRangeBtn O(n):f Pos(r)']").click()
    driver.find_elements("xpath", "//button[@class='Py(5px) W(45px) Fz(s) C($tertiaryColor) Cur(p) Bd Bdc($seperatorColor) Bgc($lv4BgColor) Bdc($linkColor):h Bdrs(3px)']")[-1].click()
    soup = BeautifulSoup(driver.page_source,"html.parser")
    #############################################################
    find_ = soup.find('a', {"class": "Fl(end) Mt(3px) Cur(p)"})
    downloadURL = find_['href']
    r2 = requests.get(downloadURL, headers = agent)
    with open(file, 'wb') as f:
        f.write(r2.content)

if __name__ == "__main__":
    tick = 'ROKU'
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
    readFinance(ticks, file = f"Data\\{ticks}.csv")
