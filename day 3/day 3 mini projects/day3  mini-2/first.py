'''file=open("notes.txt","w")
file.write("welcome to python file handling!\n")
file.write("this is a sample file.\n")
file.close()
file=open("notes.txt","a")
file.write("this is appended\n")

file.close()
'''

#with open("notes.txt",'r') as file:
 #   content=file.read()
  #  print(content)

#feedback=input("give your feedback")
#ith open("feedback.txt",'a') as file:
 #   file.write(feedback+"\n")
#print("thank u for ur feed back")

#with open("data.txt",'r') as file:
 #  print(file.readline().strip())
  #  print(file.readline().strip())
   # print(file.readline().strip())
    
'''with open("data.txt",'r') as file:
    while True:
        line=file.readline()
        if not line:
            break
        print(line.strip())
    '''
        
with open("data.txt",'r') as file:
    for line in file:
        print(line.strip())
                