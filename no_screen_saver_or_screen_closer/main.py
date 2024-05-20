import pyautogui
import time

num_clicks = 10


try:
    for i in range(1,num_clicks +1):
        pyautogui.click(50,400)
        print(f"Click {i} completed.")
        time.sleep(5)


except KeyboardInterrupt:
    print("\n Clicking interrupted by user.")
except Exception as e:
    print(f"An error occured: {e}")


print("Clicking process completed")