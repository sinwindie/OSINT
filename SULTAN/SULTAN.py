# Imports needed to function
import requests
import xlrd

#Main function
def main():
	
	#Arrays used to hold data imported from xlsx 
    urla = []
    urlb = []
    error = []
    valid = []
    url = ""            # Holds full url (UrlA + username + UrlB)
    count = 0           # Counter for looping
    found = 0           # Counter for number of found usernames
    notfound = 0        # Flag for if error text found
	
    #Prompt for username
    username = raw_input("Enter a Username: ")
    
    # Location of xlsx file for pulling data
    data = ("###REPLACEWITHFULLPATHTOYOURXLSXFILE###")
    
    #Set up xlrd
    wb = xlrd.open_workbook(data)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    
    # Pulls columns from excel file and adds them to array
    for i in range(sheet.nrows): 
        urla.append((sheet.cell_value(i, 0)))
        urlb.append((sheet.cell_value(i, 1)))  
        error.append((sheet.cell_value(i, 2)))
        valid.append((sheet.cell_value(i, 3)))  

	
	  #Loops through entire array
    for n in urla:
        
        #To Validate valid usernames, comment out when not testing
        #url = str(urla[count]) + valid[count] + str(urlb[count])   
                            
        #Assigns full weburl, uncomment when not testing
        url = str(urla[count]) + username + str(urlb[count])

        # If line is a header
        if urla[count] == "header":
            print ""                    # Spacing Line
            print urlb[count]           # Prints Header
            print ""                    # Spacing Line
            
            count += 1                  # Increase counter
            
        # If line is not a header (regular entry)
        else:

            #Send request to page
            try:
                r = requests.get(url)
            except:
                print("Could not connect to: " + url)
            
            #returns the HTML as a string            
            html = r.text

            # read the data from the URL and check for error text
            notfound = (html.find(error[count]))
            
            #If profile with username exists
            if notfound == -1:
                print url           # Prints url to profile
                found += 1          # Increases found count
	
            count+=1                # Increases counter
	
	  #Print the number of located profiles
    print "\n\nSULTAN found: " + str(found) + " profiles for " + username + "!"	
	 
main()
