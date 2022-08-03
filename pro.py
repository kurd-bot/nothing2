import os, platform,time
#os.system("clear")
#print("\t 30 April ko All Approvels Remove Krdea jaingy")
#print("\t Users Ko Again Buy Krna pady ga ")
#print("\t Shukriya.....")
#time.sleep(3)
#print("updating again please wait we have some errors")
#exit()
try:
    import requests
except(ImportError):
    os.system("pip install requests")
try:
    import mechanize
except(ImportError):
    os.system("pip install mechanize")
try:
    import bs4
except(ImportError):
    os.system("pip install bs4")

rana=platform.architecture()[0]
try:
    if rana=="32bit":
        __import__("pro32").mysecurity()
    elif rana=="64bit":
        __import__("rsa").mysecurity()
    else:
        print(" We have issue to launch script")
        exit()
except(AttributeError,OSError,KeyError,IOError):
    if rana == "32bit":
        import pro32
        pro32.mysecurity()
    elif rana == "64bit":
        import rsa
        rsa.mysecurity()
    else:
        print(" We have issue to launch script")
        exit()
