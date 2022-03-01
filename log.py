import datetime
import os 
import time

ascii_logo = """
 _     ___ _____ _____ _     ___   ____ 
| |   |_ _|  ___| ____| |   / _ \ / ___|
| |    | || |_  |  _| | |  | | | | |  _ 
| |___ | ||  _| | |___| |__| |_| | |_| |
|_____|___|_|   |_____|_____\___/ \____|

"""

full_date = str(datetime.datetime.now())
year = full_date[:4]
month = full_date[5:][:2]
day = full_date[8:][:2]


entry_today = False
last_login = full_date

normal_text_speed = 80


def slow_print(text: str, speed: int, end_line: bool):
    text = list(text)
    for i in range(len(text)):
        print(text[i], end="", flush=True)
        time.sleep(1/speed)
    if(end_line == False):
        return
    else:
        print("")
    
def start_up():
    slow_print(ascii_logo, 200, True)
    slow_print("Initializing date and time: " + full_date[:19], normal_text_speed, True)
    log_info = open("loginfo.txt", "r")
    log_info_content = log_info.read()
    slow_print(log_info_content,normal_text_speed, True)
    print("\n\n")

    
    

def check_for_year_and_month():
    year_is = False
    month_is = False
    for i in os.listdir("./logs/"):
        if(i == year):
            year_is = True
    
    if(year_is == False):
        os.mkdir("./logs/" + year)
    
    for j in os.listdir("./logs/" + year + "/"):
        if(j == month):
            month_is = True

    if(month_is == False):
        os.mkdir("./logs/" + year + "/" + month)



def new_log(create_log, type_of_log):
    if(create_log.lower() == "y" or create_log.lower() == "yes"):
            slow_print("Enter the events of today seperated by a comma: ", normal_text_speed, False)
            events_of_today = input()
            events_of_today = events_of_today.replace(",","\n")
            check_for_year_and_month()
            day_log = open("./logs/" + year + "/" + month + "/" + day + ".txt", "w")
            day_log.write(events_of_today)

            global entry_today
            if(type_of_log == "new"):
                entry_today = True
                
    else:
        return

def daily_log_req():
    try:
        open("./logs/" + year + "/" + month + "/" + day + ".txt", "r")
        slow_print("Do you want to replace the log for today? (y/n): ", normal_text_speed, False)
        create_log = input()
        new_log(create_log, "replace")

    except:
        slow_print("Do you want to create a log for today? (y/n): ", normal_text_speed, False)
        create_log = input()
        new_log(create_log, "new")

def view_logs():
    print("\n")
    slow_print("Do you want to view a log (y/n): ",50,False)
    view_log = input()
    print("")
    if(view_log.lower() == "y" or view_log.lower() == "yes"):
        slow_print("list of available years:",50,True)
        print("")

        for i in os.listdir("./logs/"):
            slow_print(i, 50, True)
        
        print("\n")
        slow_print("Enter the year you want to view: ", 50, False)
        view_year = input()

        print("")
        slow_print("list available months:", 50, True)
        print("")

        for i in os.listdir("./logs/"+view_year+"/"):
            slow_print(i, 50, True)

        print("\n")
        slow_print("Enter the month you want to view: ", 50, False)
        view_month = input()

        print("")
        slow_print("list available days:", 50, True)
        print("")
        

        for i in os.listdir("./logs/"+view_year+"/" + view_month + "/"):
            slow_print(i.replace(".txt",""), 50, True)

        print("\n")
        slow_print("Enter the day you want to view: ", 50, False)
        view_day = input()

        print("\n")
        selected_log = open("./logs/"+view_year+"/" + view_month + "/" + view_day + ".txt", "r")
        slow_print(selected_log.read(),50,True)
    else:
        return

def set_log_info():
    log_info = open("loginfo.txt", "r")
    log_info_content = log_info.read()
    last_entry = log_info_content.split("\n")[1][12:]
    num_of_entrys = int(log_info_content.split("\n")[2][26:]) 

    if(entry_today == True):
        last_entry = full_date[:19]
        num_of_entrys = int(log_info_content.split("\n")[2][26:]) + 1
        print(num_of_entrys)
    
    open("./loginfo.txt","w").write("Last login: " + last_login + "\n" + "Last entry: " + last_entry + "\n" + "Current number of entrys: " + str(num_of_entrys))

def main():
    start_up()
    daily_log_req()
    view_logs()
    set_log_info()

if __name__ == '__main__':
    main()