# Assignment 1 Python, Income predictor, Rory Hayes, C12362996

# globals

FNAME = "datatest.txt" 

totHgh = totLow = totCount = 0 # 'totCount' is total of 'adults' (used) in 'study' here

avgAge = 0 # to sum and then hold average age
avgNum = 0 # to sum and then hold average education number
avgGan = 0 # to sum and then hold average capital gain
avgLss = 0 # to sum and then hold average capital loss
avgHrs = 0 # to sum and then hold average hours per week

#functions
#fuction to find the number of above and below 50k, and above or below the average a class
def getNumHghNumLow( i, avg ):

    with open( FNAME ) as f:

        numLow = numHgh = 0

        numHgh2 = numLow2 = 0

        for line in f:

            items = line.rstrip().split( ', ' )

            if len(items) > 14:
                
                if items[14] == '>50K':
                    
                    if float(items[i]) > avg:
                        numHgh += 1
                    else:
                        numLow += 1

                else:
                    if float(items[i]) > avg:
                        numHgh2 += 1
                    else:
                        numLow2 += 1                    

    return numHgh, numLow, numHgh2, numLow2


#function to get the distribution fo above and below for a class
def getDistribution( classes, classIndex, counts, counts2 ):

    with open( FNAME ) as f:

        for line in f:

            items = line.rstrip().split( ', ' )

            if len(items) > 14:

                for i in range(len(classes)):

                    if items[14] == '>50K':

                        if classes[i] == items[classIndex]:

                            counts[i] += 1 # increment count for this class

                    else:

                        if classes[i] == items[classIndex]:

                            counts2[i] += 1 # increment count for this class



#functoin to determine if item is above or below average
def myTest( items ):

    score = 0.0

    if float(items[0]) > avgAge:

        score += pAge

    if float(items[4]) > avgNum:

        score += pEdNum

    if int(items[10]) > 0:

        score += pCapGan

    if int(items[11]) == 0:

        score += (1-pCapLos)

    if float(items[12]) > 39:

        score += pHrs

    if score > 0.0: return True

    else: return False



#First pass to get all averages needed
with open( FNAME ) as f:

    for line in f:

        # strip off white-space (new-line, etc) at end,
        # then split into Python list (of items) on ', '
        items = line.rstrip().split( ', ' )

        # note: at end of file 2 (some) lines are blank, ...
        # so, just use lines that have (at least) 15 data-fields
        if len(items) > 14:

            #recall '0' is index of 1st data field, so '14' is index of 15th
            if items[14] == '>50K':
                totHgh += 1
            else:
                totLow += 1

            avgAge += int(items[0]) # update sum so can get average
            avgNum += int(items[4]) # update sum so can get average
            avgGan += int(items[10])
            avgLss += int(items[11]) 
            avgHrs += int(items[12])

print( 'Toatl above 50k =', totHgh )
print( 'Total below 50K =', totLow )

totCount = totHgh+totLow

print( 'Above + Below = total count =', totCount )
print( 'Above / Total Count = {:.3f}'.format( totHgh / totCount ) )

avgAge /= totCount

print( 'Average Age = {:.2f}'.format( avgAge ) )

avgNum /= totCount

print( 'Average Educatoin Number = {:.2f}'.format( avgNum ) )

avgGan /= totCount

print( 'Average Capital Gain = {:.2f}'.format( avgGan ) )

avgLss /= totCount

print( 'Average Capital Loss = {:.2f}'.format( avgLss ) )

avgHrs /= totCount

print( 'Average Hours A Week  = {:.2f}'.format( avgHrs) )


#2nd pass Ages... 
print( '\nDistribution of >50K with ages either side of mean age = {:.2f}.'.format( avgAge ) )

numHgh, numLow, numHgh2, numLow2 = getNumHghNumLow( 0, avgAge )

pAge = numHgh/totHgh

print( '{:.3f}'.format(pAge), ' numHgh =', numHgh, 'ages greater than {:.2f}'.format(avgAge) )
print( 'numLow =', numLow )
print( 'numHgh2 =', numHgh2, 'ages greater than {:.2f}'.format(avgAge) )
print( 'numLow2 =', numLow2 )


