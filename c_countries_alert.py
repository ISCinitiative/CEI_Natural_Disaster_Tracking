def EUROPE_REGION_ALERT(country_type=str):
    
    URL_TARGET = f"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-{country_type}"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    

    AREA_TARGET = "cap:areadesc"
    AREA_EVENT = "cap:event"
    AREA_ONSET = "cap:expires"
    AREA_URGENCY = "cap:urgency"
    
    FIND_TARGET = SOUP_TARGET.find_all(AREA_TARGET)[-1]
    FIND_EVENT = SOUP_TARGET.find_all(AREA_EVENT)[-1]
    FIND_ONSET = SOUP_TARGET.find_all(AREA_ONSET)[-1]
    FIND_URGENCY = SOUP_TARGET.find_all(AREA_URGENCY)[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TARGET: ", FIND_TARGET.text)
    print("EVENT: ", FIND_EVENT.text)
    print("ONSET: ", FIND_ONSET.text)
    print("URGENCY: ", FIND_URGENCY.text)
    print("\n")
    
    
    
  
def BRAZIL_REGION_ALERT():
    URL_TARGET = "https://apiprevmet3.inmet.gov.br/avisos/rss"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    ITEM_ALL_CLASS = SOUP_TARGET.find_all("item")
    
    i_index_c = 0
    EVENT_LIST = []
    
    for X_LOOP_DIV in ITEM_ALL_CLASS:
    
        TD_ALL = X_LOOP_DIV.find_all("td")
        
        for X_SINGLE in TD_ALL:
            i_index_c += 1
            
            if 1 < i_index_c <= 6:
                
                EVENT_LIST.append(X_SINGLE.text)
                
                
    TYPE_TARGET = EVENT_LIST[0]
    STATUS_TARGET = EVENT_LIST[1]
    FIRST_DATE_TARGET = EVENT_LIST[2]
    SECOND_DATE_TARGET = EVENT_LIST[3]
    INFO_DATE = EVENT_LIST[4]
    
    time.sleep(0.8)
    print("\n")
    print("TARGET: ", TYPE_TARGET)
    print("STATUS: ", STATUS_TARGET)
    print("FIRST DATE: ", FIRST_DATE_TARGET)
    print("SECOND DATE: ", SECOND_DATE_TARGET)
    print("INFO: ", INFO_DATE)
    print("\n")



def CHINA_REGION_ALERT():
    URL_TARGET = "http://alert-feed.worldweather.org/cn-cma-xx/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
            
    
    DATE_EVENT = EVENT_LIST[-1]
    DESCRIPTION_EVENT = EVENT_LIST[-6]
    TYPE_EVENT = EVENT_LIST[0]
    
    time.sleep(0.8)
    print("\n")
    print("DATE: ", DATE_EVENT)
    print("DESCRIPTION: ", DESCRIPTION_EVENT)
    print("TYPE: ", TYPE_EVENT)
    print("\n")



def ECUADOR_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/ec-inamhi-es/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
            
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def GUYANA_REGION_ALERT():
    
    URL_TARGET = "https://hydromet.gov.gy/cap/en/alerts/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
            
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]

    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def HONG_KONG_REGION_ALERT():
    
    URL_TARGET = "https://alerts.weather.gov.hk/V1/cap_atom.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")


    AREA_URGENCY = "cap:urgency"
        
    FIND_TARGET = SOUP_TARGET.find_all("title")[-1].text
    FIND_EVENT = SOUP_TARGET.find_all(AREA_URGENCY)[-1].text
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", FIND_TARGET)
    print("DESCRIPTION: ", FIND_EVENT)
    print("\n")



def INDIA_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/in-imd-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
            
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")
    
    



def INDONESIA_REGION_ALERT():
    
    URL_TARGET = "https://signature.bmkg.go.id/alert/public/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[-2].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")
    

    
def KENYA_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/ke-kmd-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")
    


def MADAGASCAR_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/mg-meteo-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def MALAVI_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/mw-met-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def MONGOLIA_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/mn-namem-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def OMAN_REGION_TARGET():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/om-met-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def RUSSIA_REGION_ALERT():
    URL_TARGET = "https://meteoinfo.ru/hmc-output/cap/cap-feed/en/atom.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    DIV_ALL_CLASS = SOUP_TARGET.find("entry")
    
    FIND_TARGET = DIV_ALL_CLASS.find_all("summary")[-1].text
    FIND_EVENT = DIV_ALL_CLASS.find_all("dc:date")[-1].text
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", FIND_EVENT)
    print("DESCRIPTION: ", FIND_TARGET)
    print("\n")
    
    


def SAUDI_ARABIA_ALERT():
    
    URL_TARGET = "https://ncm.gov.sa/Ar/alert/Pages/feedalerts.aspx"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    TITLE_EVENT = EVENT_LIST[1]
    DESC_EVENT = EVENT_LIST[2].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")
    

    
def SOUTH_AFRICA_ALERT():
    
    URL_TARGET = "https://caps.weathersa.co.za/Home/RssFeed"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[1]
    DESC_EVENT = EVENT_LIST[2].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")
    
   
def SURINAME_AFRICA_ALERT():
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/sr-meteo-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")
    
    

def TANZANIA_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/tz-tma-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def TRINIDAD_AND_TOBAGO_ALERT():
    
    URL_TARGET = "http://metproducts.gov.tt/ttms/public/api/feed?type=rss"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)


    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[2].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def UGANDA_REGION_ALERT():
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/ug-unma-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)


    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def ZIMBABWE_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/zw-msd-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")
