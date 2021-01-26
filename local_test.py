import time
from twitter_program import azureDBconnections

hashtags = ["kwarantanna", "vege", "IgaŚwiatek", "hot16challange", "fitness", "krolowezycia", "kryzys", "ikea", "łódź",
            "haloween", "kawa", "radom", "karmieniepiersia", "pomidorowa", "COVID19", "nvidia", "poniedziałek",
            "biedronka"]


def count_twitts(table):
    daily = dict()
    for record in table:
        date = time.strptime(record[1], "%a %b %d %H:%M:%S %z %Y")
        str_date = str(date.tm_year) + ", " + str(date.tm_mon) + ", " + str(date.tm_mday)
        if str_date not in daily:
            daily[str_date] = {"positive": 0, "neutral": 0, "negative": 0, }
        tmp = record[2]
        if tmp == 1:
            daily[str_date]["positive"] = daily[str_date]["positive"] + 1
        elif tmp == 0:
            daily[str_date]["neutral"] = daily[str_date]["neutral"] + 1
        elif tmp == -1:
            daily[str_date]["negative"] = daily[str_date]["negative"] + 1
    return daily


def fetch_data(tag):
    tmp_data = []
    if tag == "global":
        for hash_tag in hashtags:
            table = azureDBconnections.select(hash_tag)
            counted = count_twitts(table)
            tmp_data.append({"hash_tag": hash_tag, "data": counted})
    else:
        table = azureDBconnections.select(tag)
        counted = count_twitts(table)
        tmp_data.append({"hash_tag": tag, "data": counted})
    return tmp_data


print(fetch_data("kwarantanna"))
