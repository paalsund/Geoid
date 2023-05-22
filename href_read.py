# -*- coding: cp1252 -*-
# Read GEOID ascii file from Kartverket (ftp://ftp.geodesi.no/HREF2018A_NN2000_EUREF89.gri)
# just writing here to a CSV but may be further processed to a model/grid
# 

# File organized in "data blocks"
# Blocks organized from North to South
# Each block organized West to East
# dE is delta East between each datapoint
# dN is delta North between each block

href = open('C:/temp/HREF/HREF2018A_NN2000_EUREF89.gri','r')
linjer = href.readlines()

# example
# linjer[0] = '   57.800000   72.000000    4.000000   32.000000   0.0200000   0.0400000'
# linjer[1] = '\n'
# linjer[2] = '   9999.000 9999.000 9999.000 9999.000 9999.000 9999.000 9999.000 9999.000\n'
# ..
# linjer[89] = '  9999.000 9999.000 9999.000 9999.000 9999.000\n'
# linjer[90] = '\n'
# linjer[91] = '  9999.000 9999.000 9999.000 9999.000 9999.000\n'
#
# 9999.000 is the NODATA-value

# Split first, i.e linjer[0] for grabbing the file parameters
parametre = linjer[0].split()
S =  float(parametre[0])
N =  float(parametre[1])
W =  float(parametre[2])
E =  float(parametre[3])
dN = float(parametre[4])
dE = float(parametre[5])

# Sublist for the actual data
datalinjer = linjer[2:]
# datalinjer is a list, each line is a string
# blocks are stringths with length 46 or 73
# blocks are separated by '\n' (length 1)


# File for writing
resultatfil = open('C:/temp/HREF/test2.csv','w')
resultatfil.write('Lat Long GeoideH\n')


# Loop over blocks
Nord = N
Ost = W
for linje in datalinjer:
    # len(linje) > 1 for all lines in a block
    # For each bloch the North/N is constant
    # for each datapoint East is incremented by dE
    if len(linje) > 1:
        words = linje.split()
        for word in words:
            GeoideH = float(word)
            resultatfil.write('%5.3f %5.3f %5.3f\n' % (Nord, Ost, GeoideH))
            ## print North, East, GeoideH
            Ost = Ost + dE
    # len(linje) = 1 for the line separating each block
    # Resetting the Eastvalue to W
    # North value decremented by -dN 
    if len(linje) == 1:
        Nord = Nord - dN
        Ost = W
        
# Lukker filer
href.close()
resultatfil.close()

# Ferdig
print (' Done')
