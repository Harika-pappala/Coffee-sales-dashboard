import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
st.title("☕Coffee Sales Dashboard")
df=pd.read_csv("coffee_sales_clean.csv")
store=st.selectbox("Select Store Location",df["store_location"].unique())
filtered=df[df["store_location"]==store]
st.subheader("Revenue by Hour")
hourly=filtered.groupby("hour")["revenue"].sum()
fig,ax=plt.subplots()
ax.bar(hourly.index,hourly.values)
ax.set_xlabel("Hour")
ax.set_ylabel("Revenue")
st.pyplot(fig)
st.subheader("Revenue By Product Category")
product=filtered.groupby("product_category")["revenue"].sum()
fig2,ax2=plt.subplots()
ax2.bar(product.index,product.values)
ax2.set_xlabel("Product Category")
ax2.set_ylabel("revenue")
ax2.tick_params(axis='x',rotation=45)
st.pyplot(fig2)
st.subheader("Revenue Distribution")
fig3,ax3=plt.subplots()
ax3.hist(filtered["revenue"],bins=30)
ax3.set_xlim(0,50)
st.pyplot(fig3)
st.subheader("Store vs Hour heatmap")
pivot=df.pivot_table(values="revenue",
                     index="store_location",
                     columns="hour",
                     aggfunc="sum")
fig4,ax4=plt.subplots(figsize=(20,10))
sns.heatmap(pivot,annot=True,fmt=".0f",cmap="YlGnBu",ax=ax4)
st.pyplot(fig4)
Total_revenue=filtered["revenue"].sum()
Total_transactions=filtered["transaction_id"].count()
col1,col2=st.columns(2)
col1.metric("Total Revenue",Total_revenue)
col2.metric("Total Transactions",Total_transactions)
