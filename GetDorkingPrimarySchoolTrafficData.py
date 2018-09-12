'''     numpy is making some warnings. 
        internet says not to worry about it. 
        so I'm going to make the python ignore them!
'''

import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88")
import pandas as pd 
from pandas import ExcelWriter
from pandas import ExcelFile


'''
Notes: 
    
    My first stab at this script missed a few schools. 
    
    * make a list of the primary schools.
    * use that list to make sure that you have data from all the schools

    * It would be interesting to think about suppressed cycling demand in parent    s that take the train to work.

    * It would be interresting to think about what this means for suppresd 
    demand for the train station in general. 

'''


xl = pd.read_excel('Primary-Table_1_deleted_row1-3.xlsx' )

# bellow gets you column headings.

#print('Colum headings:')
#print(xl.columns)

print('Summary of 2005 primary school travel data')

for i in xl.index: 
        namestr = xl['School_name'][i]
        name = str(namestr)

        # look for 2005 numbers

        year =  xl['Year'][i]
        #year = int(yearstr)
        

        # % taking car to school
        carstr = xl['Car'][i]
        car = float(carstr)
        carsharestr = xl['Carshare'][i]
        carshare = float(carsharestr)
        
        CarTotal = carshare + car
        
        # % taking bus to school

        PublicBusstr = xl['Public Bus'][i]
        PublicBuss = float(PublicBusstr)

        SchoolBusstr = xl['School Bus'][i]
        SchoolBuss = float(SchoolBusstr)
        if SchoolBuss == float and PublicBuss == float: 
            BussTotal = PublicBuss + SchoolBuss
        elif PublicBuss == float and SchoolBuss != float: 
            BussTotal = PublicBuss
        elif PublicBuss != float and SchoolBuss == float:
            BussTotal = SchoolBuss
        elif PublicBuss != float and SchoolBuss != float: 
            BussTotal = 0
        else: 
            print('Buss Error: not processing bus datat')

        '''
        haven't coded the other side of this. 
        if public == 0 and SchoolBuss > 0:
            make BussTotal = SchoolBuss
        '''

        if BussTotal == 0 and PublicBuss != 0: 
            BussTotal = PublicBuss
            # This is a hack to get it to work. 

        # % walking or cycling to school

        Cyclestr = xl['Cycle'][i]
        Cycle = float(Cyclestr)
        
        Footstr = xl['Foot'][i]
        Foot = float(Footstr)

        ActiveTotal = Cycle + Foot

        #Getting school name for the schools that have 'Dorking'.
        # and from 2005
        if "Dorking" in name and year == 2005:
            #Car bit is working 

            print('School Name:',name,'Year:', year) 
            
            print('CarTotal:',CarTotal)
            print('car:', car)
            print('carshare:', carshare)
            
            print('BussTotal:', BussTotal)
            print('PublicBuss:', PublicBuss)
            print('SchoolBuss:', SchoolBuss)
            
            print('ActiveTotal:', ActiveTotal)
            print('Cycling:', Cycle)
            print('Foot', Foot)

        else: 
            pass

        if "Powel" in name and year == 2005:
            #Car bit is working 

            print('School Name:',name,'Year:', year) 
            
            print('CarTotal:',CarTotal)
            print('car:', car)
            print('carshare:', carshare)
            
            print('BussTotal:', BussTotal)
            print('PublicBuss:', PublicBuss)
            print('SchoolBuss:', SchoolBuss)
            
            print('ActiveTotal:', ActiveTotal)
            print('Cycling:', Cycle)
            print('Foot', Foot)

        else: 
            pass
print('[end note]School Name: St Martins Dorking Year: No stats') 
