# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:19:04 2022

@author: EqualRanc
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:00:04 2019

@author: EqualRanc
"""

import pandas as pd
import pubchempy as pcp
import cirpy as cir
import concurrent.futures
from time import process_time

def pubsearch(casnum):
    if len(casnum) < 2:
        p = pd.DataFrame([['invalid cas number','invalid cas number','invalid cas number','invalid cas number','invalid cas number']], columns=['InChIKey','IUPACName','MolecularFormula','MonoisotopicMass','CanonicalSMILES'])
        return p
    else:
        try:
            ikey = cir.resolve(casnum, 'stdinchikey')
            ikey = '%s' % ikey[9:]    
            p = pcp.get_properties(['InChIKey','IUPACName','MolecularFormula','MonoisotopicMass','CanonicalSMILES'], ikey, namespace='inchikey', as_dataframe=True)
            return p
        except:
            p = pd.DataFrame([['notfound','notfound', 'notfound', 'notfound', 'notfound']], columns=['InChIKey','IUPACName','MolecularFormula','MonoisotopicMass','CanonicalSMILES'])
            return p

def casimport(url):
    url = "https://github.com/EqualRanc/MPP-Database-Builder/raw/main/CAS%20-%20Example%20Input%20File.csv"
    outfile = '%s - PubChem Search Results.xlsx' % url[:-4]
    chem_df = pd.read_csv(url)
    chem_df_num = chem_df.to_numpy()
    cas = []
    data = pd.DataFrame(data=None, columns=['InChIKey','IUPACName','MolecularFormula','MonoisotopicMass','CanonicalSMILES'])
    for casno in chem_df_num[:,0]:
        cas.append(str(casno))
    return cas, outfile, data

def cassearch(caslist,dat):
    #Parallel processing of CAS No. list for InChIKey, IUPAC Name, 
    #Molecular Formula, Monoisotopic Mass, and Canonical SMILES for processing MS data in MPP workflow (Agilent)
    t1 = process_time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:    
        for item, casitem in zip(caslist, executor.map(pubsearch, caslist)):
            dat = pd.concat([dat, casitem])
    t2 = process_time()
    print('PubChem Search Completed in minutes:', (t2-t1)/60)
    dat.index.names = ['CID']
    return dat

def excelout(data):
    data.to_excel(outfile, index_label=True)
    print('Export to outfile %s completed' % outfile)
    
url = input('Enter URL to CAS No. CSV File: ')
cas, outfile, data = casimport(url)
data = cassearch(cas)    
excelout(data)
