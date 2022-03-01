print("嗨，你进入了一个黑房子，这里有两扇门，请选去1或是2？")
door = input(">")
if door == "1":
    print("桌子上有瓶打开的酒和被啃了一口的蛋糕。")
    print("请你选一个")
    print("1.拿走蛋糕。")
    print("2.尝尝酒。")
    wine = input(">")
    if wine == "1":
        print("酒杯开始弥漫云雾，你永久睡了过去。")
    elif wine == "2":
        print("你突然缩小，缩成拇指大小。")
    else:
        print(f"好吧，选{wine}也许并不好。")
        print("或许有什么奖励呢")
elif door == "2":
    print("你被放到了传送带上,与你一起的东西有")
    print("1.葡萄汁")
    print("2.公主裙")
    print("3.一把宝剑")

    take = input(">")

    if take == "1" or take == "2":
        print("你被迎娶到了一所宫殿，你将终生在此度过。")
    else:
        print("你拿着宝剑，砍死了三头犬，回到了家。")
else:
    print("你被看门的三头犬咬死了。")
