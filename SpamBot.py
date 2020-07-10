from pynput.keyboard import Key, Controller
import time

print("\033[1;32;40m\n")
print("""{}
 _   ___  _______  ____   ______    
| | |   ||       ||    | |      |   
| |_|   ||       | |   | |  _    |  
|       ||       | |   | | | |   |  
|___    ||      _| |   | | |_|   |  
    |   ||     |_  |   | |       |  
    |___||_______| |___| |______|   
 _______  _______  _______  __   __ 
|       ||       ||   _   ||  |_|  |
|  _____||    _  ||  |_|  ||       |
| |_____ |   |_| ||       ||       |
|_____  ||    ___||       ||       |
 _____| ||   |    |   _   || ||_|| |
|_______||___|    |__| |__||_|   |_|
 _______  _______  _______          
|  _    ||       ||       |         
| |_|   ||   _   ||_     _|         
|       ||  | |  |  |   |           
|  _   | |  |_|  |  |   |           
| |_|   ||       |  |   |           
|_______||_______|  |___|          
{}\n\tWelcome To 4C1D's Spam Bot\n\t*Ctrl + c To Stop*\n\tSubscribe To Linux Hacker On YT, And Follow linux_hacker_4c1d On IG\n{}""".format("="*100,"="*100,"="*100))                                    
message = input("Enter Your Message Here --> ")
keyboard = Controller()

time.sleep(5)

for num in range(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
	for letter in message:
		keyboard.press(letter)
		keyboard.release(letter)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	time.sleep(0.1)

