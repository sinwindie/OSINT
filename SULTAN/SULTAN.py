# Imports needed to function
import requests

#Main function
def main():
	
	  #Prompt for username
    username = raw_input("Enter a Username: ")
    
    #Array holding urla variables
    urla = ["header","https://graph.facebook.com/","https://twitter.com/","https://www.instagram.com/","https://myspace.com/","https://www.youtube.com/"]
    
    #Array holding urlb variables
    urlb = ["Social Media","","","","",""]
    
    #Array holding error text variables
    error = ["header","Some of the aliases you requested do not exist","Sorry, that page","The link you followed may be broken","Not Found","404handler"]
    
    #Array holding valid usernames for validation testing
    valid = ["n/a","jeff","twitter","twitter","jess","jess"]
    
    url = ""            # Holds full url (UrlA + username + UrlB)
    count = 0           # Counter for looping
    found = 0           # Counter for number of found usernames
    notfound = 0        # Flag for if error text found
	
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
            r = requests.get(url)
            
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
