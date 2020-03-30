import os
import sys
os.system('kill -9 $(ps -x | grep firefox)')
os.system('./util.sh')
os.system('./fileread.sh')


