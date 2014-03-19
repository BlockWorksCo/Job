


import os
import sys
import glob
import time
import subprocess
import shlex
import logging
import logging.handlers

POLL_PERIOD     = 1.0





def Engine(myName, jobRepository, jobFilter):
    """
    The Job Engine.
    """

    #
    # Forever...
    #
    while True:

        #
        # Get a list of all files in the job directory matching the filter.
        #
        jobList = glob.glob(jobRepository+'/'+jobFilter)
        if jobList != [] :

            #
            # Try taking possession of the first job by renaming it to our local instance name.
            #
            try:
                jobFileName     = jobList[0]
                targetFileName  = myName+'-Current'

                #
                # Take possession of the job.
                #
                os.rename(jobFileName, targetFileName)
                job = open(targetFileName).read()
                os.remove(targetFileName)

                #
                # Run the job.
                #
                logger.info('Start: [%s]'%(job))
                p   = subprocess.Popen(shlex.split(job), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out,err = p.communicate()
                logger.debug('stdout:\n%s\n'%out)
                logger.debug('stderr:\n%s\n'%err)
                logger.info('Stop: [%s]'%(job))

            except Exception as e:

                #
                # Failed to take possesion of the job. Abort and try again.
                #
                logging.info('** Conflict for job %s (%s) **'%(jobFileName, str(e)))


        #
        # Wait for a while before polling the job queue again.
        #
        time.sleep(POLL_PERIOD)





if __name__ == '__main__':
    """
    Usage:
    Engine.py $COMPUTERNAME ~/JobDirectory TestTypeOne*
    """

    #
    # Extract the parameters for the Engine from the supplied parameters.
    #
    myName          = sys.argv[1]
    jobRepository   = sys.argv[2]
    jobFilter       = sys.argv[3]

    #
    # Create the logger with two handlers (stdout & file) with associated formatters.
    #
    logger = logging.getLogger('BuildEngine-'+myName)
    logger.setLevel(logging.DEBUG)

    handler     = logging.FileHandler('SimpleEngine.log')
    logger.addHandler(handler)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    handler     = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(handler)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    #
    # Start the Engine.
    #
    logger.info('Starting SimpleEngine')
    Engine(myName, jobRepository, jobFilter)



