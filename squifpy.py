import re, os
from colorama import Fore, Style, init

init()
choice = ""
should_print = True
active_pchoices = []
variables = [("said_hi",False)]
printed_sofar = ""
hasChose = False
def cprint(stuff2print):
    global printed_sofar
    mode = "normal"
    var2p = ""
    link = ""
    index = 0
    for char in stuff2print:
        if char == "}":
            mode = "normal"
        if mode == "normal":
            if char == "]":
                print(f"{Fore.BLUE}"+str(link)+f"{Style.RESET_ALL}",end="")
                printed_sofar += str(link)
                link = ""
            elif stuff2print[index-1] == "]":
                print(f"{Style.DIM}{Fore.BLUE}"+str(link)+f"{Style.RESET_ALL}",end="")
                printed_sofar += str(link)
                link = ""
                print (char, end="")
                printed_sofar += char
            elif char == "{":
                mode = "pVar"
                var2p = ""
            elif char == "}":
                for var in variables:
                    if var[0] == var2p:
                        print (var[1], end="")
                        printed_sofar += str(var[1])
                var2p = ""
            elif char == "[":
                mode = "pLink"
                link = ""
            else:
                print (char, end="")
                printed_sofar += char
        elif mode == "pVar":
            var2p += char
        elif mode == "pLink" and char not in ["[","]"]:
            link += char
        elif mode == "pLink" and char == "]":
            mode = "normal"
        index += 1

def run(section):
    global printed_sofar
    global hasChose
    global choice
    global should_print
    global active_pchoices
    global variables
    global hasChose
    if should_print:
        cprint(list(section[2]+"\n"))
    should_print = True
    choice = ""
    while choice != 'end' and choice not in section[3]+section[4]+active_pchoices: 
        choice = input("> ")
        if not hasChose:
            printed_sofar += "\nYou chose: \""+choice+"\"\n"
            hasChose = True
        else:
            printed_sofar += "\nThen, you chose: \""+choice+"\"\n"
    for i in marked:
        if i[1] == choice and i[0] == "section":
            choice = i
            print ("_________________")
            printed_sofar += "_________________\n"
            hasChose = False
            os.system("cls")
            print (printed_sofar)
            active_pchoices = []
        elif i[1] == choice and i[0] == "passage":
            choice = section
            should_print = False
            if not i[5]:
                cprint(list(i[2]+"\n"))
                for thing in i[3]+i[4]:
                    active_pchoices.append(thing)
                i[5] = True

text = ["[[default]]:"]+open("code.squifpy","r").read().split("\n")

marked1 = []

for i in text:
    if i[0] == "[" and i[-1] == ":":
        if i[1] == "[":
            marked1.append(("section", i[2:-3]))
        else:
            marked1.append(("passage", i[1:-2]))
    elif i[0] == "@":
        marked1.append(("scode", i[1:]))
    elif i[0] == "\t":
        marked1.append(("pycode", i[1:]))
    else:
        marked1.append(("text", i))

marked = []     
for i in marked1:
    if i[0] == "section" or i[0] == "passage":
        marked.append([i[0],i[1],[],"",[],[]])
    elif i[0] == "text":
        marked[-1][2].append(i[1])
for i in marked:
    i[3] = '\n'.join(i[2])
    del i[2]

for i in marked:
    for match in re.findall('\\[\\[(.*?)\\]\\]',i[2]):
        i[3].append(match)
    index = 0
    for match in re.findall('\\[(.*?)\\]',i[2]):
        if match[0] != "[":
            i[4].append(re.findall('\\[(.*?)\\]',i[2])[index])
        index += 1
choice = marked[0]

for i in marked:
    if i[0] == "passage":
        i.append(False)
while choice != 'end':
    run(choice)