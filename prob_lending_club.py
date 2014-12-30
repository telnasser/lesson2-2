import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats


#loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData = pd.read_csv('https://resources.lendingclub.com/LoanStats3b.csv.zip')

# Clean the data from null values
loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Requested')
plt.savefig("loan-requested-box-plot.png")
plt.show()

loansData.hist(column='Amount.Requested')
plt.savefig("loan-requested-histogram-plot.png")
plt.show()

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("loan-requested-qq-plot.png")
plt.show()

loansData.boxplot(column='Amount.Funded.By.Investors')
plt.savefig("loan-funded-box-plot.png")
plt.show()

loansData.hist(column='Amount.Funded.By.Investors')
plt.savefig("loan-funded-histogram-plot.png")
plt.show()

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig("loan-funded-qq-plot.png")
plt.show()
