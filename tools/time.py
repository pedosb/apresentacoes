#!/usr/bin/env python
import time
import os,sys
import sys
import termios

def getchar():
	'''
	Equivale al comando getchar() di C
	'''

	fd = sys.stdin.fileno()
	
	if os.isatty(fd):
		
		old = termios.tcgetattr(fd)
		new = termios.tcgetattr(fd)
		new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
		new[6] [termios.VMIN] = 1
		new[6] [termios.VTIME] = 0
		
		try:
			termios.tcsetattr(fd, termios.TCSANOW, new)
			termios.tcsendbreak(fd,0)
			ch = os.read(fd,7)

		finally:
			termios.tcsetattr(fd, termios.TCSAFLUSH, old)
	else:
		ch = os.read(fd,7)
	
	return(ch)

if __name__=="__main__":
   print "Type <ENTER> to start."
   i = 0
   command = getchar()
   while (command != 'q'):
      if i == 0:
	 print 'Started\n'
	 last = time.time()
	 start = last
      else:
	 now = time.time()
	 diff = now - last
	 last = now
	 print '{0: <3d}'.format(i) + ': You spent ' + '{0:0<5.2f}'.format(diff) + ' seconds'
      i += 1
      command = getchar()
   print '\nStoped. The total time spent was ' + '{0:0<5.2f}'.format(last-start) + ' seconds'
