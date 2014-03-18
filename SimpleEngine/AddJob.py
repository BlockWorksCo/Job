



import sys


if __name__ == '__main__':
    """
    """

    jobName         = sys.argv[1]
    jobRepository   = sys.argv[2]
    job             = sys.argv[3]

    open(jobRepository+'/'+jobName,'w').write(job)

