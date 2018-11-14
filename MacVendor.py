#!/usr/bin/python
#Copyright(c) 2018: By Oseid Aldary
#      MacVendor  : Get Device Vendor Company Name By He Mac Address
#      Coded BY   : Oseid Aldary
#      Follow Me  : github.com/Oseid
#
#Libraries
import sys,urllib2,requests,json,codecs,socket
# MacVendor Class
class MacVendor:
  # Check Internet Connection..
  def cnet(self):
    server = "www.google.com"
    try:
      ip = socket.gethostbyname(server)
      con = socket.create_connection((ip, 80), 2)
      return True
    except socket.error:
      pass
    return False
  # Get Vendor Company Name By Mac: Function
  def mac(self, mac):
    if self.cnet() !=True:
       # Here Your Not Connected To Internet !
       print("[!] Error: Please Check Internet Connection !!!")
       exit(1)
    try:
      #API base url,you can also use https if you need
      url = "http://macvendors.co/api/"
      request = urllib2.Request(url+mac, headers={'User-Agent' : "API Browser"})
      response = urllib2.urlopen( request )
      #Fix: json object must be str, not 'bytes'
      reader = codecs.getreader("utf-8")
      obj = json.load(reader(response))
      #Return Company vendor Name
      return obj['result']['company']
    except ValueError:
      # The Mac Address Is Not Correct !!!
      return "\n[!] Error: Please Input Correct Mac Address !!!"
    except KeyError: # Try Other Website Datebace
        response  = requests.get(url="http://api.macvendors.com/%s"%(mac))
        if "Page not found" not in response.text:
	 #Return Vendor Company Name
          return response.text
        else:
          return "\n[!] Error: Unknown Vendor Company Name Of MAC[ {} ]".format(mac)
Vendor = MacVendor()
if len(sys.argv) ==2:
 if sys.argv[1] !=None and len(sys.argv[1]) ==17:
	print("\n[>] SOURCE MAC ADDRESS : "+sys.argv[1])
	print("[+] Vendor Company Name: "+Vendor.mac(sys.argv[1]))
	print("")
######################################################################
######################### 	             #########################
#########################    END OF Module   #########################
#########################                    #########################
######################################################################
#This Method by Oseid Aldary
#Have a nice day :)
#GoodBye
