import urllib,urllib2,sys,platform,os,re
class bcolors:
	HEADER = '\033[95m'
	OKGREEN = '\033[92m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
dlib=open("dlib","r")
code=dlib.read()
dlib.close()
ln=1
av=join(re.findall('v=(.*?);',code.replace("\n",";")))
vl="https://raw.githubusercontent.com/BlackFireFox/dlib/master/dlib"
print "Connecting..."
try:
	urllib2.urlopen(vl)
	print "Success."
	site=urllib.urlopen(vl)
	page=site.read()
	page=page.replace("\n",";")
	ov=join(re.findall('v=(.*?);',page.replace("\n",";")))
	print "Actual version:",bcolors.BOLD+bcolors.OKGREEN+ov+bcolors.ENDC
	if ov==av:
		print "Your version:",bcolors.BOLD+bcolors.OKGREEN+av
		print "Your software is at the latest version."+bcolors.ENDC
	else:
		print "Your version:",bcolors.BOLD+bcolors.FAIL+av+bcolors.ENDC
		while True:
			up=raw_input("Update? [y or n]: ")
			if up=="y" or up=="yes":
				if platform.system()=="Linux":
					try:
						print "Update..."
						os.system("git clone https://github.com/BlackFireFox/dlib temp && cd temp/ && mv ../temp/* .. && rm -rf ../temp && make reinstall")
						print "(If reinstall not completed, type:)"
						print "sudo make reinstall"
						print "Completed."
					except:
						print "Git not installed."
						print "Go here for download:"
						print "https://github.com/BlackFireFox/dlib"
					sys.exit()
				else:
					print "Go here for download:"
					print "https://github.com/BlackFireFox/dlib"
					sys.exit()
			elif up=="n" or "no":
				print "Don't update."
				sys.exit()
			else:
				print "Error. Retry."
except urllib2.HTTPError, e:
	print "Error:"
	print(e.code)
except urllib2.URLError, e:
	print bcolors.FAIL+bcolors.BOLD+"Error:"+bcolors.ENDC
print(e.args)