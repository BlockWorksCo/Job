

SimpleEngine
============

A simple job-executing engine:
* Jobs are text files stored in a JobQueue (directory).
* Content of a job file is the command to run.
* A single build engine searches for jobs with the given glob pattern to enable an engine to choose appropriate jobs for itself.




To run an engine:
-----------------
python Engine.py EngineOne ~/JobQueue EngineOne-*

To queue up a job for a build engine.
python AddJob.py EngineOne-JobOne ~/JobQueue "ls -la"



