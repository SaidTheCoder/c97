string = input("enter your introduction")
charactercount=0
wordcount=1
for i in string:
     charactercount=charactercount+1
     if(i==' '):
         wordcount=wordcount+1
print("number of characters are =>",charactercount)
print("number of words are =>",wordcount-1)