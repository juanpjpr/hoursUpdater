from programin import guardarHoras


def lectura():

    f = open("reporte.txt", "r")
    user = f.readline().rstrip()
    psw = f.readline().rstrip()
    isue = f.readline().rstrip()
    hs = f.readline().rstrip()
    coment = f.readline().rstrip()

    f.close()

    a = []

    a.append(user)
    a.append(psw)
    a.append(isue)
    a.append(hs)
    a.append(coment)
 
    return a


def last():
    f = open("last.txt", "r")

    stats = []
    stats.append(f.readline())
    stats.append(f.readline())

    f.close()
    return stats


def userOk():
    f = open("reporte.txt", "r")

    a = f.seekable()
  
    if a == False:
        return False
    else:
        return True
    f.close()

def add(user, pwd):
    f = open("reporte.txt", "w")

    f.write(user+"\n")
    f.write(pwd)

    f.close()
