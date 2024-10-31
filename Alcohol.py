""""mock"""
def main():
    """test"""
    sex = str(input())
    weight = int(input())
    card = str(input())
    cc = float(input())
    al = (float(input()))/100
    num = int(input())
    hour = int(input())
    algram = ((cc*num)*al)/100
    if sex == "Male":
        ladab = (algram/(weight*0.68*10))-(0.15*hour)
    elif sex == "Female":
        ladab = (algram/(weight*0.55*10))-(0.15*hour)
    if card == "No":
        print("Not Safe")
    elif ladab <= 0.5:
        print("Safe")
    elif ladab > 0.5:
        print("Not Safe")
main()
