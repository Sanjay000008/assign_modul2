a=input("Enter String:")
pn=a.find('not')
pp=a.find('poor')
if pn < pp:
    print(a[:pn] + "good")