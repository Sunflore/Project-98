def SFD():
    s1=input('enter the file name')
    s2=input('enter the file name')
    
with open(s1, 'r') as a:
    dA=a.read()
with open(s2, 'r') as a:
    dB=a.read()
with open(s1, 'w') as a:
    a.write(s2)
with open(s2, 'w') as a:
    a.write(s1)

SFD()