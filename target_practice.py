### 
### Author: wenjun
### Course: CSc 110
### Description: The code would grab the initial hit x/y as and . Then, the outer loop would begin with as , and then the inner loop would iterate from to , printing out one character at a time. Since there are not hits on row , no s would print. After the inner loop finishes iterating, the outer loop would repeat again, with now at . The inner loop would begin iterating, and would print out a normal target up until the value reaches . At this point, AND , thus a should be printed. Right after it prints this hashtag, the program should go ahead and change and to the next values in the hit string. Then, continue looping
###
target_string = input("Hit string:\n")
target_string_len = len(target_string)
while target_string_len < 4 or target_string_len % 4 != 0:
    print("Please provide a valid hit string.")
    target_string = input("Hit string:\n")
    target_string_len = len(target_string)

marker = input("Marker:\n")
marker_len = len(marker)
while marker_len != 1:
    print("Please provide a valid marker.")
    marker = input("Marker:\n")
    marker_len = len(marker)

current_hit_x = int(target_string[0] + target_string[1])
current_hit_y = int(target_string[2] + target_string[3])
index_hit = 0

for index_row in range(5, -6, -1):
    for index_column in range(-7, 8):
        if index_row == current_hit_y and index_column == current_hit_x:
            print(marker[0], end='')
            index_hit += 4
            if index_hit < target_string_len:
                current_hit_x = int(target_string[index_hit] + target_string[index_hit + 1])
                current_hit_y = int(target_string[index_hit + 2] + target_string[index_hit + 3])
        elif index_column == 0:
            print('|', end='')
        elif index_row == 0:
            print('-', end='')
        else:
            print(' ', end='')
    print("")
