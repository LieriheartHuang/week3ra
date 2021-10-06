### 
### Author: Your Name Here
### Course: CSc 110
### Description:Many of you have probably selected or created an avatar, perhaps for a video-game or a profile image. There are also general-purpose avatar creators online,This section explains what each input values controls. Each of the inputs have an expected format. However, you do not need to validate all of these inputs. You may assume that the user will enter a value that follows the rules for all of them.
###





def hat(hat_style):
    print("       ~-~       ")
    print("     /-~-~-\     ")
    if (hat_style == "left"):
        print(" ___/_______\    ")
    elif (hat_style == "both"):
        print(" ___/_______\___ ")
    elif (hat_style == "right"):
        print("    /_______\___ ")
    elif (hat_style == "front"):
        print("    /_______\    ")
    else:
        print(
            f"err - unknown hat style {hat_style}, must be 'left' or 'both' or 'right' or 'front'"
        )


def face(eye_character, long_hair):
    if (long_hair == "True"):
        print("   \"|\"\"\" \"\"\"|\"    ")
    elif (long_hair == "False"):
        print("    |'''''''|   ")
    else:
        print(f"err - wrong long hair {long_hair}, must be 'True' or 'False'")
    hair_char = "\"" if long_hair == "True" else " "
    print(f"   {hair_char}| {eye_character}   {eye_character} |{hair_char}")
    print(f"   {hair_char}|   V   |{hair_char}")
    print(f"   {hair_char}|  ~~~  |{hair_char}")
    print(f"   {hair_char} \_____/ {hair_char}")


def body(arm_style, torso_length):
    torso_length = int(torso_length)
    start = 0  # (torso_length - 1) // 2 - 1
    while start > 0:
        print("      |-X-|      ")
        start -= 1
        torso_length -= 1
    print(f" 0{arm_style*4}|---|{arm_style*4}0")
    torso_length -= 1
    while torso_length >= -1:
        print("      |-X-|      ")
        torso_length -= 1
    print("      HHHHH      ")


def leg(leg_length):
    leg_length = int(leg_length)
    if not isinstance(leg_length, int) or not (0 < leg_length < 5):
        print(f"err - wrong leg length {leg_length}, must be 1~4")
    else:
        row = 0
        while row < leg_length:
            row += 1
            print(" " * (6 - row) + "///" + " " * (2 * row - 1) + "\\\\\\")


def shoe(shoe_look):
    print(f"{shoe_look}       {shoe_look}")


def custom():
    # create custom avatar
    print("Answer the following questions to create a custom avatar")
    hat_style = input("Hat style ?\n")
    eye_character = input("Character for eyes ?\n")
    long_hair = input("Long hair (True/False) ?\n")
    arm_style = input("Arm style ?\n")
    torso_length = input("Torso length ?\n")
    leg_length = input("Leg length (1-4) ?\n")
    shoe_look = input("Shoe look ?\n")
    print(' ')
    hat(hat_style)
    face(eye_character, long_hair)
    body(arm_style, torso_length)
    leg(leg_length)
    shoe(shoe_look)


def Jeff():
    hat("both")
    face("0", "False")
    body("=", 6)
    leg(2)
    shoe("#HHH#")


def Jane():
    hat("right")
    face("*", "True")
    body("T", 3)
    leg(3)
    shoe("<|||>")


def Chris():
    hat("front")
    face("U", "False")
    body("W", 4)
    leg(4)
    shoe("<>-<>")


def main():
    # entry point
    print("----- AVATAR -----")
    command = input("Select an Avatar or create your own:\n")
    while True:
        if command == "custom":
            custom()
        elif command == "exit":
            break
        elif command == "Jeff":
            Jeff()
        elif command == "Jane":
            Jane()
        elif command == "Chris":
            Chris()
        else:
            print(f"wrong command: {command}")
            print(
                "must be one of 'custom' or 'exit' or 'Jeff' or 'Jane' or 'Chris'"
            )
        break


main()

