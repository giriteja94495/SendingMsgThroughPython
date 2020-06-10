# if you haven't installed chromeDriveManager in your local system
# use pip install webdriver-manager and run this code
from selenium import webdriver
# we are using selenium package

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# this is for rechecking of the installation

driver.get("https://web.whatsapp.com/")
# to open the website using python script

driver.maximize_window()
# to maximize the chrome window

chat = input("Enter the contact name or the group name")
# enter the name of the contact or group name

message = input("Type in the message that you want to send")
# Enter the message you want to send

count = (int)(input("Enter how many times you want to send"))
# How many times ,the msg has to be sent

input("kEY TESTING AFTER QR CODE SCANNING")
# to intiate the process of sending ..it's just to stop running further code until the pages loads completely

user_select = driver.find_element_by_xpath("//span[@title='{}']".format(chat))
# to select contact
user_select.click()

message_block = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
# to type the msg in the msg_block of the contact

for i in range(count):
    message_block.send_keys(message)
    # click on button for every i in the range of user entered count
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

print("We did it bro yay")


#code by BILLE GIRITEJA (GITHUB:@giriteja94495)
