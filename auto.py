import pyautogui as pag
import time

rmkt = [
 [
    "chibi_chatlieu",
    "chibi_sale1",
    "chibi_anhthat",
    "chibi_sale2"     
 ],
 [
    "mica_chatlieu",
    "mica_sale1",
    "mica_anhthat",
    "mica_sale2"     
 ],
 [
   "tranhcat_chatlieu",
   "tranhcat_sale1",
   "tranhcat_anhthat",
 ]
]

def auto_rmkt():
   print("Which page do you want to rmkt?\n Type 1 for chibi, 2 for mica, 3 for tranhcat:")
   x=int(input())
   print("Which level rmkt do you want to run?:")
   y=int(input())
   if ((x==3) and (y>3)):
      print("No RMKT4 on tranhcat")
      return 0
   elif(y>4):
      print("Maximum RMKT4")
   else:
      print("How many time do you want to run?:")
      loop = int(input())
      print("move cursor to position (just move, don't click)")
      time.sleep(5)
      pos = pag.position()
      for _ in range (loop):
         pag.click(pos)
         time.sleep(0.2)
         pag.write("/"+rmkt[x-1][y-1])
         time.sleep(0.2)
         pag.hotkey("enter")
         time.sleep(0.2)
         pag.hotkey("enter")
         time.sleep(0.3)
         pag.hotkey("alt", str(y))
         time.sleep(0.3)
         pag.hotkey("alt", str(y+1))
         time.sleep(0.3)
auto_rmkt()
run = input("Do you want to continue? \n(Type Y to continue, other key to exit):")
while run == "Y":
    auto_rmkt()
    run = input("Do you want to continue? \n(Type Y to continue, other key to exit):")
