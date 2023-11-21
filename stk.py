import pyautogui as p
def number(a):
    d={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','20':'twenty'}
    if a in d:
        return d[a]
    else:
        return number(str(int(a)%10))+'teen'
def tens(a):
    d={'2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}
    if(a[-2]=='1'):
        return number(a)
    else:
        if(int(a)%10==0):
            return d[a[-2]]
        elif(a[0]=='0' and a[1]!='0'):
            return number(a[1])
        else:
            return d[str(a[-2])]+number(a[-1])
def hundreds(a):
    if(a[1:]=='00'):
        e='-'
    elif(a[1]=='0' and a[2]!='0'):
        e=number(a[2])
    else:
        e=tens(a[1:])
    if(a[0]=='0'):
        return e
    else:
        h=number(a[0])
    return h+'-hundred-'+e
def thousands(a):
    if(a[1:]=='000'):
        e='-'
    else:
        e=hundreds(a[1:])
    if(a[0]==0):
        return e 
    else:
        t=number(a[0])
    return t+'-thousand-'+e
def tenthousands(a):
    if(a[2:]=='000'):
        return tens(a[0:2])+'-thousand-'
    else:
        if(a[0:2]=='00'):
            return hundreds(a[2:])
        else:
            return tens(a[0:2])+'-thousand-'+hundreds(a[2:])
def lakhs(a):
    if(a[1:]=='00000'):
        return number(a[0])+'lakh'
    else:
        return number(a[0])+'-lakh-'+tenthousands(a[1:])
def tenlakhs(a):
    if(a[2:]=='00000'):
        return tens(a[0:2])+'-lakh-'
    else:
        if(a[0:2]=='00'):
            return tenthousands(a[2:])
        else:
            return tens(a[0:2])+'-lakh-'+tenthousands(a[2:])
def crores(a):
    if(a[1:]=='0000000'):
        return number(a[0])+'-crore-'
    else:
        return number(a[0])+'-crore-'+tenlakhs(a[1:])
def tencrores(a):
    if(a[2:]=='0000000'):
        return tens(a[0:2])+'-crores-'
    else:
        return tens(a[0:2])+'-crore-'+tenlakhs(a[2:])
def billions(a):
    if(a[3:]=='0000000'):
        return hundreds(a[0:3])+'-crores-'
    else:
        return hundreds(a[0:3])+'-crore-'+tenlakhs(a[3:])
def print_word(a):
    if(a<10):
        return number(str(a))
    elif(a<100):
        return tens(str(a))
    elif(a<1000):
        return hundreds(str(a))
    elif(a<10000):
        return thousands(str(a))
    elif(a<100000):
        return tenthousands(str(a))
    elif(a<1000000):
        return lakhs(str(a))
    elif(a<10000000):
        return tenlakhs(str(a))
    elif(a<100000000):
        return crores(str(a))
    elif(a<1000000000):
        return tencrores(str(a))
    elif(a<10000000000):
        return billions(str(a))
    else:
        return "Limit Reached"
p.alert(title="Number_to_Word",text="Numbers_Limited_to_Trillion",button='ok')
a=p.prompt(title="Number_to_Word/Input",text="Enter the Number:")
if(a!=None):
    p.alert(title="Number_to_Word/Result",text=print_word(int(a)))