vote_num = 0


def vote(vote_n):
    print("紬に投票する")
    vote_n += 1
    return vote_n


def sevote(vote_n):
    print("紡に投票する")
    vote_n += 1
    return vote_n


def reset_box():
    print("箱を空にする")
    vote_n = 0
    return vote_n


def check_box(vote_n):
    print("紬の表の数は{}です".format(vote_n))
    return


def secheck_box(vote_n):
    print("紡の表の数は{}です".format(vote_n))


vote_num = vote(vote_num)
check_box(vote_num)
for i in range(5):
    vote_num = vote(vote_num)
check_box(vote_num)
vote_num = vote(vote_num)
vote_num = sevote(vote_num)
for i in range(4):
    vote_num = sevote(vote_num)
