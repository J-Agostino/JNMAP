import nmap

welcome = "J-NMAP is for those who are lazy enough to don't write (or research) a single line and want to discover hosts and/or open ports\n**Remember to have nmap installed"
print(welcome)
print('-------------------------')


menu = ['Select a scan type:','1- Host discovery','2- Scan all TCP ports (-p-)','3- Fast TCP scan (-F)', '4- Scan all UDP ports #This will take time', '5- TCP/UDP scan', 'Run the script as root for option 4 and 5']
for pmenu in menu:
	print(pmenu)
print('-------------------------')

option_select = input('Number: ')
print('\n')

### option 1 discovery

if option_select == '1':
    discovery = nmap.PortScanner()
    discovery.scan(hosts='192.168.1.0/24', arguments='-PR')

    # Print the hosts that are up
    for host in discovery.all_hosts():
        if discovery[host].state() == 'up':
            print(f"Host: {host} is up")

### option 2 all tcp

elif option_select == '2':
	iphost = input('IP to scan: ')
	tcp = nmap.PortScanner()
	tcp.scan(hosts=iphost, arguments='-sT -p-')	
	for host in tcp.all_hosts():
		if tcp[host].state() == 'up':
			print(f"Host: {host}")
			for port in tcp[host]['tcp'].keys():
				port_data = tcp[host]['tcp'][port]
				print(f"Port: {port}\tState: {port_data['state']}\tService: {port_data['name']}")

### option 3 fast tcp

elif option_select == '3':
    iphost = input('IP to scan: ')
    tcpf = nmap.PortScanner()
    tcpf.scan(hosts=iphost, arguments='-sT -F')

    for host in tcpf.all_hosts():
        if tcpf[host].state() == 'up':
            print(f"Host: {host}")
            if 'tcp' in tcpf[host]:
                for port in tcpf[host]['tcp'].keys():
                    port_data = tcpf[host]['tcp'][port]
                    print(f"Port: {port}\tState: {port_data['state']}\tService: {port_data['name']}")
            else:
                print("No TCP ports detected.")

 
### option 4 udp

elif option_select == '4':
	iphost = input('IP to scan: ')
	udp = nmap.PortScanner()
	udp.scan(hosts=iphost, arguments='-sU -p-')	
	for host in udp.all_hosts():
		if udp[host].state() == 'up':
			print(f"Host: {host}")
			for port in udp[host]['udp'].keys():
				port_data = udp[host]['udp'][port]
				print(f"Port: {port}\tState: {port_data['state']}\tService: {port_data['name']}")

### option 5 all scan

elif option_select == '5':
    iphost = input('IP to scan: ')
    scanner = nmap.PortScanner()
    scanner.scan(hosts=iphost, arguments='-sU -sT -F')

    for host in scanner.all_hosts():
        if scanner[host].state() == 'up':
            print(f"Host: {host}")
            for port in scanner[host]['tcp'].keys():
                port_data = scanner[host]['tcp'][port]
                print(f"Port: {port}\tState: {port_data['state']}\tService: {port_data['name']}")


### option for people who don't care about rules

else:
	print('Select a number from the list')
	
