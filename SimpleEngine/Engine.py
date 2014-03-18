


import os
import sys
import glob
import time



POLL_PERIOD     = 1.0





def SimpleEngine(myName, jobRepository, jobFilter):
    """
    """

    while True:

        jobList = glob.glob(jobRepository+'\\'+jobFilter)
        if jobList != [] :
            jobFileName     = jobList[0]
            job = open(jobFileName).read()
            print('Job: [%s]'%(job))

        time.sleep(POLL_PERIOD)





if __name__ == '__main__':
    """
    Usage:
    SimpleEngine.py $COMPUTERNAME ~/JobDirectory TestTypeOne*
    """

    myName          = sys.argv[1]
    jobRepository   = sys.argv[2]
    jobFilter       = sys.argv[3]

    SimpleEngine(myName, jobRepository, jobFilter)



