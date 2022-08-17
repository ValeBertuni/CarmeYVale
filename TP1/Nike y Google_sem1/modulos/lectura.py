def leernike(nomarch):
    archi=open(nomarch, "r")
    for i in range(1):
        aux=archi.readline()
    entero=archi.readlines()
    nikefecha=[];nikepre=[];nikedia=[];nikemes=[]; nikeanioyhora=[]
    for linea in entero:
        linea=linea.rstrip()
        nikef, nikep=linea.split(',')
        nikefecha.append(nikef)
        nikep=float(nikep)
        nikepre.append(nikep)
    for lin in nikefecha:
        niked, nikem, nikeayh=lin.split('/')
        nikedia.append(niked)
        nikemes.append(nikem)
        nikeanioyhora.append(nikeayh)
    return(nikepre)

nikep=leernike("nike.csv")
print("lista de precio:",nikep)