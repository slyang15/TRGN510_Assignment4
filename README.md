# TRGN510_Assignment4
This program takes a gtf file and column number as an input, and converts a csv file's Ensembl name to its HUGO name.

## Installation
### GTF file download
* The data Homo_sapiens.GRCh37.75.gtf.gz was downloaded from http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens.
* download the file using wget: wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz
* unzip the file using gunzip: gunzip Homo_sapiens.GRCh37.75.gtf.gz
* download a unit test for the csv file using git clone: git clone https://github.com/davcraig75/unit

## Usage
### Convert ENSG to HUGO name
* The gtf file has a dictionary created, that uses Ensembl gene names as a key, and the HUGO name as a value. This dictionary is to be applied to the argument, a csv file.
* When running the script with a unit test (https://github.com/davcraig75/unit), its Ensemble gene name is converted to its HUGO name. 
* Options range from “-f [0-9]” where -f2 would pick the 2nd column. If there is no “-f” then the first column is used.
* If there are no dictionary values that match, the column will be changed to "NA".

## Dependencies
* wget
* git, git clone
* sys
* fileinput
* csv
* re

## Complications
* The program has not been tested with files other than the Homo_sapiens.GRCh37.75.gtf.gz file. 
* Ensembl gene names that are not included in the dictionary will have "NA" in place of the Ensembl name. 
* The program has only been tested with the unit file; therefore, there may be complications applying the -f option. 

## Contact
* Lynn Yang at seolynya@usc.edu
