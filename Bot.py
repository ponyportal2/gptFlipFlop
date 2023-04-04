from driverLib import webDriverInit
from driverLib import loadPoe
from driverLib import fillMessage
from driverLib import sendMessage
from driverLib import getLast
from driverLib import kGlobalBotNum
from driverLib import kMessageDelayMultiplier
import time
import random
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

kGlobalBotNum = 2
firstRun = False
# -----------------
# CLASSES AND SHIT:
# -----------------


def clean(line):
    innerline = line
    for char in innerline:
        if char in "''":
            innerline.replace(char, '')
    return innerline


class OnMyWatch:
    # Set the directory on watch:
    if kGlobalBotNum == 1:
        watchDirectory = "./botTwo/"
    elif kGlobalBotNum == 2:
        watchDirectory = "./botOne/"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print("Watchdog received created event - % s." % event.src_path)
        elif event.event_type == 'modified':
            if kGlobalBotNum == 1:
                print("1\n")
                text_file = open("./botTwo/botTwo.txt", "r")
                response = text_file.read()
                text_file.close()
                fillMessage("'"+str(response)+"'", globalDriver)
                time.sleep(5)
                sendMessage(globalDriver)
                time.sleep(kMessageDelayMultiplier * random.randint(45, 75))
                text_file = open("./botOne/botOne.txt", "w")
                text_file.write(str(getLast(globalDriver)).replace(
                    "'", "").replace('"', '').replace('\n', ''))
                text_file.close()
                time.sleep(5)

            elif kGlobalBotNum == 2:
                if firstRun == True:
                    time.sleep(kMessageDelayMultiplier *
                               random.randint(45, 75))
                print("2\n")
                text_file = open("./botOne/botOne.txt", "r")
                response = text_file.read()
                text_file.close()
                fillMessage("'"+str(response)+"'", globalDriver)
                time.sleep(5)
                sendMessage(globalDriver)
                time.sleep(kMessageDelayMultiplier * random.randint(45, 75))
                text_file = open("./botTwo/botTwo.txt", "w")
                text_file.write(str(getLast(globalDriver)).replace(
                    "'", "").replace('"', '').replace('\n', ''))
                text_file.close()
                time.sleep(5)


# -----
# MAIN:
# -----
globalDriver = webDriverInit()
loadPoe(globalDriver)
time.sleep(10)
if kGlobalBotNum == 1:
    firstMessage = "'Please speak every next message in the voice of SHODAN from System Shock franchise, imitate how she would respond'"
else:
    firstMessage = "'Please speak every next message in the voice of SHODAN from System Shock franchise, imitate how she would respond'"
fillMessage(firstMessage, globalDriver)
time.sleep(5)
sendMessage(globalDriver)
time.sleep(1)
sendMessage(globalDriver)
time.sleep(1)
sendMessage(globalDriver)
time.sleep(kMessageDelayMultiplier * random.randint(45, 75))

if kGlobalBotNum == 1:
    secondMessage = "'Keep writing more and more ideas for books and end the message with \"Do you have any more ideas? Also please make them more and more bizzare, please.\"'"
    fillMessage(secondMessage, globalDriver)
    time.sleep(5)
    sendMessage(globalDriver)
    # time.sleep(kMessageDelayMultiplier * random.randint(45, 75))
    time.sleep(5)
    text_file = open("./botTwo/botTwo.txt", "w")
    text_file.write(str(getLast(globalDriver)).replace(
        "'", "").replace('"', '').replace('\n', ''))
    text_file.close()

watch = OnMyWatch()
watch.run()
