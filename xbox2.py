from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import random, string, threading
import os
os.system('color 0A')
user_home = os.path.expanduser("~")
client_id_path = os.path.join(
    user_home,
    r"AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftpe\clientId.txt",
)
if os.path.exists(client_id_path):
    os.remove(client_id_path)

text = (
    "                             アカウントジェネレーター \n "
    + "\n           この黒い画面は自動で閉じます手動で閉じないでください\n"+
    "         正しく動作しない場合はもう一つのexeファイルを実行してください\n"+
    "       preset.txtを作成しあらかじめ作成する個数を設定することもできます\n\n"
)
print(text)
if os.path.isfile('preset.txt'):
    with open('preset.txt', 'r') as f:
        count = int(f.read().strip())

else:
    count = int(input("いくつ生成しますか?(最大3) >"))

name = 0
def gen():
    global name
    def randomname(n):
        randlst = [
            random.choice(string.ascii_letters + string.digits) for i in range(n)
        ]
        return "".join(randlst)
    w = randomname(10)
    name = name + 1
    browser = webdriver.Chrome()
    browser.get(
        "https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&rver=7.3.6963.0&wp=MBI_SSL&wreply=https:%2f%2faccount.xbox.com%2fja-jp%2faccountcreation%3frtc%3d1%26csrf%3diRRDbBsXHWOzqJoxX9GqJOfUcAQCvJVJSNVhpu9YR0ntJtPfRjwCMjSg4qE1UQC4yx6KIvX4cVItbVhM5kW-6bAyA7o1&id=292543&aadredir=1&contextid=8369C2F0524F361B&bk=1602012918&uiflavor=web&lic=1&mkt=ja-jp&lc=1033&uaid=3ba71ae4427e4c300da204fc26106240"
    )
    browser.implicitly_wait(20)
    browser.find_element(By.ID, "liveSwitch").click()
    browser.implicitly_wait(20)
    browser.find_element(By.ID, "usernameInput").send_keys("a" + w)
    browser.find_element(By.ID, "nextButton").click()
    browser.implicitly_wait(20)
    p = randomname(10)
    browser.find_element(By.ID, "Password").send_keys(p)
    browser.find_element(By.ID, "nextButton").click()
    f = open(f"{name}pack.txt", "a")
    f.write(f"a{w}@outlook.jp\n{p}\n")
    browser.implicitly_wait(20)
    browser.find_element(By.ID, "lastNameInput").send_keys("1")
    browser.find_element(By.ID, "firstNameInput").send_keys("1")
    browser.find_element(By.ID, "nextButton").click()
    browser.implicitly_wait(60)
    browser.find_element(By.ID, "BirthYear").send_keys("1987")
    browser.find_element(By.ID, "BirthMonth").send_keys("1")
    browser.find_element(By.ID, "BirthDay").send_keys("1")
    browser.find_element(By.ID, "nextButton").send_keys(Keys.RETURN)
    browser.implicitly_wait(60000)
    browser.find_element(By.ID, "declineButton").click()
    browser.implicitly_wait(60)
    browser.find_element(By.ID, "Cancel").click()
    browser.close()
for e in range(count):
    t = threading.Thread(target=gen)
    t.start()