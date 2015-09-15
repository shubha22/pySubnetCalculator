#!/usr/bin/python

import re
import sys 

#ip = sys.argv[1]
#print ip

class SubnetCal ( object ):
    def __init__( self, ip, subnet ):
        self.ip_ = ip
        self.subnet_ = subnet

    #def __init__ ( self , ip , subnet ):
    #    self.ip_ = ip
    #    self.subnet_ = subnet
    
    def validIp ( self ):
         #This function will check if the input ip is valid 
         print " The ip is ",self.ip_
         return 

    def validSubnet ( self ):
        # This function will validate the subnet mask 
        print " The sbubnet mask is ",self.subnet_
        return
    
    def ipToBin ( self, ip ):
       # This function will change the ip into bin
       iplist =  ip.split(".")
       ipbin =  [ '{:08b}'.format(int(iplist[0])),
                  '{:08b}'.format(int(iplist[1])),
                  '{:08b}'.format(int(iplist[2])),
                  '{:08b}'.format(int(iplist[3]))]
       return ipbin
        

if __name__ == "__main__" :
    # This is the main function
    ip = raw_input("\nPlease enter a IP ")
    subnet = raw_input("\nPlease enter a subnet ")

    cal = SubnetCal( ip, subnet )
    cal.validIp()
    cal.validSubnet()
    # Find out the NID of the IP
    l =  ip.split(".")
    s =  subnet.split(".")
    nip1= int(s[0]) & int(l[0])
    nip2= int(s[1]) & int(l[1])
    nip3= int(s[2]) & int(l[2])
    nip4= int(s[3]) & int(l[2])
    
    print "\nNetwork Addres is  :",nip1,".",nip2,"." ,nip3,".",nip4 
    
   
    #Converting the Mask to Binary 
    ipbin = cal.ipToBin ( subnet )
    # Calculating the number of hosts per subnet 
    ipbin.reverse()
    c = 0
    for l in ipbin :
        for i in l[::-1]:
            if i == "1":
                break
            c+=1
    validhost = 2 ** c - 2 
    print "\nNumber of Valid Hosts per subnet :", validhost
    #Calculating the wildcard mask
    l =  subnet.split(".")
    wip1= 255 - int(l[0])
    wip2= 255 - int(l[1])
    wip3= 255 - int(l[2])
    wip4= 255 - int(l[3])
    
    print "\nWildcard mask :",wip1,".",wip2,"." ,wip3,".",wip4   
     
    #Calculating the BID
    bip1= nip1 | wip1
    bip2= nip2 | wip2
    bip3= nip3 | wip3
    bip4= nip4 | wip4
        
    print "\nBroadcast Address :",bip1,".",bip2,"." ,bip3,".",bip4   

