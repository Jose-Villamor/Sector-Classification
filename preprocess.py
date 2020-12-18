def preprocess_std(data):
    data.NetIn = (data.NetIn - 443.975638) /1602.694815
    data.NetInG = (data.NetInG - 1.101639) / 15.199172
    data.FCF = (data.FCF - 498.250510) / 1947.045048
    data.EPS = (data.EPS - 1.161511) / 6.557545
    data.PRICEVAR = (data.PRICEVAR - 20.394844) / 51.362008
    data.MarketC =(data.MarketC - 8074.544643) / 25644.724295	
    data.PayoutRatio = (data.PayoutRatio - 0.282934)/ 2.292481
    data.ROE = (data.ROE  - -0.029917) / 2.082617
    data.debtRatio =(data.debtRatio - 0.314700) / 0.245188
    data.currentRatio = (data.currentRatio - 2.285548) / 3.987827
   
    return data

