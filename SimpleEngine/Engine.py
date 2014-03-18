


import os
import sys
import glob
import time
import subprocess
import shlex


POLL_PERIOD     = 1.0





def SimpleEngine(myName, jobRepository, jobFilter):
    """
    """

    while True:

        jobList = glob.glob(jobRepository+'/'+jobFilter)
        if jobList != [] :

            try:
                jobFileName     = jobList[0]
                targetFileName  = myName+'-Current'

                os.rename(jobFileName, targetFileName)
                job = open(targetFileName).read()
                os.remove(targetFileName)

                print('Job: [%s]'%(job))

                p   = subprocess.Popen(shlex.split(job), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out,err = p.communicate()
                print(out)
                print(err)

            except Exception as e:
                print('** Conflict for job %s (%s) **'%(jobFileName, str(e)))

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