#3rd pass Education Number... 
print( '\nDistribution of >50K with ed. num.'\

       ' either side of mean = {:.2f}.'.format( avgNum ) )

numHgh, numLow, numHgh2, numLow2 = getNumHghNumLow( 4, avgNum )

pEdNum = numHgh/totHgh

print( '{:.3f}'.format(pEdNum), ' numHgh =', numHgh, 'education numbers greater than {:.2f}'.format(avgNum) )
print( 'numLow =', numLow )
print( 'numHgh2 =', numHgh2, 'education numbers greater than {:.2f}'.format(avgNum) )
print( 'numLow2 =', numLow2 )


#4th pass work classes ...
workClasses = [ 'Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov',

                'Local-gov', 'State-gov', 'Without-pay', 'Never-worked',

                '?' ]

workCounts = [ 0 ]*len(workClasses) #get Python list of 9 int's all set to 0 to start

workCounts2 = [ 0 ]*len(workClasses)

getDistribution( workClasses, 1, workCounts, workCounts2 )

print( '\nDistribution of >50K among all', len(workClasses) , 'possible work classes.' )                      

i = 0; totCount = 0; totCount2 = 0  # re-set to zero                  

for count, count2 in zip(workCounts, workCounts2):

    print( i, count, '{:.3f}'.format(count/totHgh), count2, workClasses[i] )

    totCount += count; totCount2 += count2

    i += 1


#5th pass married classes ...
marriedClasses = [ 'Married-civ-spouse', 'Divorced', 'Never-married', 'Separated',

                   'Widowed', 'Married-spouse-absent', 'Married-AF-spouse' ]

marriedCounts = [ 0 ]*len(marriedClasses) #get Python list of 7 int's all set to 0 to start

marriedCounts2 = [ 0 ]*len(marriedClasses)

getDistribution( marriedClasses, 5, marriedCounts, marriedCounts2 )

print( '\nDistribution of >50K among all', len(marriedClasses) , 'possible married classes.' )                      

i = 0; totCount = 0; totCount2 = 0  # re-set to zero                    

for count, count2 in zip(marriedCounts, marriedCounts2):

    print( i, count, '{:.3f}'.format(count/totHgh), count2, marriedClasses[i] )

    totCount += count; totCount2 += count2

    i += 1


#6th pass occupation classes ...
occupationClasses = [ 'Tech-support', 'Craft-repair', 'Other-service', 'Sales',

                      'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct',

                      'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv',

                      'Protective-serv', 'Armed-Forces', '?' ]

occupationCounts = [ 0 ]*len(occupationClasses) #get Python list of 15 int's all set to 0 to start

occupationCounts2 = [ 0 ]*len(occupationClasses)

getDistribution( occupationClasses, 6, occupationCounts, occupationCounts2 )

print( '\nDistribution of >50K among ', len(occupationClasses) , ' occupation classes.' )                      

i = 0; totCount = 0; totCount2 = 0  # re-set to zero                   

for count, count2 in zip(occupationCounts, occupationCounts2):

    print( i, count, '{:.3f}'.format(count/totHgh), count2, occupationClasses[i] )

    totCount += count; totCount2 += count2

    i += 1


#7th pass relationship classes ...
relationshipClasses = [ 'Wife', 'Own-child', 'Husband', 'Not-in-family',

                        'Other-relative', 'Unmarried' ]

relationshipCounts = [ 0 ]*len(relationshipClasses) #get Python list of 6 int's all set to 0 to start

relationshipCounts2 = [ 0 ]*len(relationshipClasses)

getDistribution( relationshipClasses, 7, relationshipCounts, relationshipCounts2  )

print( '\nDistribution of >50K among ', len(relationshipClasses) , ' relationship classes.' )                      

i = 0; totCount = 0; totCount2 = 0  # re-set to zero                   

