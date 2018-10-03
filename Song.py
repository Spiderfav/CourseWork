import Auth_score

Auth_score.input_usr()

from Auth_score import admin_usr

while admin_usr != 1:
    Auth_score.input_usr()

    if admin_usr == 1:
        print("Go ahead, you are authorised.")
        print(admin_usr)
        break
    else:
        print("Not authorised to play.")
        print(admin_usr)
        print("")

print("Does it work?")
