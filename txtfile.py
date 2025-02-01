from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

words_input = []
words = []
translations = []
account = "443470944@qq.com"
pwd = "Jmd668008"
driver = webdriver.Chrome("chromedriver_130.0.6723.70.exe")
driver.minimize_window()
URL = "https://my.godic.net/Recite/userbookwords?bookid=00000000-0000-0000-0000-000000000000#popover"
name = input("单元数: ")


def set_name():
    name_fill = driver.find_element(By.CLASS_NAME, "fi-input")
    name_fill.send_keys("欧标德语教程"+name)

    save_btn = driver.find_element(By.CLASS_NAME, "achieve_btn")
    save_btn.send_keys(Keys.RETURN)


def get_wordlist():#das Heft -e
    print("开始输入单词")
    while True:
        a = input().strip()
        if a == "" or a == "Verben 动词" or a == "Adjektive 形容词" or a == "Kleine Wörter 其他词" or a == "Fragewörter 疑问词" or a == "Nomen 名词":
            continue

        if a[0] == "0" or a == "Wendungen 习惯用语":
            print("ok")
            break
        words_input.append(a)


def split_word():
    for i in range(len(words_input)):
        words.append([])
        translations.append([])
        if_word = True
        if_nomen = False

        if words_input[i][0] == "d" and (words_input[i][1] == "a" or words_input[i][1] == "e" or words_input[i][1] == "i") and (words_input[i][2] == "r" or words_input[i][2] == "s" or words_input[i][2] == "e") and words_input[i][3] == " ":
            if_nomen = True

        for j in range(len(words_input[i])):
            if if_nomen and j <= 3:
                continue
            if words_input[i][j] == "," or words_input[i][j] == "-" or words_input[i][j] == "(" or words_input[i][j] == "+":
                if_word = False
            if (words_input[i][j] == " " or 90 >= ord(words_input[i][j]) >= 65 or 122 >= ord(words_input[i][j]) >= 97 or words_input[i][j] == "," or words_input[i][j] == "-" or words_input[i][j] == "(" or words_input[i][j] == ")" or words_input[i][j] == "." or words_input[i][j] == "ö" or words_input[i][j] == "Ö" or words_input[i][j] == "ä" or words_input[i][j] == "Ä" or words_input[i][j] == "ü" or words_input[i][j] == "Ü" or words_input[i][j] == "ß" or words_input[i][j] == "+" or "9" >= words_input[i][j] >= "0" or words_input[i][j] == "/" or words_input[i][j] == "ạ" or words_input[i][j] == "ọ" or words_input[i][j] == "ị" or words_input[i][j] == "ẹ" or words_input[i][j] == "ụ") and if_word:
                if words_input[i][j] == "ạ":
                    words[i].append("a")
                    continue
                if words_input[i][j] == "ọ":
                    words[i].append("ọ")
                    continue
                if words_input[i][j] == "ị":
                    words[i].append("ị")
                    continue
                if words_input[i][j] == "ẹ":
                    words[i].append("ẹ")
                    continue
                if words_input[i][j] == "ụ":
                    words[i].append("ụ")
                    continue
                if words_input[i][j] == ",":
                    words[i].append(" ")
                    continue
                words[i].append(words_input[i][j])
            else:
                if (words_input[i][j] == " " or 90 >= ord(words_input[i][j]) >= 65 or 122 >= ord(
                        words_input[i][j]) >= 97 or words_input[i][j] == "," or words_input[i][j] == "-" or
                    words_input[i][j] == "(" or words_input[i][j] == ")" or words_input[i][j] == "." or words_input[i][
                        j] == "ö" or words_input[i][j] == "Ö" or words_input[i][j] == "ä" or words_input[i][j] == "Ä" or
                    words_input[i][j] == "ü" or words_input[i][j] == "Ü" or words_input[i][j] == "ß" or words_input[i][
                        j] == "+" or "9" >= words_input[i][j] >= "0" or words_input[i][j] == "/") and if_word:
                    continue
                translations[i].append(words_input[i][j])
                if_word = False


def login():
    driver.get(URL)
    time.sleep(1)

    account_fill = driver.find_element(By.CLASS_NAME, "input-username")
    account_fill.send_keys(account)

    pwd_fill = driver.find_element(By.CLASS_NAME, "input-password")
    pwd_fill.send_keys(pwd)

    submit_press = driver.find_element(By.CLASS_NAME, "btn-submit")
    submit_press.send_keys(Keys.RETURN)
    time.sleep(2)


def edit_txt():
    if os.path.isfile("txts/Kapitel"+name+".txt"):
        os.remove("txts/Kapitel"+name+".txt")

    with open("txts/Kapitel"+name+".txt", "a", encoding='utf-8') as f:
        #f.write("new line\n")
        for i in range(len(words)):
            for j in words[i]:
                f.write(j)

            f.write(",")

            for j in translations[i]:
                f.write(j)

            f.write("\n")


def upload_word():
    submit_btn = driver.find_element(By.CLASS_NAME, "webuploader-element-invisible")
    submit_btn.send_keys(os.getcwd() + "/txts/Kapitel" + name + ".txt")

    time.sleep(1)

    save_btn = driver.find_element(By.CLASS_NAME, "achieve_btn")
    save_btn.send_keys(Keys.RETURN)

    time.sleep(1)


def main():
    login()
    set_name()
    get_wordlist()
    split_word()
    edit_txt()
    upload_word()
    print("Finish")
    return 0


if __name__ == '__main__':
    main()

