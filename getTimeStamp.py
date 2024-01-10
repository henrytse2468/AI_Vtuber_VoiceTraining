def getTimeStamp(filepath):
    f = open(filepath, "r")

    txt = f.read().replace("\u200b", "").replace("  ", "").replace("...", "").split("\n")

    timestamp = [sentence[:12] for sentence in txt]

    return timestamp

def getTranscipt(filepath):
    f = open(filepath, "r")

    txt = f.read().replace("\u200b", "").replace("  ", "").replace("...", "").split("\n")

    transcript = [sentence[12:-1] for sentence in txt]

    return transcript