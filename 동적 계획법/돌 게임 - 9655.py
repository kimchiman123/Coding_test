def stone_game(n):
    flag = 0
    stone = n
    while True:
        if stone % 4 == 1 or stone % 4 == 2: 
            stone -= 1
        else:
            if stone >= 3:
                stone -= 3
            else: 
                stone -= 1

        if stone == 0:
            if flag == 0:
                return "SK"
            else:
                return "CY"
        flag = 1 - flag
             
        
     
n = int(input())
print(stone_game(n))