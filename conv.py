import fnmatch
import os
m4as = []
for root, dirs, files in os.walk('/Users/piyushladdha/Desktop/spotmp3'):
    m4as += fnmatch.filter(files, '*.m4a')
##print(m4as)
count = 0
for i in m4as:
	print(i+ " "+str(count))
	count= count +1
	os.system("ftransc -r -q extreme -f mp3 "+"'"+i+"'")
