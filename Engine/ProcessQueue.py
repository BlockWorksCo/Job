#!/usr/bin/python






from Logging import *
from Configuration import *
import traceback
import sys









if __name__ == '__main__':
    """
    Entry point for the Continuus CI system. This is the main loop for a Continuus machine.
    """

    if len(sys.argv) == 2:

        #
        # First parameter is the classname of the QueueReader to create.
        # Create an instance of the desired class type.
        #
        qReaderModuleName     = sys.argv[1] 
        qReaderModule         = __import__(qReaderModuleName)
        qReaderClass          = qReaderModule.__dict__[qReaderModuleName]
        qReaderInstance       = qReaderClass()

        #
        # Using the qReader we have just created, get the next Builder object from the queue and 
        # process it.
        # Note: The Builder object is already configured via the parameters in the queue by this point.
        #
        try:
            builder = qReaderInstance.GetNext()
            if builder != None:
                builder.Go()
            else:
                Log('Nothing in queue')

        except:
            traceback.print_exc()
            Log('\nBugger, we got an exception performing a %s.'%qReaderModuleName)

    else:
        print('\nProcessBuilderQueue <QueueReaderClassName>\n\n')


