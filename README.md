# MPP-Database-Builder
Builds an MPP database to enable non-targeted analyses of emerging toxic substances of concern using high-performance liquid chromatography-quadrupole-time-of-flight mass spectrometry (HPLC-Q-ToF MS) data.

The MPP database used by Agilent has the ability to search for chemicals in samples based on chemical properties and retention times provided by the user. The original database provided had incomplete entries for chemicals, and the side-project herein was intended to reconcile the original database to public databases such as PubChem and ChemSpider. This version of the tool uses the CAS numbers to build a database for chemicals to watch for in suspect screening.

# Instructions
1. Run the MPP-Database-Builder.py file.
2. Enter in the file location on your local disk drive with the filename included, e.g. C:\Desktop\MyCASList.csv
3. Allow the builder to complete and an appropriate .xlsx file should generate, e.g. MyCASList - PubChem Search Results.xlsx, in the same directory as the input CAS list.
