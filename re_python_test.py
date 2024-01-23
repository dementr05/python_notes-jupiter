import re
 # meta characheters

# 1. [] -> A set of charachters
            #example
txt = "The rain in Spain"
#find all the lower case char. alpjabetically b/w a and m
x = re.findall("[a-m]",txt)
print(x)
    # here findall is a method returns a list containing all matches
 
 # 2. \ -> Signals a special sequence(can also be used to escape special characters)
# example

txt1 = "That will be 59 dollars"
#find all digit characters
x1 =re.findall("\d",txt1)
print(x1)


# 3.  . -> Any character(except newline charachter)
# example
txt3 = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x3 = re.findall("he..o",txt3)
print(x3)