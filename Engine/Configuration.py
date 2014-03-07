"""
This is the central configuration file for the Continuus software.
Note that it is actually an executable python file and as such it can contain dynamically
generated data (i.e. read a value from an environment variable).
Also, the code at the end allows you to run this file from the command line to obtain
a pretty-printed version of what will actually be defined in your program.
"""

import os
import pprint


#
# Globals.
#
ContinuusBase           = os.getenv('CONTINUUS_BASE')
DatabaseName            = ContinuusBase+'/Database/Continuus.sqlite'

emailServer             = 'ZooKoo.com'
emailUsername           = 'script%zookoo.com'
emailPassword           = 'script'
emailFrom               = 'Script@ZooKoo.com'



if __name__ == '__main__':
    """
    """
    pprint.pprint(globals())

