address = input("Enter your IP:")
subnet = input("Enter your subnet mask:")

address_bytes = address.split(".")
subnet_bytes = subnet.split(".")

resulting_address = []

i=0
while i < 4:
    address_byte=int(address_bytes[i])
    subnet_byte=int(subnet_bytes[i])
    address_byte_binary = bin(address_byte)[2:]
    subnet_byte_binary = bin(subnet_byte)[2:]
    network_address_binary=int(address_byte_binary)&int(subnet_byte_binary)
    network_address=int(network_address_binary)
    resulting_address.append(f"{network_address}")
    i+=1
    
resulting_address = ".".join(resulting_address)
print(f"{resulting_address} {subnet}")