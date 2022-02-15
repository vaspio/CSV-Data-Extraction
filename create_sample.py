import csv

def create_csv(test_sample = 1000):

    with open('CUSTOMER.CSV', newline='') as f:
        csv_file = csv.reader(f)

        # first line contains heading
        csv_heading = next(csv_file)

        # open the sample file to write
        with open('CUSTOMER_SAMPLE.CSV', 'w') as sample: 
            sample_file = csv.writer(sample) 
            sample_file.writerow([csv_heading[0]])

            # counts number of customers parsed
            count = 0

            # iterate lines of the CSV file
            for line in csv_file:
                
                # write customers codes to file
                sample_file.writerow([line[0]]) 

                count += 1
                if(count >= test_sample):
                    break


if __name__ == "__main__":
    create_csv()
    
    print("Created sample")