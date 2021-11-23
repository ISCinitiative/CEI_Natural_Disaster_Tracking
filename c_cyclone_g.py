def get_cyclone(count_search=int):
    
    try:
    
        GDACS_TARGET = requests.get("https://www.gdacs.org/default.aspx").text
        SOUP_GDACS = BeautifulSoup(GDACS_TARGET,"html.parser")
        ALL_C_DISASTER = SOUP_GDACS.find_all("div",id="mainListTc")
        CONTROL_VALUE_LIST = []
        i_count_stop = 0
        
        
        for x_att in ALL_C_DISASTER:
            
            ALERT_DETAIL_LINK = x_att.find_all("a")
                
            for x_detail_link in ALERT_DETAIL_LINK:
                
                LINK_AFTER_SITE = str(x_detail_link.get("href"))
                SUB_TARGET = requests.get(LINK_AFTER_SITE).text
                SOUP_GDACS_FUNCTION = BeautifulSoup(SUB_TARGET,"html.parser")
                SUB_TARGET_SOUP = SOUP_GDACS_FUNCTION.find_all("div",id="alert_summary_left")
                
                if i_count_stop <= count_search:
                        
                    i_count_stop += 1
                        
                    for x_sub_target in SUB_TARGET_SOUP:
                            
                        FIND_TR_ALL = x_sub_target.find_all("td")
                            
                        for x_sub_td in FIND_TR_ALL:
                            ALL_INFO_TEXT = x_sub_td.text
                            CONTROL_VALUE_LIST.append(ALL_INFO_TEXT.replace("\n","").replace("\n",""))
                   
                        time.sleep(0.8)   
                        print("\n")
                        print("NAME: ",CONTROL_VALUE_LIST[3])
                        print("DETAIL: ",CONTROL_VALUE_LIST[5])
                        print("DETAIL: ",CONTROL_VALUE_LIST[7])
                        print("DETAIL: ",CONTROL_VALUE_LIST[11])
                        print("--"*10)
                            
                        CONTROL_VALUE_LIST = []
                        
    except:
        
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)
