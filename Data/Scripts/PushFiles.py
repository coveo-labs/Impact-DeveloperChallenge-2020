#!/usr/bin/env python
# -------------------------------------------------------------------------------------
# Push People using Python Push SDK
# -------------------------------------------------------------------------------------

import csv
import datetime
import os
import json

from coveopush import CoveoPush
from coveopush import Document
from coveopush import CoveoPermissions
from coveopush import CoveoConstants

# create a document
def create_document(fileloc):
    # Create new push document
    print("Adding: "+fileloc)
    mydoc = Document('https://server?id='+fileloc)

    return mydoc

def checkDirectory(push, path):
  for filename in os.listdir(path):
      print (path+"/"+filename)
      if os.path.isfile(path+"/"+filename): 
        push.Add( create_document(path+"/"+filename) )
      else:
        checkDirectory(push, path+"/"+filename)

def main():
    # setup Push client
    sourceId = '--Enter your source id--'
    orgId = '--Enter your org id--'
    apiKey = '--Enter your API key--'


    updateSourceStatus = True
    deleteOlder = False

    # Create the push client
    push = CoveoPush.Push(sourceId, orgId, apiKey)
    push.Start(updateSourceStatus, deleteOlder)

    # Create the documents
    path = '../Files'
    for filename in os.listdir(path):
      print (path+"/"+filename)
      if os.path.isfile(path+"/"+filename): 
        push.Add( create_document(path+"/"+filename) )
      else:
        checkDirectory(push, path+"/"+filename)

    push.End(updateSourceStatus, deleteOlder)


if __name__ == '__main__':
    main()
