import requests
import re


#funcs
def printResults(list):
    if len(list) < 1:
        print("\nNo Resources Found")
    else:
        print("\nFound {} Resources".format(len(list)))
        printResources = raw_input("\nPrint Resources? Yes/No\n")
        if printResources.lower() == 'yes':
            print("\nPrinting Resources...\n")
            for l in list:
                print(l)
        
        




def start():
    try:
        # get url & search type
        url = raw_input('\nEnter a URL (do not include `http://`): ')
        searchType = raw_input("\nPlease select search type:\n1 = Links\n2 = Emails\n3 = Phone Numbers\n4 = ALL\n")

        # connect to the url
        website = requests.get('http://' + url)

        # read html
        html = website.text

        # use re.findall to grab all the links
        links = re.findall('"((http|ftp)s?://.*?)"', html)
        emails = re.findall('([\w\.,]+@[\w\.,]+\.\w+)', html)
        #phoneNumbers = re.findall('^((\(?0\d{4}\)?\s?\d{3}\s?\d{3})|(\(?0\d{3}\)?\s?\d{3}\s?\d{4})|(\(?0\d{2}\)?\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$', html)
        phoneNumbers = re.findall('(^[0-9 ]*$)', html)
        

        
        if searchType == '1':
            printResults(links)
        elif searchType == '2':
            printResults(emails)
        elif searchType == '3':
            printResults(phoneNumbers)
        else:
            printResults(links)
            printResults(emails)
            printResults(phoneNumbers)
        start()
    except:
        print("\nIncorrect URL")
        start()
  

                    
    
    
    



start()

