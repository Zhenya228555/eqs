a = int (input("ведите час:"))
def get_time(a):
    if a < 7:
        print("нічь")
    elif a > 22:
        print("нічь")
    elif a < 11:
        print("ранок")
    elif a < 18:
        print("день")
    elif a < 24:
        print("вечір")

get_time(a)