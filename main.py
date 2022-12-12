
def make_octets(ip_or_sub,type_of_address):
    complete = False
    while complete == False:
        address = input(f"Please enter {ip_or_sub} address: ")
        octet = 1
        add = {}
        num = ""

        try:

            for item in address:
                if item != '.': #concat numbers to string
                    num = num + item

                if item == '.':   #move to next octet upon hitting the period
                    add["oct" + str(octet)] = int(num)
                    octet = octet + 1
                    num = ""
            if octet == 4:                  #placed outside of for to complete 4th octet
                add["oct4"] = int(num)

            for values in add.values():
                if type_of_address == 'ip' and values <= 0 or values > 255:  #if address is an IP add
                    print(f'"{values}" is out of range (1 - 255 only)')
                if type_of_address == 'subnet_mask' and values < 0 or values > 255: # if add is a subnet mask
                    print(f'"{values}" is out of range (0 - 255 only)')

                    break

            return add
            complete = True

        except TypeError:
            print('The address must be formatted: XXX.XXX.XXX.XXX (ex: 192.168.1.1)')

        except ValueError:
            print('The address must be formatted: XXX.XXX.XXX.XXX (ex: 192.168.1.1)')




my_ip = make_octets('an IP','ip')
#print(my_ip)






my_subnet = make_octets('a Subnet Mask','subnet_mask')
printed_network_add = ''
printed_broadcast = ''
printed_first_usable = ''
net_add = {}
broadcast_add = {}
for subs in my_subnet:         #repeating 4 times, needs to cycle through each oct once
    sub_add = my_subnet[subs]
    ip = my_ip[subs]

    sub_size = int(256 - sub_add)
    first_add = int(ip / sub_size)
    starting_add = first_add * sub_size
    make_last = sub_size - 1
    broadcast = starting_add + make_last  # the last usable address of the subnet or returns in full if 255



    net_add[subs] = starting_add
    broadcast_add[subs] = broadcast

    if sub_size != 1 and sub_add == 0:#watch this here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        first_usable = starting_add + 1
        printed_first_usable += str(first_usable) + '.'
    elif sub_size == 1:
        printed_first_usable += str(starting_add) + '.'
    else:
        printed_first_usable += str(starting_add) + '.'


    printed_network_add += str(starting_add) + '.'
    printed_broadcast += str(broadcast) + '.'




printed_network_add = printed_network_add[:-1]
printed_broadcast = printed_broadcast[:-1]
printed_first_usable = printed_first_usable[:-1]

print(f"This is your network address: {printed_network_add}")
print(f"This is your first usable address: {printed_first_usable}")
#print(f"This is your last usable address: {last_usable}")
print(f"This is your broadcast address: {printed_broadcast}")













#x = lambda a : a + 10
#print(x(5))






