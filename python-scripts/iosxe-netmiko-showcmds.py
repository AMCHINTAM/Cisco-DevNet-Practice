from netmiko import ConnectHandler



ios_xe_latest = {
             "device_type": "cisco_ios",
             "ip": "sandbox-iosxe-latest-1.cisco.com",
             "username": "admin",
             "password": "C1sco12345"            
          }
net_connect = ConnectHandler(**ios_xe_latest)

with open('show_output.txt', 'a') as f:
    output = net_connect.send_command ('show run')
    print(output, file=f)
    output = net_connect.send_command ('show ip interface brief')
    print(output, file=f)
    output = net_connect.send_command ('show ip route')
    print(output, file=f)
 

net_connect.disconnect
