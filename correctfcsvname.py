import os

filepath = 'F://F save'
alldirs = os.listdir(filepath)
for dir in alldirs:
    ffilepath = filepath+'//'+dir+'//F.fcsv'
    if os.path.exists(ffilepath):
        os.rename(ffilepath,filepath+'//'+dir+'//'+dir+'.csv')