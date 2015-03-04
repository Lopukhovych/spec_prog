import  urllib2
import pandas as pd
import time
from datetime import datetime, timedelta, date, time as dt_time
arr=[0,22,24,23,25,3,4,8,19,20,21,9,26,10,11,12,13,14,15,16,27,17,18,6,1,2,7,5]
d = datetime.today()
def ff():
    i=1


    #the_time = d.timetz()
    #the_time = the_time.replace(second=0, microsecond=0)
    while i<=27:
        if i<10:
            url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R0"+str(i)+".txt"
        else :
            url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"+str(i)+".txt"
        vhi_url = urllib2.urlopen(url)
        out = open('vhi_id_'+ str(arr[i])+'_'+str( d.date())+'.csv','wb')
        out.write(vhi_url.read())
        out.close()
        import pandas as pd

        df = pd.read_csv('vhi_id_'+str(arr[i])+'_'+str( d.date())+'.csv',index_col=False, header=1)
        print list(df.columns.values)
        print df[:1]
        i=i+1
def VHI():
    f=input('Enter the id to the field')
    df = pd.read_csv('vhi_id_'+str(f)+'_'+str("2015-02-20")+'.csv',index_col=False, header=1)#d.date()
    y=input('Enter year')
    w=input('Enter week')
    print('number  VHI')
    print (df[(df['year']==y)& (df['week']==w)]['VHI'])
    print('MAXIMUM')
    print max(df[(df['year']==y)]['VHI'])
    print('MINIMUM')
    print min(df[(df['year']==y)]['VHI'])
def dry(percent):
    f=input('Enter the id to the field')
    df = pd.read_csv('vhi_id_'+str(f)+'_'+str("2015-02-20")+'.csv',index_col=False, header=1) # d.date()
    print (df[(df['VHI']<15)& (df['%Area_VHI_LESS_15']>int(percent))]['year'])
def moderate(percent):
    f=input('Enter the id to the field')
    df = pd.read_csv('vhi_id_'+str(f)+'_'+str( d.date())+'.csv',index_col=False, header=1)
    print (df[(df['VHI']<35)&(df['VHI']>15)& (df['%Area_VHI_LESS_35']>int(percent))]['year'])
##VHI()
#ff()
#dry('10')
#moderate('30')
print "VHI is downloaded..."
