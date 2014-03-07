




import Database
import json





class QueueReader:
    """
    """

    def __init__(self):
        """
        Initialise the QueueReader with a default query that would pull anything off the queue.
        """
        self.query  = """ select ID,ClassName,Parameters,Priority,JobID from BuilderQueue order by Priority limit 1; """
        print('QueueReader created')




    def PutJobIntoQueue(self, className, parameters, priority, jobID):
        """
        This should be put into a QueueWriter object (or more likely the Job object) as it doesn't belong here.
        """
        parameterText   = json.dumps(parameters)
        rows            = Database.ExecuteSQL(""" insert into BuilderQueue (ClassName,Parameters,Priority,JobID) values ('%s','%s',%d,%d); """%(className, parameterText, priority, jobID))
        for row in rows:
            print(row)




    def CreateInstanceOfClass(self, className, parameters):
        """
        This is actually a utility function to create an instance of the named class and pass it the 
        supplied parameters dictionary.
        """
        moduleObject   = __import__(className)
        classObject    = moduleObject.__dict__[className]
        instance       = classObject(parameters)

        return instance




    def GetNext(self):
        """
        Returns an instance of a Builder from the description at the top of the queue.
        The 'top of queue' is entirely determined by the query (overridden in derived
        classes).
        """

        #
        # TODO: This needs to be an atomic transaction.
        #
        rows    = Database.ExecuteSQL(self.query)
        if len(rows) > 0:

            (ID, className, parameterText, priority, jobID)     = rows[0]
            parameters      = json.loads(parameterText)
            builderObject   = self.CreateInstanceOfClass(className, parameters)
            #print('--- %s ---'%str(rows[0]))

            result  = Database.ExecuteSQL(""" delete from BuilderQueue where ID=%d; """%ID)
            print(result)

            return builderObject 

        return None




    def Show(self):
        """
        Show the contents of the queue for debugging purposes.
        """
        rows    = Database.ExecuteSQL(""" select * from BuilderQueue; """)
        for row in rows:
            print('-> %s'%(str(row)))







if __name__ == '__main__':
    """
    Test code
    """
    q   = QueueReader()
    print('\nBefore:')
    q.Show()
    q.PutJobIntoQueue('BananaUnitTester',{"a":0,"b":1,"c":2}, 1,5)
    print('\nAfter:')
    q.Show()

