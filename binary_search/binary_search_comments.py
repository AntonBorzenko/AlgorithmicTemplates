"""
def check1(a):
    return a >= 15

def check2(a):
    return a < 15

bisearch(check1, 0, 100),  # 15
bisearch(check1, 0, 100, right_border=False),  # 14
bisearch(check2, 0, 100, False),  # 15
bisearch(check2, 0, 100, False, False),  # 14
"""
