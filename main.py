
def web_page(scr):

     html1 ="<html> <head>" 
     html2="<script>window.onload=function(){alert('You Have Entered Wrong Username Or Password')}</script>" 
     html3="<link rel='icon' href='data:,'> <style>@font-face{font-family:'Source Sans Pro';font-style:normal;font-weight:200;src:url(https://fonts.gstatic.com/s/sourcesanspro/v19/6xKydSBYKcSV-LCoeQqfX1RYOo3i94_wlxdr.ttf) format('truetype')}@font-face{font-family:'Source Sans Pro';font-style:normal;font-weight:300;src:url(https://fonts.gstatic.com/s/sourcesanspro/v19/6xKydSBYKcSV-LCoeQqfX1RYOo3ik4zwlxdr.ttf) format('truetype')}*{box-sizing:border-box;margin:0;padding:0;font-weight:300}body{font-family:'Source Sans Pro',sans-serif;color:#fff;font-weight:300}body ::-webkit-input-placeholder{font-family:'Source Sans Pro',sans-serif;color:#fff;font-weight:300}body :-moz-placeholder{font-family:'Source Sans Pro',sans-serif;color:#fff;opacity:1;font-weight:300}body ::-moz-placeholder{font-family:'Source Sans Pro',sans-serif;color:#fff;opacity:1;font-weight:300}body :-ms-input-placeholder{font-family:'Source Sans Pro',sans-serif;color:#fff;font-weight:300}.wrapper{background:#50a3a2;background:linear-gradient(to bottom right,#50a3a2 0,#53e3a6 100%);position:absolute;top:50%;left:0;width:100%;height:500px;margin-top:-250px;overflow:hidden}.wrapper.form-success .container h1{transform:translateY(85px)}.container{max-width:600px;margin:0 auto;padding:80px 0;height:400px;text-align:center}.container h1{font-size:50px;transition-duration:1s;transition-timing-function:ease-in-put;font-weight:900}form{padding:60px 0;position:relative;z-index:2}form input{-webkit-appearance:none;-moz-appearance:none;appearance:none;outline:0;border:1px solid rgba(255,255,255,.4);background-color:rgba(255,255,255,.2);width:250px;border-radius:3px;padding:10px 15px;margin:0 auto 10px auto;display:block;text-align:center;font-size:18px;color:#fff;transition-duration:.25s;font-weight:300}form input:hover{background-color:rgba(255,255,255,.4)}form input:focus{background-color:#fff;width:300px;color:#53e3a6}form button{-webkit-appearance:none;-moz-appearance:none;appearance:none;outline:0;background-color:#fff;border:0;padding:10px 15px;color:#53e3a6;border-radius:3px;width:250px;cursor:pointer;font-size:18px;transition-duration:.25s}form button:hover{background-color:#f5f7f9}.bg-bubbles{position:absolute;top:0;left:0;width:100%;height:100%;z-index:1}.bg-bubbles li{position:absolute;list-style:none;display:block;width:40px;height:40px;background-color:rgba(255,255,255,.15);bottom:-160px;-webkit-animation:square 25s infinite;animation:square 25s infinite;transition-timing-function:linear}.bg-bubbles li:nth-child(1){left:10%}.bg-bubbles li:nth-child(2){left:20%;width:80px;height:80px;-webkit-animation-delay:2s;animation-delay:2s;-webkit-animation-duration:17s;animation-duration:17s}.bg-bubbles li:nth-child(3){left:25%;-webkit-animation-delay:4s;animation-delay:4s}.bg-bubbles li:nth-child(4){left:40%;width:60px;height:60px;-webkit-animation-duration:22s;animation-duration:22s;background-color:rgba(255,255,255,.25)}.bg-bubbles li:nth-child(5){left:70%}.bg-bubbles li:nth-child(6){left:80%;width:120px;height:120px;-webkit-animation-delay:3s;animation-delay:3s;background-color:rgba(255,255,255,.2)}.bg-bubbles li:nth-child(7){left:32%;width:160px;height:160px;-webkit-animation-delay:7s;animation-delay:7s}.bg-bubbles li:nth-child(8){left:55%;width:20px;height:20px;-webkit-animation-delay:15s;animation-delay:15s;-webkit-animation-duration:40s;animation-duration:40s}.bg-bubbles li:nth-child(9){left:25%;width:10px;height:10px;-webkit-animation-delay:2s;animation-delay:2s;-webkit-animation-duration:40s;animation-duration:40s;background-color:rgba(255,255,255,.3)}.bg-bubbles li:nth-child(10){left:90%;width:160px;height:160px;-webkit-animation-delay:11s;animation-delay:11s}@-webkit-keyframes square{0%{transform:translateY(0)}100%{transform:translateY(-700px) rotate(600deg)}}@keyframes square{0%{transform:translateY(0)}100%{transform:translateY(-700px) rotate(600deg)}}</style> <script>$('#login-button').click(function(e){e.preventDefault(),$('form').fadeOut(500),$('.wrapper').addClass('form-success')});</script> <meta name='viewport' content='width=device-width, initial-scale=1'> </head><body><div class='wrapper'><div class='container'><h1>Welcome</h1> <form action='/' method='get' class='form'><input type='text' placeholder='Username' name='loginname' required><input type='password' placeholder='Password' name='loginpwd' required><button type='submit' id='login-button'>Login</button></form></div><ul class='bg-bubbles'><li></li><li></li><li></li><li></li><li></li><li></li><li></li><li></li><li></li><li></li></ul></div></body></html>"
     if (scr==True):
         html=html1+html2+html3
     else:
        html=html1+html3
        
     return html
