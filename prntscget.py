
# https://prnt.sc/p01tc1
linktotal = ""
linkstart = "https://prnt.sc/p"
linkmiddle = "tc"

def main():
    fileName = "prntscoutput.txt"
    file = open(fileName, "w+")

    file.write("\n")

    for x in range(80):
        for y in range(10):
            linktotal = linkstart+'%02d' % x+linkmiddle+str(y)
            file.write("\n" + linktotal)



    file.close()


if __name__== "__main__":
    main()