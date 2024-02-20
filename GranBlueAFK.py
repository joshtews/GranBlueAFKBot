from pynput.keyboard import Controller, Key
import time
import keyboard
import pyautogui

keyboard_controller = Controller()

active = False
image_search = False
last_results_check = 0

while True:  # making a loop
    time.sleep(1)

    if keyboard.is_pressed('f10'):  # if key 'q' is pressed 
        active = not active
        keyboard_controller.release('w')
        print("Bot is now active: " + str(active))
        time.sleep(2)

    if keyboard.is_pressed('f9'):  # if key 'q' is pressed
        image_search = not image_search
        print("Image search is now active: " + str(image_search))
        time.sleep(2)

    if image_search:
        try:
            # Dont check battle results if we just checked them in the last 60 seconds
            if time.time() - last_results_check < 55:
                keyboard_controller.press("w")
                continue
            keyboard_controller.release("w")
            location = pyautogui.locateOnScreen('BattleResults.png', grayscale=True, confidence=.5)
            print('image found')
            time.sleep(5)
            keyboard_controller.press(Key.enter)
            time.sleep(0.1)
            keyboard_controller.release(Key.enter)
            time.sleep(1)
            keyboard_controller.press(Key.enter)
            time.sleep(0.1)
            keyboard_controller.release(Key.enter)
            time.sleep(1)
            keyboard_controller.press(Key.enter)
            time.sleep(0.1)
            keyboard_controller.release(Key.enter)
            time.sleep(1)
            keyboard_controller.press(Key.enter)
            time.sleep(0.1)
            keyboard_controller.release(Key.enter)
            time.sleep(1)
            keyboard_controller.press(Key.enter)
            time.sleep(0.1)
            keyboard_controller.release(Key.enter)
            time.sleep(1)
            keyboard_controller.press(Key.enter)
            time.sleep(0.1)
            keyboard_controller.release(Key.enter)
            time.sleep(3)
            keyboard_controller.press(Key.enter)
            time.sleep(0.1)
            keyboard_controller.release(Key.enter)
            last_results_check = time.time()

            #Wait for second page
            print('waiting for second page')
            time.sleep(5)

            #Check afk image
            print('checking afk image')
            try:
                location = pyautogui.locateOnScreen('afkcheckcropped.png', grayscale=True, confidence=.5)
                print('image found')
                keyboard_controller.press('w')
                time.sleep(0.1)
                keyboard_controller.release('w')
                time.sleep(0.2)
                keyboard_controller.press(Key.enter)
                time.sleep(0.1)
                keyboard_controller.release(Key.enter)
                time.sleep(1)
            except pyautogui.ImageNotFoundException:
                print('ImageNotFoundException: image not found')

            keyboard_controller.press(Key.enter)
            time.sleep(0.1)
            keyboard_controller.release(Key.enter)
            time.sleep(1)
            keyboard_controller.press(Key.enter)
            time.sleep(0.1)
            keyboard_controller.release(Key.enter)
            time.sleep(1)
            
        except pyautogui.ImageNotFoundException:
            print('ImageNotFoundException: image not found')
