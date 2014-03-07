

import re
import sys
import sqlite3
from Configuration import *




def ExecuteSQL(query, databaseName=''):
    """
    Execute a SQL query & return the results in a list of rows (tuples)
    if no rows exist, [] is returned.
    """

    if databaseName == '':
        databaseName    = DatabaseName
    
    try:
        db      = sqlite3.connect(databaseName)
        cursor  = db.cursor()
        cursor.execute(query)
        
        try:
            rows    = cursor.fetchall()
        except:
            rows    = []

        db.commit()
        cursor.close()
        db.close()

    except IOError,e:
        print(str(e))
    
    return rows

    
    
    
    
if __name__ == '__main__':
    """
    Test code...
    """

    rows    = ExecuteSQL(""" insert into BuilderQueue (`ClassName`,`Parameters`,`Priority`,`JobID`) values ('ClassName','Parameters',1,4); """)
    for row in rows:
        print(row)

    rows    = ExecuteSQL(""" select * from BuilderQueue; """)
    for row in rows:
        print(row)


    
