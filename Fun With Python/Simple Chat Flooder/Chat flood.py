import pyautogui,time
time.sleep(5)
f=open("EnterYourScript.txt",'r')
for word in f:
    
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(5)