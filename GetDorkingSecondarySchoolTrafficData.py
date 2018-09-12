'''     numpy is generating warning. ignoring  them!
'''

import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88")

import pandas as pd 
from pandas import ExcelWriter
from pandas import ExcelFile

xl = pd.read_excel('Secondary-Table_del_first3_rows_excel.xlsx' )

# get you column headings.
#print('Colum headings:')
#print(xl.columns)

print('Summary of 2004 Secondary school travel data')

for i in xl.index: 
        namestr = xl['School'][i]
        name = str(namestr)
        year =  xl['Year'][i]
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

        # Print summary

        if "Ashcombe" in name and year == 2004:
            #Car bit is working 

            print('School Name:',name,'Year:', year) 
            
            #print('CarTotal:',CarTotal) note out for speed. 
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

        if "The Priory" in name and year == 2004:
            #Car bit is working 

            print('School Name:',name,'Year:', year ) 
            #print('CarTotal:',CarTotal) noted out for speed
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

print('[end note]: between 2002 and 2004 there is a massive jump in bus ridership at The Priory from 46>395.')
