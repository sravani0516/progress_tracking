ip_a=[]
with open ("sample_log.log","r") as log:
    lines=log.readlines()
    
    for line in lines:
        if "reverse mapping" in line:
            words=line.split("[")
            ip_add=words[2].split("]")
            ip_a.append(ip_add[0])
with open("ip_address_out.txt","w") as ip:
    for addr in ip_a:
        ip.write(addr+ "\n")
        
print("Ip addresses extracted successfully")
with open("ip_address_out.csv","w") as ip:
    for addr in ip_a:
        ip.write(addr+ "\n")
