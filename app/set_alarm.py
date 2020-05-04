import schedule
import time
import webbrowser, os, sys

def job():
    url = "www.youtube.com/watch?v=5qap5aO4i9A"
    chrome_path = '/usr/lib/chromium-browser/chromium-browser'
    webbrowser.get(chrome_path).open(url)
    
    time.sleep(10)

    #print("Alarm set for {}".format(t))
    return schedule.CancelJob


def main(h,m):
    schedule.every().day.at("{}:{}".format(h,m)).do(job)
    print("alarm successfully set")

    while True:
        schedule.run_pending()
        time.sleep(1)
