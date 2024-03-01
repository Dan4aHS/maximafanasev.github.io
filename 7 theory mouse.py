import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

print(pyautogui.size())
width, height = pyautogui.size()
print(width)
print(height)

# 2 раза переместить мышку 
#for i in range(2):
    #pyautogui.moveTo(100,100, duration=0.01)
    #pyautogui.moveTo(200,100, duration=0.01)
    #pyautogui.moveTo(200,200, duration=0.01)
    #pyautogui.moveTo(100,100, duration=0.01)

print(pyautogui.position())



