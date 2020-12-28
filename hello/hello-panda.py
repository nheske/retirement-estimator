import pandas as pd

fruits = ['apples', 'bananas', 'grapefruit', 'cherry', 'blueberry', 'orange', 'lemon']
df = pd.DataFrame(fruits)
print(df)

df = pd.DataFrame(fruits, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'], columns=['Names'])
print(df)

names = [['tom', 25], ['krish', 30], ['nick', 26], ['juli', 22]]
df = pd.DataFrame(names, columns=['Name', 'Age'])
print(df)

multi_list_students = [['tom', 'reacher', 25, 'BS'], ['krish', 'pete', 30, 'PhD'],
                       ['nick', 'wilson', 26, 'MBA'], ['juli', 'williams', 22, 'GED']]
df = pd.DataFrame(multi_list_students, columns=['First Name', 'Last Name', 'Age', 'Degree'], dtype=float)
print(df)


# list of name, degree, score
nme = ["Tom", "Steve", "Rachel", "Pirom"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': scr}
df = pd.DataFrame(dict)
print(df)

cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'], 'Price': [22000,25000,27000,35000], 'Year': [2015,2013,2018,2018]}
df = pd.DataFrame(cars, columns= ['Brand', 'Price', 'Year'])
df.to_csv (r'hello\data\cars.csv', index = False, header=True)
print(df)
print()
df = pd.read_csv(r'hello\data\cars.csv')
df.sort_values(by=['Brand'], inplace=True)
print (df)

#JSON file into Pandas DataFrame
# reading the file yields data {'year': 1926, 'stocks': 0.1163, 'bonds': 0.07...  {'year': 1927, 'stocks': 0.3744, 'bonds': 0.07... }
data = pd.read_json(r'hello\data\sample.json')

# displaying the DataFrame
print(data.head(5))