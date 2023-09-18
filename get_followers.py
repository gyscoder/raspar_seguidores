# Get instance
import instaloader
L = instaloader.Instaloader()

# Login or load session
L.login(r'login', r'senha')        # (login)


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "$") #substituir $ @pra ser raspado

# Print list of followees
follow_list = []
count=0
for followee in profile.get_followers():
    follow_list.append("@"+followee.username)
    file = open("seguidores.txt","a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count=count+1