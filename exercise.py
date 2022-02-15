import sys
import csv

class Csv_Handler(object):
    
    def __init__(self, customer_sample):
        # keep customer codes in a set
        customers = set()

        with open(customer_sample, newline='') as f:
            csv_file = csv.reader(f)

            # first line contains heading
            csv_heading = next(csv_file)

            # iterate lines of the CSV file
            for line in csv_file:
                customers.add(line[0])
                print(line)

        self.create_files(customers)


        
    def create_files(self, customers):

        with open('CUSTOMER.CSV', newline='') as f:
            csv_file = csv.reader(f)
            csv_heading = next(csv_file)

            with open('CUSTOMER_SMALL.CSV', 'w') as customer_sample: 
                # write to CUSTOMER_SMALL.CSV
                sample_file = csv.writer(customer_sample) 
                sample_file.writerow(csv_heading)

                for line in csv_file:
                    if(line[0] in customers):
                        sample_file.writerow(line)


        # to keep invoice codes
        invoices = set()
        with open('INVOICE.CSV', newline='') as f:
            csv_file = csv.reader(f)
            csv_heading = next(csv_file)

            with open('INVOICE_SMALL.CSV', 'w') as inv_sample: 
                sample_file = csv.writer(inv_sample) 
                sample_file.writerow(csv_heading)

                for line in csv_file:
                    if(line[0] in customers):
                        sample_file.writerow(line) 
                        
                        # keep sample customer invoices
                        invoices.add(line[1])


        # print(invoices)
        with open('INVOICE_ITEM.CSV', newline='') as f:
            csv_file = csv.reader(f)
            csv_heading = next(csv_file)

            with open('INVOICE_ITEM_SMALL.CSV', 'w') as inv_item_sample: 
                sample_file = csv.writer(inv_item_sample) 
                sample_file.writerow(csv_heading)

                for line in csv_file:
                    if(line[0] in invoices):
                        sample_file.writerow(line) 




if __name__ == "__main__":
    # check if user gave argument file
    if(len(sys.argv) > 1):
        customer_sample = sys.argv[1]
        
        handler = Csv_Handler(customer_sample)
        print("Success")
        
    else:
        print("Please give input file!")