"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Completed 11-14-19 by RC
Passed 100% of automated testing.
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        field_names = csvreader.fieldnames
    return field_names



def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each dictionary
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, 
                                   delimiter=separator, 
                                   quotechar=quote)
        table = []                                    
        for row in csvreader:
            table.append(row)                                                                               
    return table


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, 
                                   delimiter=separator, 
                                   quotechar=quote)
        table = {}                                    
        for row in csvreader:
            table[row[keyfield]] = row                                    
    return table


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file for output.
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields in CSV output file.
      quote      - character used to optionally quote fields in CSV output file.
    Output:
      Writes the table to a CSV file with the name filename, using the
      given sequence of keys, fieldnames, to set order.  All non-numeric fields 
      will be quoted.
    """
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=separator,
                                   quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)
        csvwriter.writeheader()
        csvwriter.writerows(table)


