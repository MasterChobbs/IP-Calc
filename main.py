
def make_octets(ip_or_sub,type_of_address):
    complete = False
    while complete == False:
        address = input(f"Please enter {ip_or_sub} address: ")
        octet = 1
        add = {}
        num = ""
        out_of_range = False

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
                if values < 0 or values > 255:
                    print(f'"{values}" is out of range (0 - 255 only)')
                    out_of_range = True

            if out_of_range == False: #outside of for to check if num is out of range
                return add
                complete = True



        except TypeError:
            print('The address must be formatted: XXX.XXX.XXX.XXX (ex: 192.168.1.1)')

        except ValueError:
            print('The address must be formatted: XXX.XXX.XXX.XXX (ex: 192.168.1.1)')


my_ip = make_octets('an IP','ip')
my_subnet = make_octets('a Subnet Mask','subnet_mask')

printed_network_add = ''
printed_broadcast = ''
printed_first_usable = ''
printed_last_usable = ''
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

    if sub_size != 1 and subs == 'oct4':
        printed_first_usable += str(starting_add+1) + '.'
    elif subs == 'oct1' and first_add == int(0):
        printed_first_usable += str(starting_add + 1) + '.'
    else:
        printed_first_usable += str(starting_add) + '.'

    if subs == 'oct1' and first_add == int(0):
        printed_network_add += str(starting_add+1) + '.'
    else:
        printed_network_add += str(starting_add) + '.'

    printed_broadcast += str(broadcast) + '.'

    if subs == 'oct4':
        printed_last_usable += str(broadcast -1)

    else:
        printed_last_usable = printed_broadcast

printed_network_add = printed_network_add[:-1]
printed_broadcast = printed_broadcast[:-1]
printed_first_usable = printed_first_usable[:-1]
printed_last_usable = printed_last_usable # left off -1 so it doesn't subtract last number from last octet

print(f"This is your network address: {printed_network_add}")
print(f"This is your first usable address: {printed_first_usable}")
print(f"This is your last usable address: {printed_last_usable}")
print(f"This is your broadcast address: {printed_broadcast}")



















