import sys, ID_GEN2, random, json
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
    wba = FF.root.active
    ws = wba.values
    schecol = 5 #index where the schedule is
    schedule = [row[schecol] for row in ws]
    sche = list(set(schedule))
    sche.remove("SCHEDULE")
    sheesh = {}
    margin = 7
    cat = list(FF.nav.keys())
    colors = []
    dcolors = {}
    print("initialization of data and collor assignment!")
    for sched in sche:
        local = {}
        subject = []
        counts = []
        for cindex, data in enumerate(FF.sheet.iter_cols()):
            if cindex < margin or data[0].value not in cat: continue
            if data[0].value not in list(dcolors.keys()):
                while True: #color management
                    color = (random.random(), random.random(), random.random())
                    if color not in colors:
                        colors.append(color)
                        dcolors[data[0].value] = color
                        break

            count = 0
            for rindex, row in enumerate(data[1:]):
                rindex += 1
                rsched = schedule[rindex]
                if isValid(row) and sched == rsched:
                    count += 1
            counts.append(count)
            subject.append(data[0].value)
        local["subjects"] = subject
        local["count"] = counts
        sheesh[sched] = local
            
    with open("debug.json", "w", encoding="utf8") as F:
        json.dump(sheesh, F, ensure_ascii=False, indent=4)
    ##input("shit has been dumped")

    #quickfix
    #AM
    sel = sheesh['10 - 12 AM']
    sel["count"][18-6] += 44 #ani2
    sel["count"][19-6] += 35 #prog1
    sel["count"][20-6] += 19 #prog2
    sel["count"][16-6] += 36 #rob2
    #PM
    sel = sheesh['1 - 3 PM']
    sel["count"][15-6] += 33 #rob1
    sel["count"][18-6] += 44 #ani2
    sel["count"][19-6] += 39 #prog1
    sel["count"][20-6] += 40 #prog2
    sel["count"][14-6] += 45 #gamed2


    fig, axs = plt.subplots(1, 3, figsize=(30, 7))

    for tind, tsched in enumerate(list(sheesh.keys())):
        plt.xticks(rotation=80, fontsize=8)
        axs[tind].bar(list(sheesh[tsched]["subjects"]), list(sheesh[tsched]["count"]), 0.6, color=colors)
        axs[tind].xaxis.set_visible(False)
        #axs[tind].set_xlabel("topics")
        #axs[tind].set_ylabel("students take")
        #axs[tind].set_title(sheesh[tsched])
        for i, v in enumerate(list(sheesh[tsched]["count"])):
            axs[tind].text(i, v+.2, str(v), ha='center', va='bottom')

    #plt.figure(figsize=(10, 7))
    #plt.figure(figsize=(10, 6))
    margin = 7
    #margin = 8
    #plt.bar(cat[margin:], val[margin:], 0.6, color=colors[margin:])
    #for i, v in enumerate(val[margin:]):
    #    plt.text(i, v+.2, str(v), ha='center', va='bottom')
    plt.xticks(rotation=80, fontsize=8)
    plt.subplots_adjust(bottom=0.4)
    #plt.xlabel("topics")
    #lt.ylabel("students take")
    #plt.title("FAITH Topics Graph")
    #plt.title("UE Manila Topics")

    for ind, sub in enumerate(sheesh[None]["subjects"][0:9]):
        plt.text(-40, (ind+1)*-10, sub.replace("\n", " "), color=colors[ind][0:9])
    for ind, sub in enumerate(sheesh[None]["subjects"][10:]):
        plt.text(-20, (ind+1)*-10, sub.replace("\n", " "), color=colors[ind+9])    


    plt.show()
