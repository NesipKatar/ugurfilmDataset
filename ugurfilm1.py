import requests
from bs4 import BeautifulSoup
link = "https://ugurfilm3.com/page"
for sayi in range(415):
    try:
        sayi+=1
        link=link+"/"+str(sayi)
        print(link)
        icerik=requests.get(link)
        soup = BeautifulSoup(icerik.content, "html.parser")
        info=soup.find_all("a",{'class':'resim'})
        for ic in info:

            gel=ic.get("href")
            print(gel)
            icerik=requests.get(gel)
            soup = BeautifulSoup(icerik.content, "html.parser")
            info=soup.find("div",{'class':'bilgi'})
            #print((info.p.text.split())[1])
            hep=info.find_all("p")
            bir=info.h2.text
            bir=bir.replace(",","")
            bir=bir.strip() 
            print(bir)
            v=","
            say=0
            for i in hep:
                say+=1
                if say==1:
                    iki=i.text.split()[1:]
                    ham=""
                    for cek in iki:
                        ham+=cek
                        ham+=" "
                    iki=ham
                    iki=iki.replace(",","")
                    iki=iki.strip()
                    print(iki)
                elif say==2:
                    uc=i.text.split()[1:]
                    ham=""
                    for cek in uc:
                        ham+=cek
                        ham+=" "
                    uc=ham
                    uc=uc.replace(",","")
                    uc=uc.strip()
                    print(uc)
                elif say==3:
                    dort=i.text
                    dort=dort.replace(",","")
                    dort=dort.strip()
                    print(dort)
                elif say==4:
                    bes=i.text.split()[1:]
                    ham=""
                    for cek in bes:
                        ham+=cek
                        ham+=" "
                    bes=ham
                    bes=bes.replace(",","")
                    bes=bes.strip()
                    print(bes)
                elif say==5:
                    alti=i.text.split(":")[1:]
                    ham=""
                    for cek in alti:
                        ham+=cek
                        ham+=" "
                    alti=ham
                    alti=alti.replace(",","")
                    alti=alti.strip()
                    print(alti)
                elif say==6:
                    yedi=i.text.split()[1:]
                    ham=""
                    for cek in yedi:
                        ham+=cek
                        ham+=" "
                    yedi=ham
                    yedi=yedi.replace(",","")
                    yedi=yedi.strip()
                    print(yedi)
            son=bir+v+iki+v+dort+v+uc+v+bes+v+yedi+v+alti
            dosya = open("ugurfilm3.txt","a",encoding="utf-8")
            dosya.write(son+"\n")
            print(son)
            link = "https://ugurfilm3.com/page"
    except(AttributeError,ImportError):
        continue
    finally:
        continue
dosya.close()









