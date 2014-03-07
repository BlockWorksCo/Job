#!/bin/sh

export CONTINUUS_BASE=~/Projects/ContinuusSoftware
export PYTHONPATH=$CONTINUUS_BASE/Core:$CONTINUUS_BASE/FrontEnd:$CONTINUUS_BASE/Core/ProjectSpecific
python ProcessQueue.py QueueReader 

