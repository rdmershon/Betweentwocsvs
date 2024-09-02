import csv

def compare_csv_emails_with_csv_lib(file1, file2, email_column):
    """
    Compares two CSV files based on email columns using the csv library and outputs a new CSV with comparison results.

    Args:
        file1: Path to the first CSV file.
        file2: Path to the second CSV file.
        email_column: The name of the email column in both CSV files.

    Returns:
        None (Outputs the results to a new CSV file)
    """

    # Read the second CSV file and extract emails
    with open(file2, 'r') as f2:
        reader2 = csv.DictReader(f2)
        emails2 = set(row[email_column] for row in reader2)

    # Read the first CSV file, compare, and write output
    with open(file1, 'r') as f1, open('comparison_results.csv', 'w', newline='') as outfile:
        reader1 = csv.DictReader(f1)
        fieldnames = reader1.fieldnames + ['Exists in Second File']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader1:
            row['Exists in Second File'] = row[email_column] in emails2
            writer.writerow(row)

    print("Comparison results saved to comparison_results.csv")

# Example usage
file1 = 'customers100.csv'
file2 = 'customers25.csv'
email_column = 'Email'

compare_csv_emails_with_csv_lib(file1, file2, email_column)