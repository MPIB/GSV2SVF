import sys
import os
import SVFCore
import time


if __name__ == "__main__":
    dir = sys.argv[1]
    GSVCapture = SVFCore.GSVCapture()
    GSVCapture.initialize(True)
    sys.stdout.flush()
    try:
        sys.stdout.write("task.started\n")
        sys.stdout.flush()
        GSVCapture.batchGetByID(dir)
        sys.stdout.write("task.finished\n")
        sys.stdout.flush()
    except Exception as err:
        sys.stdout.write(str(err) + "\n")
        sys.stdout.write("task.failed\n")
        sys.stdout.flush()
