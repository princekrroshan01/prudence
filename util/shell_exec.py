import os
import sys

'''used to kill the process running firefox as sqlite3 does not work with 2 concurrent threads'''
os.system('kill -9 $(ps -x | grep firefox)')
#used to find the loaction of places.sqlite in system 
os.system('./util.sh')
#used to create the file track.csv and track1.csv 
os.system('./fileread.sh')
