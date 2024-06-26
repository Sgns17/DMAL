dataset = [['Milk','Onion','Nutmeg','Kidney Beans', 'Eggs', 'Yogurt'],
          ['Dill','Onion','Nutmeg','Kidney Beans','Eggs','Yogurt'],
          ['Milk','Apple','Kidney Beans','Eggs'],
          ['Milk','Unicorn','Corn','Kidney Beans','Yogurt'],
          ['Corn','Onion','Onion','Kidney Beans','Ice Cream','Eggs']]
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit_transform(dataset)
df =pd.DataFrame(te_ary, columns=te.columns_)
from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
from mlxtend.frequent_patterns import association_rules
res = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
res1 = res[['antecedents','consequents','support','confidence','lift']]
res2 = res1[res1['confidence'] >= 1]
print(res2)

