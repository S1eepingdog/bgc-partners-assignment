# bgc-partners-assignment-1
### We periodically receive Security and Pricing reference files from our data vendors.  We process these files and import them into our Security Reference System.  The system stores data in a database, but for this assignment we will work with ‘reference’ files only.

#### Inputs:
1.	Example of Corporate Bond / Preferred Equity Vendor reference file: corp_pfd.dif
#### References:
1.	In-use field reference file:  reference_fields.csv
2.	Complete Security Reference file: reference_securities.csv
#### Outputs:
1.	New Security Reference file:  new_securities.csv
2.	Field-Value Reference file:  security_data.csv
 ####Input file is structured as follows:  
-	Column names are stored in a block between lines:   START-OF-FIELDS and END-OF-FIELDS
-	Data is stored between lines:  START-OF-DATA and END-OF-DATA
-	Data is pipe ‘|’  delimited
#### Steps:
1.	Read Security Reference input file and convert it to DataFrame using column names supplied in input file: corp_pfd.diff
2.	Limit columns in DataFrame to only those found in reference_fields.csv
3.	Compare securities in input file with reference_securities.csv file.  Use ID_BB_GLOBAL as the unique key.   Create new_securities.csv, which should include all securities NOT found in reference_securities.csv.   new_securities.csv structure should match reference_securities.csv (Note.  if ID_BB_GLOBAL is NOT unique in input file – use first available row with same ID_BB_GLOBAL)
4.	Create security_data.csv   (comma ‘,’ delimited) with the following structure:

#### How to use
1. Put files to be processed in the root directory
2. Import preprocessor from preprocessor
3. Call process of preprocessor to process files, it will generate two files:

    `new_securities.csv`: security data which not exists in the reference file

    `security_data.csv`: input file which stored in column-based

#### Project Structure

```angular2html
security-data-processor
   ├── README.md
   ├── corp_pfd.dif
   ├── main.py
   ├── new_securities.csv
   ├── preprocessor
   │   ├── __init__.py
   │   ├── constants.py
   │   ├── parser.py
   │   ├── preprocessor.py
   │   └── utils.py
   ├── reference_fields.csv
   ├── reference_securities.csv
   └── security_data.csv
```