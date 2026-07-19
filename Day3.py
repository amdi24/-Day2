def TalaBirr_transaction():
    transactions = {}
    try:
     # reading the transactions from the file and storing them in a dictionary
     with open("transactions.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, amount = line.split(",")
            amount = float(amount)

        # Building a dictionary to store the total amount for each name
            transactions[name] = transactions.get(name, 0) + amount
    except FileNotFoundError:
        print("The file transactions.txt was not found.")
        return
    
    #storing the stored transactions in a sorted manner based on the total amount in desceding order
    sorted_transactions = sorted(transactions.items(), key=lambda x: x[1], reverse=True)        
    for name, total in sorted_transactions:
        print(f"{name}: {total}")

    with open("report.txt","w") as report:
        for name, total in sorted_transactions:
          report.write(f"{name}: {total}\n")

print("Report generated successfully in report.txt.")
 # hear i call the function to execute the transaction processing and report generation
TalaBirr_transaction()
   
    
   