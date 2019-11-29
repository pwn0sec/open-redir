#!/usr/bin/python
import os,requests,signal
from optparse import OptionParser
from colorama import *

def banner():
    print(Style.BRIGHT + Fore.YELLOW + """
    ____                 ____           ___                __ 
   / __ \_      ______  / __ \___  ____/ (_)_______  _____/ /_
  / /_/ / | /| / / __ \/ /_/ / _ \/ __  / / ___/ _ \/ ___/ __/
 / ____/| |/ |/ / / / / _, _/  __/ /_/ / / /  /  __/ /__/ /_  
/_/     |__/|__/_/ /_/_/ |_|\___/\__,_/_/_/   \___/\___/\__/                                                            
       [ version 0.1 ]       [ Pwn0sec (pwn0sec.researcher@gmail.com) ]
                                           [ twitter.com/pwn0sec ]
        """ + Style.RESET_ALL)

def main():
    os.system('clear')
    banner()
    usage = "Usage: python %prog [-h] -u 'URL' -f [file]"

    parser = OptionParser(usage=usage)
    parser.add_option("-u", "--url", dest="url", help="target URL")
    parser.add_option("-f", "--file", dest="file", help="payloads file")    

    (options, args) = parser.parse_args()
    if options.url is None: 
        parser.print_help() 
        exit()
    
    # Payloads file
    if options.file is True:
        s.addOption("file", True)


    #Open file
    with open(options.file) as f: 
	for payload in f:
	    payloadF = payload.strip() 
	    urlF = options.url + payloadF
	    print(urlF)
	
	    #Get the response(200,400,404).
	    response = requests.get(urlF, verify=True)

	    #===Process to find an open redirect===.
	    if response.history:
	            
	        #Compare the destination url with Bing's url.
	        if str(response.url)[0:19] == 'http://www.bing.com' or str(response.url)[0:20] == 'https://www.bing.com':

		    print (Style.BRIGHT + Fore.YELLOW + "Open Redirect Vulnerability found!" + Style.RESET_ALL)
	            print (Fore.YELLOW + "Redirected to:"), Fore.RED, response.status_code, response.url, Style.RESET_ALL
	            print (Style.BRIGHT + Fore.BLUE + "Payload ---> " + Style.RESET_ALL), Fore.BLUE + payloadF + Style.RESET_ALL + "\n"
	            exit()
	        else:
	            print (Fore.YELLOW + "Redirected to:"), response.status_code, response.url, Style.RESET_ALL + "\n"

	    else:
	        print "Request was not redirected\n"


#Press ctrl+c to finish
def ctrl_c(signum, rfm):
    print ("\nSee you soon!\n")
    exit()

signal.signal(signal.SIGINT, ctrl_c)

try:
    main()
    print(Fore.YELLOW + "RESULT: " + Style.RESET_ALL + "No Open Redirect Found!")
except(TypeError):
    print("Usage: python ordetector.py -u 'URL' -f [file]\n")
