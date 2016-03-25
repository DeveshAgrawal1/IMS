# Data Retriever
# The module can be used to retrieve data from different sources,
# to eventually prepare database for training the neural network

# Presently the DSD : Daily solar data is being downloaded,
# other data could be downloaded using the retriever method

#python 2.7.11
#tested and working
#in case one needs to export to MySql database, use  SQLAlchemy along with pandas SQL

import urllib2
from time import sleep
from sys import argv
import pandas as pd

class DataRetriever:
    def __init__(self):
        # Download data to a user specified local directory
        # Provide destination in such formats:
        #   ubuntu : /home/simar/Repos/eras
        #   windows: C:/Repos/eras
        self.dest = argv[1]
        
    def retriever(self, url, dest):
        df = pd.read_csv(url,header=None,skiprows=12,delimiter=" ",skipinitialspace=True)
        df.to_csv(dest, header=False)

    def dsd_retriever(self):
        for n in range(2001, 2013):
            url = "ftp://ftp.swpc.noaa.gov/pub/warehouse/{0}/{0}_DSD.txt"
            url = url.format(n)

            # Constructing output as example : destination/dsd_2011.csv
            dest = r"{0}/dsd_{1}.csv".format(self.dest, n)
            print "\nDownloading DSD {0} data :".format(n)
            
            self.retriever(url, dest)
            # Providing sleep time to prevent forced session termination
            sleep(3)


if __name__ == '__main__':
    retrieve = DataRetriever()
    retrieve.dsd_retriever()
