
import pandas as pd
import matplotlib.pyplot as plt
pd.read_excel('cat.xlsx', engine='openpyxl')


#importiranje na datasetot
df=pd.read_excel("clients_products_dataset.xlsx")

print(df.head())
print(df.tail())


# #Kreiranje na novi koloni
# df["remaining_debt"]=df["amount"]-df["payed_amount"]
# #PROVERKA
# #3.83%=3.83/100=0.0383
# df["total_debt_with_interest"]=df["remaining_debt"]*(1+df["interest_rate"]/100)


# print(df.head())
# print(df.tail())


# #Iznos vo default
# default_debt=df.groupby("default")["remaining_debt"].sum()
# print(default_debt)


# #Prosecna kamata po produkt
# product_mean_interes=df.groupby("product_type")["interest_rate"].mean()
# print(product_mean_interes)


# #Tabela na korelacija
# corr=df[["amount","payed_amount","interest_rate"]].corr()
# print(corr)


# #Suma na ostanatiot dolg po produkt
# product_max_loan=df.groupby("product_type")["remaining_debt"].sum()
# print(product_max_loan)


# plt.subplot(2,3,1)
# plt.bar(product_mean_interes.index, product_mean_interes.values)
# plt.title("Prosecna kamatna stapka za produkt")


# plt.subplot(2,3,2)
# plt.hist(df["interest_rate"])
# plt.title("Prosecna kamatna stapka za produkt")


# plt.subplot(2,3,3)
# plt.bar(default_debt.index, default_debt.values)
# plt.title("Remaining debt, default 0 i 1")


# plt.subplot(2,3,4)
# plt.scatter(df["amount"],df["interest_rate"])
# plt.title("Amount vs Interest rate")


# plt.subplot(2,3,5)
# plt.imshow(corr,cmap="coolwarm")
# plt.colorbar()
# plt.xticks(range(len(corr.columns)), corr.columns)
# plt.yticks(range(len(corr.columns)), corr.columns)
# plt.title("Matrica na korelacija")

# total_debt=df.groupby("product_type")["remaining_debt"].sum()

# plt.subplot(2,3,6)
# plt.bar(total_debt.index, total_debt.values)
# plt.title("Noviot dolg po produkt")


# plt.suptitle("Client Products Analysis Dashboard")


# plt.tight_layout()
# plt.show()

# #PAUZA DO 10:20