# pylint: disable=C0321,C0103,C0301,E1305,E1121,C0302,C0330,C0111,W0613,W0611,R1705
# -*- coding: utf-8 -*-
import os, sys, time, datetime,inspect


##################################################################################################
def test1():

   from utilmy import (Session,
                       global_verbosity,




                       os_makedirs,
                       os_system ,
                       os_removedirs,





                       pd_read_file,
                       pd_show,



                       git_repo_root,
                       git_current_hash,


                      )




   import pandas as pd, random

   ll = [[ random.random() for i in range(0, 77)] for j in range(0,103) ]
   df =pd.DataFrame(ll, columns = [i for i in range(0,100)])
   os.makedirs("data/parquet/", exist_ok= True)
   df.to_csv( "data/parquet/f01.csv.gz", compression='gzip' )
   df.to_csv( "data/parquet/fa02.csv.gz", compression='gzip' )
   df.to_csv( "data/parquet/fab03.csv.gz", compression='gzip' )
   df.to_csv( "data/parquet/fabc04.csv.gz", compression='gzip' )
   df.to_csv( "data/parquet/fabc05.csv", )


   df1 = pd_read_file("data/parquet/f*.gz", verbose=1, n_pool=3)
   print('pd_read_file gzip ', df1)
   b = df1.mean()
   a = df.mean()
   assert round(a,5) == round(b,5), "Sum of loaded df <> Original df"



   df1 = pd_read_file("data/parquet/fab*.*", verbose=1)
   print('pd_read_file csv ', df)

   df1 = pd_read_file("data/parquet/fab*.*", n_pool=1 )
   print('pd_read_file csv ', df)

   df1 = pd_read_file("data/parquet/f*.gz", verbose=1, n_pool=3)
   print('pd_read_file gzip ', df1)
   b = df1.mean()
   a = df.mean()
   
   print(a.equals(b))
   # for index, val in a.iteritems():
   #  print(f'{index}: {round( val, 5)}')

   # for index, val in b.iteritems():
   #  print(f'{index}: {round( val, 5)}')

   # the 1st
   df1 = pd_read_file("data/parquet/fab*.*", n_pool=0 )

   df1 = pd_read_file("data/parquet/fab*.*", n_pool=1000 )

   df1 = pd_read_file("data/parquet/fac*.*")

   df1 = pd_read_file("data/parquet/")


   # the 2nd
   # pd_show()

   # the 3rd
   print(git_repo_root())


   #############################################################
   os_makedirs('ztmp/ztmp2/myfile.txt')
   os_makedirs('ztmp/ztmp3/ztmp4')
   os_makedirs('/tmp/')
   os_makedirs('/tmp/one/two')
   os_makedirs('/tmp/myfile')
   os_makedirs('/tmp/one/../mydir/')
   os_makedirs('./tmp/test')
    
   os.system("ls ztmp")


   os_removedirs("ztmp/ztmp2")



   print('verbosity', global_verbosity(__file__, "config.json", 40,))
   print('verbosity', global_verbosity('../', "config.json", 40,))
   print('verbosity', global_verbosity(__file__))

   sess = Session("ztmp/session")
   sess.save('mysess', globals(), '01')
   os.system("ls ztmp/session")

   sess.save('mysess', globals(), '02')
   sess.show()

   sess.load('mysess')
   sess.load('mysess', None, '02')


   res = os_system( f" ls . ",  doprint=True)
   print(res)

   res = os_system( f" ls . ",  doprint=False) 
   res = os_system( f" ls . ",  doprint=True) 

   print("success")


if __name__ == "__main__":
    import fire
    fire.Fire(test1)





