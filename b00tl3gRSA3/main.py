def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# https://www.alpertron.com.ar/ECM.HTM
phi = '23 535847 797352 724952 573669 034185 659271 778047 341695 210256 682267 879124 693873 236827 349936 952222 653425 777804 387847 752421 773866 089054 249115 901360 894302 004293 295595 487404 279379 089783 226518 381764 047980 864944 147767 831316 155295 749824 446787 730149 172429 909115 893444 128881 487811 103327 108447 860366 576909 692957 614050 912612 912731 492480 586874 880000 000000 000000'
phi = int(phi.replace(' ',''))

c = 112012444651822239534436036843409765171568454922856423968021691090225178482798526874099218355953097739059019879878441937660101902467834695130113229766758314086124784802446075459580884680495458314072919383201513020646159267963918859180454159572692262651212463409319260308653302331183451096673806121278301165974681510842459362747428569283932957
n = 23535847862066207342186706983076099588324574498414600241829807293975466820821106898804156842088294863769014275732413119385034385949033225377756590087533138149739328455804855524296659763341299523334009151182246229486116690044616419077192268796392624805388826670296867705254900967211713899829418872438924976820063613375988514881610181494670079191
e = 65537

d = modinv(e, phi)

print hex(pow(c,d,n))[2:-1].decode('hex')
# picoCTF{too_many_fact0rs_4426407}