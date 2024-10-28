import sys, ID_GEN2, random
import matplotlib.pyplot as plt

class analize:
    def __init__(self, data, mode="bar") -> None:
        pass

def isValid(data):
    fetched = data.value
    if fetched is None or isinstance(fetched, str) and len(fetched.strip(" ")) <= 0:
        return False
    else:
        return True

if __name__ == "__main__":
    FF = ID_GEN2.Container.XL_Data("IMPORTANT FILES BATANGAS TRACKER UPDATED.xlsx", "FAITH ATTENDANCE Updated")
    #FF = ID_GEN2.Container.XL_Data("UE Manila Tracker.xlsx", "NEW TRACKER")
    cat = list(FF.nav.keys())
    val = []
    colors = []
    for data in FF.sheet.iter_cols():
        if data[0].value not in cat: continue
        count = 0
        for row in data[1:]:
            if isValid(row): count += 1
        val.append(count)
    print("creating color scheme")
    print(cat, len(val))
    for i in val:
        while True:
            color = (random.random(), random.random(), random.random())
            if color not in colors:
                colors.append(color)
                break
    plt.figure(figsize=(10, 7))
    #plt.figure(figsize=(10, 6))

    val[15] += 33 #rob1
    val[18] += 44 #ani2
    val[18] += 44 #ani2
    val[19] += 39 #prog1
    val[19] += 35 #prog1
    val[20] += 40 #prog2
    val[20] += 19 #prog2
    val[14] += 45 #gamed2
    val[16] += 36 #rob2
    val[16] += 1 #rob2

     
    margin = 7
    #margin = 8
    plt.bar(cat[margin:], val[margin:], 0.6, color=colors[margin:])
    for i, v in enumerate(val[margin:]):
        plt.text(i, v+.2, str(v), ha='center', va='bottom')
    plt.xticks(rotation=80, fontsize=8)
    plt.subplots_adjust(bottom=0.4)
    plt.xlabel("topics")
    plt.ylabel("students take")
    plt.title("FAITH Topics Graph")
    #plt.title("UE Manila Topics")
    plt.show()
