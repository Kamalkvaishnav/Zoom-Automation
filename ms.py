import schedule
import time
import webbrowser

def open_link(link):
    webbrowser.open(link)

def demo_meeting():
    open_link('https://iitgn-ac-in.zoom.us/j/8922574112')

schedule.every().monday.at("00:51").do(demo_meeting)

while 1:
    schedule.run_pending()
    time.sleep(1)
