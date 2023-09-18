import time #importa a data do sistema
import pyautogui
import threading
# Get instance
import instaloader
L = instaloader.Instaloader()

# Login or load session
#L.login(r'username', r'passwd')        # (login)


# Obtain profile metadata
#profile = instaloader.Profile.from_username(L.context, "$") #substituir $ por @pra ser raspado

# Print list of followees
follow_list = []

time.sleep(5)
file = open("seguidores.txt","r+")
count=0
for followee in file: #profile.get_followers()
    #follow_list.append("@"+followee.username)
    #file = open("seguidores.txt","a+")
    #file.write(follow_list[count])
    #file.write("\n")
    #file.close()
    time.sleep(1)
    #print(follow_list[count])
    #pyautogui.typewrite(followee)
    #pyautogui.press("enter")
    print(followee)
    count=count+1
# (likewise with profile.get_followers())