for count, count2 in zip(relationshipCounts, relationshipCounts2):

    print( i, count, '{:.3f}'.format(count/totHgh), count2, relationshipClasses[i] )

    totCount += count; totCount2 += count2

    i += 1


#8th pass race classes ...

raceClasses = [ 'White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black' ]

raceCounts = [ 0 ]*len(raceClasses) #get Python list of 5 int's all set to 0 to start

raceCounts2 = [ 0 ]*len(raceClasses)

getDistribution( raceClasses, 8, raceCounts,  raceCounts2 )

print( '\nDistribution of >50K re. ', len(raceClasses) , ' race classes.' )                      

i = 0; totCount = 0; totCount2 = 0  # re-set to zero                   

for count, count2 in zip(raceCounts, raceCounts2):

    print( i, count, '{:.3f}'.format(count/totHgh), count2, raceClasses[i] )

    totCount += count; totCount2 += count2

    i += 1


#9th pass sex classes ...
sexClasses = [ 'Female', 'Male' ]

sexCounts = [ 0 ]*len(sexClasses) #get Python list of 2 int's all set to 0 to start

sexCounts2 = [ 0 ]*len(sexClasses)

getDistribution( sexClasses, 9, sexCounts, sexCounts2 )

print( '\nDistribution of >50K among all', len(sexClasses) , 'possible sex classes.' )                      

i = 0; totCount = 0; totCount2 = 0  # re-set to zero                    

for count, count2 in zip(sexCounts, sexCounts2):

    print( i, count, '{:.3f}'.format(count/totHgh), count2, sexClasses[i] )

    totCount += count; totCount2 += count2

    i += 1


#10th pass captial gain... 
print( '\nDistribution of >50K with capital gain.' )

numHgh, numLow, numHgh2, numLow2 = getNumHghNumLow( 10, 0 )

pCapGan = numHgh/totHgh

print( '{:.3f}'.format(pCapGan), ' numHgh =', numHgh, 'with capital gain' )
print( 'numLow =', numLow )
print( 'numHgh2 =', numHgh2, 'with capital gain' )
print( 'numLow2 =', numLow2 )


#11th pass captial loss... 
print( '\nDistribution of >50K with capital loss.' )

numHgh, numLow, numHgh2, numLow2 = getNumHghNumLow( 11, 0 )

pCapLos = numHgh/totHgh

print( '{:.3f}'.format(pCapLos), ' numHgh =', numHgh, 'with capital loss' )
print( 'numLow =', numLow )
print( 'numHgh2 =', numHgh2, 'with capital loss' )
print( 'numLow2 =', numLow2 )


#12th pass hours per week...
print( '\nDistribution of >50K with hours per week'\

       ' greater than 39.' )

numHgh, numLow, numHgh2, numLow2 = getNumHghNumLow( 12, 39 )

pHrs = numHgh/totHgh

print( '{:.3f}'.format(pHrs), ' numHgh =', numHgh, 'hours per week greater than {:.2f}'.format(39) )
print( 'numLow =', numLow )
print( 'numHgh2 =', numHgh2, 'hours per week greater than {:.2f}'.format(39) )
print( 'numLow2 =', numLow2 )


# test and report ...
with open( FNAME ) as f:

    accuracy = 0
    numHgh = numLow = 0
    numHgh2 = numLow2 = 0
    numHgh3 = numLow3 = 0

    for line in f:

        items = line.rstrip().split( ', ' )

        if len(items) > 14:

            if items[14] == '>50K':

                if items[14] == '>50K':
                    numHgh += 1 #actual
                else:
                    numLow += 1

                if myTest( items ):
                    numHgh2 += 1 #predicted
                else:
                    numLow2 += 1

                if myTest( items ) and items[14] == '>50K':
                    numHgh3 += 1 #predicted and actual
                else:
                    numLow3 += 1

                    
accuracy = (numHgh2 / numHgh+numLow) * 100
print( '\nActual =', numHgh, 'total =', numHgh+numLow )
print( 'Predicted =', numHgh2, 'total =', numHgh2+numLow2 )
print( '\nThe % accuracy of >50k is {:.3f}'.format(accuracy) )
