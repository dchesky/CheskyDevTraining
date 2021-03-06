"""DevNet High - Class of 2020 - Challenge 1"""

import random
import ipaddress

# TODO: Write a print statement that displays both the type and value of 'ip'
ip = "10.1.1.200"
x=type(ip)
print()
print ("TODO: Write a print statement that displays both the type and value of 'ip'")
print ('Type = ',(x))
print('IP =',(ip))



# TODO: Write a conditional to print out if `iosversion` is less than or greater than 14
iosversion = random.randint(12, 17)

print ()
print("TODO: Write a conditional to print out if `iosversion` is less than or greater than 14")
print('iosversion =', iosversion)
if iosversion < 14:
	print('iosversion is less than 14'.format(iosversion))
if iosversion > 14:
	print('iosversion is greater than 14'.format(iosversion))


# TODO: Write a conditional that prints the serial number of the device
devices = ({'CAT9300':'XVNM1245ERGC'}, {'ISR4331':'VNMM8742THBX'}, {'NGFW2120':'EAQP4900RTJO'})
device = random.sample(devices, 1) [0]
device = list(device.values())[0]

print()
print("TODO: Write a conditional that prints the serial number of the device")
print (device)
if device == 'XVNM1245ERGC' :
	print ('CAT9300 serial number =', device)
elif device == 'VNMM8742THBX' :
	print ('ISR4311 serial number =', device)
else:
	print ('NGFW2120 serial number =', device)

# Function for converting CIDR notation into 32-bit netmask (nothing to do here)
def cidr_to_netmask(ip_str):
    ip = ipaddress.IPv4Network(ip_str)
    return ip.with_netmask

'''
TODO: Call the function above few times to so that the input of IP network with CIDR displays the IP network with 32-bit netmask
Example:
Input would be '10.1.1.0/24' and when printed out the output would be '10.1.1.0/255.255.255.0'
'''

print()
print('TODO: Call the function above few times to so that the input of IP network with CIDR displays the IP network with 32-bit netmask')
result = cidr_to_netmask('10.1.1.0/24')
print()
print(result)
result = cidr_to_netmask('10.5.25.128/32')
print()
print(result)
result = cidr_to_netmask('10.1.81.0/25')
print()
print(result)
result = cidr_to_netmask('10.1.1.0/24')
print()
print(result)


