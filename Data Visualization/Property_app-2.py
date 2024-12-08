#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel('/Users/anjaliraj/Documents/Capstone/Final Data/Combined_Data.xlsx')

# Streamlit app
st.title('Property Finder')

# User option to select whether buying or renting
option = st.selectbox('Are you buying a property or looking to rent?', ('Buying', 'Renting'))

if option == 'Buying':
    # User inputs for buying
    walk_score_range = st.slider('Select Walk Score Range', min_value=0, max_value=100, value=(0, 100))
    company_adj = st.selectbox('Select Company', df['Company_Adj'].unique())
    min_price = st.number_input('Enter Minimum Selling Price', min_value=0, value=0)
    max_price = st.number_input('Enter Maximum Selling Price', min_value=0, value=10000000)

    # Filter the dataframe based on user inputs for buying
    filtered_df = df[(df['Walk_Score'] >= walk_score_range[0]) & 
                     (df['Walk_Score'] <= walk_score_range[1]) & 
                     (df['Company_Adj'] == company_adj) & 
                     (df['Selling_Price'] >= min_price) & 
                     (df['Selling_Price'] <= max_price)]

    # Display the filtered zipcodes for buying
    st.write('Matching Zipcodes:')
    matching_zipcodes = filtered_df['Zipcode'].unique()
    st.write(matching_zipcodes)

    # Generate a histplot showing the range of selling prices for these zipcodes if there are more than one matching zipcodes
    if len(matching_zipcodes) > 1:
        fig, ax = plt.subplots()
        sns.histplot(data=filtered_df, x='Selling_Price', hue='Zipcode', multiple='stack', ax=ax)
        plt.title('Range of Selling Prices by Zipcode')
        plt.xlabel('Selling Price')
        plt.ylabel('Frequency')
        st.pyplot(fig)

elif option == 'Renting':
    # User inputs for renting
    walk_score_range = st.slider('Select Walk Score Range', min_value=0, max_value=100, value=(0, 100))
    company_adj = st.selectbox('Select Company', df['Company_Adj'].unique())
    min_rent = st.number_input('Enter Minimum Rental Value', min_value=0, value=0)
    max_rent = st.number_input('Enter Maximum Rental Value', min_value=0, value=100000)

    # Filter the dataframe based on user inputs for renting
    filtered_df = df[(df['Walk_Score'] >= walk_score_range[0]) & 
                     (df['Walk_Score'] <= walk_score_range[1]) & 
                     (df['Company_Adj'] == company_adj) & 
                     (df['Estimated_Rental_Value'] >= min_rent) & 
                     (df['Estimated_Rental_Value'] <= max_rent)]

    # Display the filtered zipcodes for renting
    st.write('Matching Zipcodes:')
    matching_zipcodes = filtered_df['Zipcode'].unique()
    st.write(matching_zipcodes)

    # Generate a histplot showing the range of rental values for these zipcodes if there are more than one matching zipcodes
    if len(matching_zipcodes) > 1:
        fig, ax = plt.subplots()
        sns.histplot(data=filtered_df, x='Estimated_Rental_Value', hue='Zipcode', multiple='stack', ax=ax)
        plt.title('Range of Rental Values by Zipcode')
        plt.xlabel('Rental Value')
        plt.ylabel('Frequency')
        st.pyplot(fig)

if __name__ == "__main__":
    main()
# In[ ]:




