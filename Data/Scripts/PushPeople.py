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
def create_document(people):
    # Create new push document
    mydoc = Document('https://myreference?id='+str(people['id']))
    # Build up the quickview/preview (HTML)
    content = "<HTML><BODY></BODY></HTML>"
    mydoc.SetContentAndZLibCompress(content)

    return mydoc


def main():
    # setup Push client
    sourceId = '--Enter your source id--'
    orgId = '--Enter your org id--'
    apiKey = '--Enter your API key--'

    updateSourceStatus = True
    deleteOlder = True

    # Create the push client
    push = CoveoPush.Push(sourceId, orgId, apiKey)
    push.Start(updateSourceStatus, deleteOlder)

    # Create the documents
    path = '../Authors'
    for filename in os.listdir(path):
       with open(path+"/"+filename,encoding='utf8') as data_file: 
          people = json.load(data_file)
          push.Add( create_document(people) )

    push.End(updateSourceStatus, deleteOlder)


if __name__ == '__main__':
    main()
