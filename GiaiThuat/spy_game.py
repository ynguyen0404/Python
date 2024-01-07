################################# SPY_GAME Find 007 in an iterable ###################################

list1 = [1,2,4,0,0,7,5] # ---> True
list2 = [1,0,2,4,0,5,7] # ---> True
list3 = [1,7,2,0,4,5,0] # ---> False

def spy_game(lst):

    count = 0                       # Biến này dúng để check xem có đủ 2 số 0 trong dãy chưa

    for i in lst:
        if i == 0:                  # Kiểm tra xem có số 0 nào ở trong list không, nếu có tăng count lên 1
            count += 1
        elif i == 7 and count >= 2: # Kiểm tra xem đã đủ 2 số 0 trước số 7 hay chưa bằng cách check count có >=2 không, và kiểm tra xem có số 7 đồng thời không
            return True             # Thỏa return True
    return False

print("{}".format(spy_game(list1)))