



import sys
import os.path


if __name__ == '__main__':
    """
    Usage:
    python AddJob.py EngineOne-JobOne ~/JobQueue "cal"
    """

    #
    # Extract the parameters from the arguments.
    #
    jobName         = sys.argv[1]
    jobRepository   = sys.argv[2]
    job             = sys.argv[3]

    #
    # write the job to the file in the job queue directory.
    #
    open(os.path.join(jobRepository,jobName),'w').write(job)

