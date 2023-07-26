vote_num = 0


def vote():
    print("紬に投票します")
    global vote_num
    vote_num += 1


def sevote():
    print("紡に投票する")
    global vote_num
    vote_num += 1


def reset_box():
    global vote_num
    print("箱を空にします")
    vote_num = 0


def check_box():
    global vote_num
    print("紬の表の数は{}です".format(vote_num))


def secheck_box():
    global vote_num
    print("紡ぐの表の数は{}です".format(vote_num))


vote()
check_box()
vote()
check_box()
for i in range(3):
    sevote()
secheck_box()
reset_box()
check_box()
secheck_box()
