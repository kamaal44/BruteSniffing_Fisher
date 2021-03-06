import Setup.setup as setup
import Includes.includes as includes
import modules.Attack.BruteForce.bruteforce as bruteforce
from modules.Attack import fishing, sniffer, infoGathering
import os
import sys


def max_index(dictionary):
    '''
    returns the bigger index < 98 on the current menu
    :param dictionary:
    :return: maxIndex: int
    '''
    keys = list(dictionary.keys())
    L = []
    for key in keys:
        if key < 98:
            L.append(key)
    return max(L)

class Directory:

    def __init__(self, dict, flag):
        self.dict = dict
        self.flag = flag

    def show(self):
        for key in self.dict:
            print("%d) %s" % (key, self.dict[key]))

    def change_directory(self, newDict, newFlag):
        self._oldFlag = self.flag
        self.dict = newDict
        self.flag = newFlag

    def clear_screen(self):
        os.system(includes.command(setup.commands, 'clear'))



    def printt(self, cmd):
        print(includes.command(setup.commands,cmd))

class Router:

    def __init__(self, dire, directories, links, attack):
        self.dire = dire
        self.attack = attack
        self.dirS = directories
        self.links = links


    def start(self):
        while 1:

            self.dire.show()
            try:
                x = int(input(">> "))
            except KeyboardInterrupt:
                print("\nExiting...")
                sys.exit(0)
            except:
                print("\nInput mus be an integer")
                continue

            if x == 99:
                sys.exit(0)
            elif x == 98:
                self.dire.change_directory(self.dirS[self.dire._oldFlag], self.dire._oldFlag)
                self.dire.clear_screen()
                continue
            elif x > max_index(self.dire.dict):
                print('\n[-]',x,"is not a valid argument\n")
                continue
            if self.links[0][0] in list(self.dire.dict.values()) and x == self.links[0][1]:
                self.dire.change_directory(self.dirS[x],x)
            else:
                self.attack.name = self.dire.dict[x]
                self.attack.run()
                #break

            self.dire.clear_screen()


class Attack:

    def __init__(self, dire):
        self.name = ""
        self.dire = dire

    def run(self):
        self.dire.clear_screen()
        if self.name == "Information Gathering":
            infoGathering.scanner()
        elif self.name == "Sniffing":
            sniffer.sniffing()
        elif self.name == 'Zip-file Bruteforce':
            bruteforce.zip_bruteForce()
        elif self.name == "Bruteforce":
            bruteforce.run()
        elif self.name == "Cloning":
            fishing.clone()
        elif self.name == "Fishing":
            fishing.fish()

