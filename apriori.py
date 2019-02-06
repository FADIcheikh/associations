# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

df = pd.read_table("D:\Data_Minig\sseance5_associative_apriori\market_basket\market_basket.txt",sep ='\t',header = 0)
#print df.head(5)
#print len(df)
#print df.shape[1]

#The Apriori library requires our dataset to be in the form of a list of lists

records = []
for i in range(0, len(df)):
    records.append([str(df.values[i,j]) for j in range(0, df.shape[1])])


print len(records[0])

# Transform 0,1=> variables
for i in range(0, len(df)):
    for j in range(0,(len(records[0]))):

        if records[i][j]== str(1):
            records[i][j] = str(df.columns[j])
        else:
            records[i][j] =float('nan')

print records[:5]

#Support(B) = (Transactions containing (B))/(Total Transactions)
#Confidence(A→B) = (Transactions containing both (A and B))/(Transactions containing A)
#Lift(A→B) = (Confidence (A→B))/(Support (B))
association_rules = apriori(records, min_support=0.05, min_confidence=0.3, min_lift=4, min_length=2)
association_results = list(association_rules)
#Number of association rules
print len(association_results)
print(association_results[0])
## clean display
for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")