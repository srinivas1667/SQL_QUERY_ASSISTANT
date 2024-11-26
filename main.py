from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text


def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database is for an e-commerce platform and has the following tables:

    1. Products (ProductID, Name, Category, Price, StockQuantity)
    The Products are categorized into Clothing,Electronics,Accesories,Footwear,appliances,Furniture,etc.
    2. Customers (CustomerID, FirstName, LastName, Email, RegistrationDate)
    3. Orders (OrderID, CustomerID, OrderDate, TotalAmount, Status)
    4. OrderDetails (OrderDetailID, OrderID, ProductID, Quantity, Price)

    For example:
    1. Question: How many products are in stock?
       SQL: SELECT SUM(StockQuantity) FROM Products;

    2. Question: What are the top 5 most expensive products?
       SQL: SELECT Name, Price FROM Products ORDER BY Price DESC LIMIT 5;

    3. Question: Who are the customers who placed orders in the last month?
       SQL: SELECT DISTINCT c.FirstName, c.LastName FROM Customers c
            JOIN Orders o ON c.CustomerID = o.CustomerID
            WHERE o.OrderDate >= date('now', '-1 month');

    Provide only the SQL query without any additional explanation. The sql code should not have ``` in the beginning or end and should not include the word 'sql' in the output.
    """
]

st.set_page_config(page_title="E-commerce Database Query Assistant")
st.header("E-commerce Database Query Assistant")

question = st.text_input("Enter your question about the e-commerce database:", key="input")
submit = st.button("Run Query")

if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query:")
    st.code(response, language="sql")

    try:
        query_result = read_sql_query(response, "ecommerce.db")
        st.subheader("Query Result:")
        if query_result:
            st.table(query_result)
        else:
            st.write("No results found.")
    except Exception as e:
        st.error(f"An error occurred while executing the query: {str(e)}")

st.sidebar.header("About")
st.sidebar.info(
    "This app uses Gemini API to convert your questions into SQL queries and run them against an e-commerce database.")
st.sidebar.header("Sample Questions")
st.sidebar.markdown("""
- How many products are in stock?
- What are the top 5 most expensive products?
- Who are the customers who placed orders in the last month?
- What is the total revenue from completed orders?
- Which product category has the highest average price?
""")