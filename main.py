address = input("Please enter an IP address: ")
#original_address = address



def make_octets(address):


    octet = 1
    add = {}
    num = ""
    for item in address:
        if item != '.': #concat numbers to string
            num = num + item

        if item == '.':   #move to next octet upon hitting the period
            add["oct" + str(octet)] = int(num)
            octet = octet + 1
            num = ""
    if octet == 4:                  #placed outside of for to complete 4th octet
        add["oct4"] = int(num)


    for keys,values in add.items():
        if values <= 0 or values > 255:
            print(f'This number is out of range [{values}] (1 - 255 only)')
            continue
        else:
            return




my_ip = make_octets(address)



subnet_mask = input("Please enter a subnet mask(or CIDR number [ex. /24])")

my_subnet = make_octets(subnet_mask)

last_add = ""
net_add = ""
for subs in my_subnet:         #repeating 4 times, needs to cycle through each oct once
    sub_add = my_subnet[subs]
    ip = my_ip[subs]

    sub_size = int(256 - sub_add)
    first_add = int(ip / sub_size)
    starting_add = first_add * sub_size
    make_last = sub_size - 1
    last_add = starting_add + make_last  # the last address of the subnet


    if starting_add == 0:
        net_add += str(starting_add) + '.'


    else:
        net_add += str(starting_add) + '.'

net_add = net_add[:-1]
#last_address = net_add["oct4"] = str(last_add)

print(f"This is your network address: {net_add}")

print(last_add)









#x = lambda a : a + 10
#print(x(5))






