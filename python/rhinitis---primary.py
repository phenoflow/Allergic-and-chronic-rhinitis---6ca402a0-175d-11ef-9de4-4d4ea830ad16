# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"H120.00","system":"readv2"},{"code":"H17..00","system":"readv2"},{"code":"47599.0","system":"readv2"},{"code":"1930.0","system":"readv2"},{"code":"121.0","system":"readv2"},{"code":"175.0","system":"readv2"},{"code":"24163.0","system":"readv2"},{"code":"15553.0","system":"readv2"},{"code":"964.0","system":"readv2"},{"code":"95938.0","system":"readv2"},{"code":"16134.0","system":"readv2"},{"code":"5627.0","system":"readv2"},{"code":"1108.0","system":"readv2"},{"code":"42065.0","system":"readv2"},{"code":"1838.0","system":"readv2"},{"code":"18572.0","system":"readv2"},{"code":"42556.0","system":"readv2"},{"code":"774.0","system":"readv2"},{"code":"13377.0","system":"readv2"},{"code":"10546.0","system":"readv2"},{"code":"4861.0","system":"readv2"},{"code":"28589.0","system":"readv2"},{"code":"1468.0","system":"readv2"},{"code":"775.0","system":"readv2"},{"code":"16158.0","system":"readv2"},{"code":"15248.0","system":"readv2"},{"code":"3798.0","system":"readv2"},{"code":"30375.0","system":"readv2"},{"code":"2372.0","system":"readv2"},{"code":"16441.0","system":"readv2"},{"code":"14645.0","system":"readv2"},{"code":"3162.0","system":"readv2"},{"code":"72490.0","system":"readv2"},{"code":"805.0","system":"readv2"},{"code":"104543.0","system":"readv2"},{"code":"12382.0","system":"readv2"},{"code":"J31.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('allergic-and-chronic-rhinitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["rhinitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["rhinitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["rhinitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
