import re
'''text="python is powerful"
res=re.match("python",text)
if res:
    print("Marcg Found: ",res.group())
    '''
#text="my number is 6258969531 and 9812546324"
#num=re.findall(r"\d{10}",text)
#print(num)
#for match in re.finditer(r"\d{10}",text):
 #   print("match found at index: ",match.start(),"to",match.end())
 
text="my number is 9014827267"
masked=re.sub(r"\d{6}","XXXXXX",text)
print(masked)