def opendoor():
     led.value(1)
     time.sleep(0.5)
     led.value(0)
     
error = False   
rtc = RTC() # initialize the RTC
ntptime.settime() # set the RTC's time using ntptime
print(rtc.datetime()) # print the current time from the RTC
date = str(rtc.datetime())
print(date)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  try:
    if gc.mem_free() < 102000:
      m = gc.collect()
      n = gc.mem_free()
      #print(m)
      #print(n)
      conn, addr = s.accept()
      conn.settimeout(3.0)
      print('Got a connection from client')
      request = conn.recv(1024)
      print(request)
      print("request received")
      #conn.settimeout(3.0)
      #print('Content = %s' % str(request))
      request = str(request)
      #print(request)
      signuppos = request.find('/?username')
      loginpos = request.find('/?loginname')
      print(signuppos)
      print(loginpos)
      #print("signupname & loginname position",signupname,loginname)
      if (signuppos==6):
        a = request.rsplit(' ')
        b = a[1]
        c = b.split('=')
        d = c[1]
        e = d.split('&')
        reqname = e[0]
        print(reqname)
        f = c[2]
        g =f.split('&')
        reqpwd =g[0]
        print(reqpwd)
        h = c[3]
        i =h.split('&')
        reqcpwd = i[0]
        print(reqcpwd)
        print(reqname,reqpwd,reqcpwd)
        file = open("signupdetails.txt","a")
        file.write("\n"+reqname+' '+reqpwd+' '+reqcpwd)
        print("write success")
        file.close()
        print("signup connection closed")
      elif (loginpos==6):
        a1 = request.split(' ')
        a2 = a1[1]
        a3 = a2.split('=')
        a4 = a3[1]
        a5 = a4.split('&')
        a6 = a3[2]
        a7 = a6.split('&')
        Lname = a5[0]
        Lpwd = a7[0]
        print(Lname,Lpwd,date)
        error = True
        with open("signupdetails.txt","r") as f:
            for i in f:
                name = i.split(' ')
                if name[0] == Lname and name[1] == Lpwd:
                    print("for loop name",name)
                    logfile = open('logindetails.txt','a')
                    logfile.write('\n'+Lname+' '+Lpwd+' '+date)
                    print("loged in successful")
                    error =False
                    opendoor()
                    break
            print("for loop completed")
        if (error==False):
            print("password matched")
        else:
            print("password not matched")
    
      response = web_page(error)
      conn.send('HTTP/1.1 200 OK\n')
      conn.send('Content-Type: text/html\n')
      conn.send('Connection: close\n\n')
      conn.sendall(response)
      conn.close()
  except OSError as e:
    conn.close()
    print('Connection closed')

