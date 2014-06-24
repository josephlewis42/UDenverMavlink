import os
import sys

sys.path.append(os.path.join('pymavlink','generator'))
from mavgen import *


OUTPUT_FOLDER = "include/"
LANGUAGE = "C"
PROTOCOL = "1.0"
ERROR_LIMIT = 5


"""\
This class mimicks an ArgumentParser Namespace since mavgen only
accepts an object for its opts argument.
"""
class MavgenOptions:
    def __init__(self,language,protocol,output,error_limit):
        self.language = language
        self.wire_protocol = protocol
        self.output = output
        self.error_limit = error_limit;


def generateHeaders(XML_FILE):

    filename = XML_FILE.split("/")[-1][:-4]
    outputpath = OUTPUT_FOLDER + filename + "/mavlink.h"

    #print os.path.getmtime(outputpath)
    #print os.path.getmtime(XML_FILE)

    #try:
    #    if os.path.getmtime(XML_FILE) < os.path.getmtime(outputpath):
    #        print "NOTHING TO BE DONE FOR: " + XML_FILE + " already generated newer version"
    #        return 0
    #except OSError:
    #    pass

    # Generate headers
    opts = MavgenOptions(LANGUAGE, PROTOCOL, OUTPUT_FOLDER, ERROR_LIMIT);
    args = [XML_FILE]

    try:
        mavgen(opts,args)
    except Exception as ex:
        exStr = formatErrorMessage(str(ex));

        print exStr
        return 1
    return 0



if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)

    exit( generateHeaders(sys.argv[1]))
