#debug
def loadTweetData2(filePath = path + "./tweet_small.txt"):
    data = openFile(filePath, 'r')
    checkEnd = lambda x: re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', x)
    checkStart = lambda x: re.search(r'^\d{2,}\t\d{2,}\t', x)
    result = []
    for line in data:
        if not checkStart(line):
            result.append(line)
    return result

##x = loadTweetData()
##f = openFile("./new.txt", 'w+')
##for i in x:
##    f.write(i[0] + "\t" + i[1] + "\t" + i[2] + "\n")
##f.close()
