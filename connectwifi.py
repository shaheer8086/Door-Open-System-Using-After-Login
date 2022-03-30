print('this is connectwifi.py')
def connect():
    import network
    print('inside connect function')
 
    ssid = "MilestoneFiber"
    password =  "sup@milestoneit.net"
 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        print(station.ifconfig())
        return
 
    station.active(True)
    station.ifconfig(('192.168.10.71','255.255.255.0','192.168.10.1','8.8.8.8'))
    station.connect(ssid,password)
     
 
    while station.isconnected() == False:
        pass
    print("Connection successful")
    print(station.ifconfig())
    
def disconnect():
    import network
    station = network.WLAN(network.STA_IF)
    station.disconnect()
    station.active(False)


