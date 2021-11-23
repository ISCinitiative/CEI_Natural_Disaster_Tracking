def get_latest_cyclone_report():
    
    TARGET_REQ_URL = "https://www.cyclocane.com/tropical-storm-risk/"
    
    try:
        
        REQ_TARGET = requests.get(TARGET_REQ_URL).text
        SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
        
        FIND_ALL_PRE = SOUP_TARGET.find_all("pre")
        
        LIST_ALL_RES = []
        for x_loop in FIND_ALL_PRE:
            
            CLEAR_OUT = x_loop.text.replace("$$","")
            LIST_ALL_RES.append(CLEAR_OUT)
            
        for x_num_in,x_list_in in enumerate(LIST_ALL_RES):
            
            time.sleep(0.8)
            print("\n")
            print(LIST_ALL_RES[x_num_in])
            print("--"*10)
            
    except:
        
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)
