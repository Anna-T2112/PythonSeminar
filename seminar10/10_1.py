import pandas as pd

def show_dummies(lst):
    data = pd.DataFrame({'whoAmI':lst})
    data.head()
    dummies = pd.get_dummies(data['whoAmI'])
    print(dummies)

def show_dummies_with_grouping(lst,lst2,grouping):
    data = pd.DataFrame({'whoAmI':lst,'myName':lst2})
    data.head()
    df = data[['whoAmI']].join(pd.get_dummies(data['myName'])).groupby(grouping).max()
    print(df)


lst = ['robot'] * 10
lst += ['human'] * 10
lst2 = ['RS232'] * 10
lst2+=['Иван']*10

show_dummies(lst)
show_dummies_with_grouping(lst,lst2,'whoAmI')
