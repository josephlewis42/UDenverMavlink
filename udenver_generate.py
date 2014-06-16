import os
import sys

sys.path.append(os.path.join('pymavlink','generator'))
from mavgen import *


XML_FILE = "message_definitions/ualberta.xml"
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


def generateHeaders():
	# Generate headers
	opts = MavgenOptions(LANGUAGE, PROTOCOL, OUTPUT_FOLDER, ERROR_LIMIT);
	args = [XML_FILE]
	
	try:
		mavgen(opts,args)
		return 0
	except Exception as ex:
		exStr = formatErrorMessage(str(ex));
		
		print exStr
		return 1


if __name__ == "__main__":
		exit( generateHeaders())
