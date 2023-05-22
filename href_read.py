# -*- coding: cp1252 -*-
# Lese GEOIDE ascii filen fra Kartverket (finnes her, ftp://ftp.geodesi.no/HREF2018A_NN2000_EUREF89.gri)
# Skriver til en CSV fil som kan prosesseres videre i ArcGIS til en modell/grid
# 

# Filen er organisert i "blokker" med data
# Blokkene er organisert fra N til S
# Hver blokk er organisert fra Vest til �st
# dE som forskjell i �st-verdi mellom hvert datapunkt
# dN som forskjell i nord-verdi mellom hver "blokk"

href = open('C:/temp/HREF/HREF2018A_NN2000_EUREF89.gri','r')
linjer = href.readlines()

# linjer[0] = '   57.800000   72.000000    4.000000   32.000000   0.0200000   0.0400000'
# linjer[1] = '\n'
# linjer[2] = '   9999.000 9999.000 9999.000 9999.000 9999.000 9999.000 9999.000 9999.000\n'
# ..
# linjer[89] = '  9999.000 9999.000 9999.000 9999.000 9999.000\n'
# linjer[90] = '\n'
# linjer[91] = '  9999.000 9999.000 9999.000 9999.000 9999.000\n'
#
# 9999.000 er NODATA-verdien

# Splitter f�rste linje, dvs linjer[0] for � ta ut parametre
parametre = linjer[0].split()
S =  float(parametre[0])
N =  float(parametre[1])
W =  float(parametre[2])
E =  float(parametre[3])
dN = float(parametre[4])
dE = float(parametre[5])

# Subliste kun for dataverdiene
datalinjer = linjer[2:]
# datalinjer er en liste, der hver rad i lista er en streng
# blokkene har strenger med lengde 46 eller 73
# blokkene skilles av streng '\n' med lengde 1 (en)


# Lager en fil for � skrive resultatene til
resultatfil = open('C:/temp/HREF/test2.csv','w')
resultatfil.write('Lat Long GeoideH\n')


# Loop over blokkene
Nord = N
Ost = W
for linje in datalinjer:
    # len(linje) > 1 for alle linjene i en blokk
    # I hver blokk er Nord-verdien konstant
    # men hvert datapunkt skal inkrementeres fra Vest
    # med verdien dE
    if len(linje) > 1:
        words = linje.split()
        for word in words:
            GeoideH = float(word)
            resultatfil.write('%5.3f %5.3f %5.3f\n' % (Nord, Ost, GeoideH))
            ## print Nord, Ost, GeoideH
            Ost = Ost + dE
    # len(linje) = 1 for linjen som skiller hver blokk
    # Resetter da �stverdien til utgangspunktet W
    # Nordverdien dekrementeres med -dN 
    if len(linje) == 1:
        Nord = Nord - dN
        Ost = W
        
# Lukker filer
href.close()
resultatfil.close()

# Ferdig
print (' Done')
