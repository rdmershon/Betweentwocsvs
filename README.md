This just compares two CSV files. The intent is to take the first file, load all column values in the "Email" column into memory.

It then compares the values in the first csv, against the values of the columns in the second csv.

It appends the values to a copy of the first csv if the fields are present in the second csv or not (true for present, false for not).

The Dataset is from https://www.datablist.com/learn/csv/download-sample-csv-files

This script was 99% written by Gemini, and was barely modified (I told it to use the CSV library vs Pandas).

