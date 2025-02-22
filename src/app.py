from utils import db_connect
engine = db_connect()

# your code here

df = pd.read_csv ('https://raw.githubusercontent.com/4GeeksAcademy/logistic-regression-project-tutorial/main/bank-marketing-campaign-data.csv')
print (df.head())

