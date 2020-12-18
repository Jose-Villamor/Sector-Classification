import streamlit as st
import pickle
import pandas as pd
from PIL import Image

from  preprocess import preprocess_std
from graph import func_pct,  donut_graph

model = pickle.load(open('Financial_Classification','rb'))

st.set_page_config(
    page_title="Finacial Sector Classification App",
    layout="centered",
    initial_sidebar_state="expanded")

def predict_sector(data):
    prediction = model.predict_proba(data)
    return prediction.ravel()

st.sidebar.header('Select financial indicators values') 
def side_bar():
    NetIn = st.sidebar.slider("Net Income (Millions)", value=10.0, step=1.0, min_value=-500.0, max_value=1000.0)
    NetInG = st.sidebar.slider("Net income growth", value=1.0, step=1.0, min_value=-91.54, max_value=100.0)
    FCF = st.sidebar.slider("Free Clash Flow (Millions)", value=100.0, step=10.0, min_value=-500.0, max_value=1500.0)
    EPS = st.sidebar.slider("Earnings per share", value=1.16, step=1.0, min_value=-50.3, max_value=50.55)
    PRICEVAR = st.sidebar.slider("2019 price variation (%)", value=20.39, step=1.0, min_value=-98.75, max_value=150.70)
    MarketC = st.sidebar.slider("Market Capitalization (Millions)", value=500.0, step=1.0, min_value=1.0, max_value=2000.10)
    PayRat = st.sidebar.slider("Payout Ratio", value=0.28, step=0.1, min_value=-10.0, max_value=10.0)
    ROE = st.sidebar.slider("ROE", value=0.00, step=0.1, min_value=-5.0, max_value=5.0)
    debtRat = st.sidebar.slider("Debt Ratio", value=0.31, step=0.1, min_value=0.01, max_value=2.0)
    currentRat = st.sidebar.slider("Current Ratio", value=2.28, step=0.1, min_value=0.01, max_value=10.35)
    
    features = {"NetIn":NetIn,
                "NetInG":NetInG,  
                "FCF": FCF,
                "EPS":EPS, 
                "PRICEVAR":PRICEVAR, 
                "MarketC":MarketC, 
                "PayoutRatio":PayRat,  
                "ROE":ROE, 
                "debtRatio":debtRat, 
                "currentRatio":currentRat}
        
    
    data = pd.DataFrame(features,index=["Values"])
    return data
    
def main():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    st.subheader("Jose Villamor")

    image = Image.open('sectors.png')
    st.image(image, use_column_width=True)

    st.write("This website app predicts a sector depending on the financial indicators selected in the side panel. The outcome is represented by a donut chart.") 
    st.write("**If you want to know more about the project or others that i have done visit my github account: https://github.com/Jose-Villamor/Kaggle-Notebooks**")
    
    data = side_bar()   
 
    st.subheader("Selected features")
    st.table(data)
    
    prepro = preprocess_std(data)

    predict = predict_sector(prepro)
    donut_graph(predict)

    st.write(""" 
    **Other category include Real state, Enery,Communication Services and Utilities sectors**
    """)

    st.subheader("Model description")
    st.write("To make the model I use SVM with a large C so predicted probability was more distributed among classes. We obtained a low accuracy score but the objective of this project is to make a dinamic visualization where all categories are somewhat fill not only one.The dataset use was obtained from Kaggle: 200+ Financial Indicators of US stocks (2014-2018).")


if __name__=='__main__':
    main()
