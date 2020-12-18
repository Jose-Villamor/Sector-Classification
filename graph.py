import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def func_pct(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%".format(pct, absolute)

def donut_graph(data):
    #variables
    labels=['Consumer','Financial Services','Healthcare','Industrials','Other', 'Technology']
    explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05) 
    
    #Plot
    fig, ax = plt.subplots()
    fig.set_size_inches(6,6)
    ax.pie(data, labels=labels, explode=explode,shadow=False, startangle=90,
           autopct=lambda pct: func_pct(pct, data), pctdistance=1.2, labeldistance=1.4, textprops={'fontsize': 14})
    
    plt.title("Types of Sectors", fontsize=20, pad=50)
  

    # add a circle at the center
    my_circle=plt.Circle((0,0), 0.7, color='white')
    p=plt.gcf()
    p.gca().add_artist(my_circle)
 
    st.pyplot()
    return