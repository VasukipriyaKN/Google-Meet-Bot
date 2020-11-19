from selenium import webdriver
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains 
from twilio.rest import Client 
from playsound import playsound
from screen_recorder_sdk import screen_recorder


def msg():
  
    # Your Account Sid and Auth Token from twilio.com / console 
    account_sid = '<ACCOUNT SID>'                           #FILL HERE
    auth_token = '<TOKEN>'                                  #FILL HERE
    
    client = Client(account_sid, auth_token) 
    
    ''' Change the value of 'from' with the number  
    received from Twilio and the value of 'to' 
    with the number in which you want to send message.'''
    message = client.messages.create( 
                                from_='<CONTACT NO.>',      #FILL HERE
                                body ='<MESSAGE>',          #FILL HERE
                                to ='<CONTACT NO.>'         #FILL HERE
                            ) 
    print(message.sid)

def automsg():
    msg()
    time.sleep(5)
    element = browser.find_element_by_class_name('HKarue')
    element.click()
    time.sleep(5)
    pyautogui.write("<YOUR_NAME> Present")                      #ENTER YOUR NAME
    pyautogui.press("enter")
    playsound('<PATH ADDRESS OF RECORDED AUDIO>')               #PATH OF RECORDED AUDIO

driver = webdriver.ChromeOptions()
driver.add_argument("--incognito")

caps = driver.to_capabilities()

browser = webdriver.Chrome(desired_capabilities=caps)
browser.get('https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fwww.google.com%2F&_ga=2.27245821.19144059.1605760032-822222673.1605760032&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
time.sleep(6)
pyautogui.write("<EMAIL ID>")                                   #FILL HERE
pyautogui.press("enter")
time.sleep(2.5)
pyautogui.write("<PASSWORD>")                                   #FILL HERE
pyautogui.press("enter")
time.sleep(7)
pyautogui.press("enter")
time.sleep(10)
pyautogui.press("esc")
time.sleep(3)
pyautogui.click(x=1310, y=600)
time.sleep(5)

element = browser.find_element_by_class_name('n8i9t')
element.click()

time.sleep(0.5)
element = browser.find_element_by_class_name('aGJE1b')

if (element.get_attribute('innerHTML')=="<YOUR NAME OR ROLL NUM>"):     #TYPE ON WHAT WORDS YOU WANT TO GET NOTIFIED
    automsg()