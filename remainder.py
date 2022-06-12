from plyer import notification
import time 

while True:
    notification.notify(
            title = "*Drink Water!!*",
            message = "To prevent dehydration, you need to get plenty of water from drink and food every day.",
            app_icon = "D:\\Coding\\Python\\Jarvis\\drinkWater.ico",
            timeout = 5
    )
    time.sleep(5)
