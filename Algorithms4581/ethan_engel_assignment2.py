import pandas as pd
import sys
sys.setrecursionlimit(100000)
sec_df=pd.read_csv("securities.csv")


def psa(file):
    psa_df=pd.read_csv(file)
    return psa_df

def company_subarray(df,symbol):
    company_df = df[df["symbol"] == symbol]
    company_df.reset_index(inplace=True)
    company_array=[]
    for sub in range(len(company_df)-1):
        daily_change=company_df["close"][sub+1]-company_df["close"][sub]
        company_array.append(daily_change)
    return company_array


def MSSDAC (A,low, high):
    if low==high-1:
        return low, high, A[low]
    else:
        mid=(low+high)//2
        leftlow, lefthigh, maxLeft=MSSDAC(A,low,mid)
        rightlow, righthigh, maxRight=MSSDAC(A,mid,high)

    maxLeft2Center=left2Center=0
    leftsum=float('-inf')
    crosslow=mid
    for i in range(mid-1,low-1,-1):
        left2Center += A[i]
        if left2Center>leftsum:
            leftsum=left2Center
            crosslow=i

    maxRight2Center=right2Center=0
    crosshigh=mid+1
    rightsum=float('-inf')
    for i in range(mid,high):
        right2Center += A[i]
        if right2Center>rightsum:
            rightsum=right2Center
            crosshigh=i+1

    if (maxLeft>maxRight and maxLeft>(rightsum+leftsum)):
        return leftlow, lefthigh, maxLeft
    elif (maxRight>maxLeft and maxRight>(rightsum+leftsum)):
        return rightlow, righthigh, maxRight
    else:
        return crosslow, crosshigh,(rightsum+leftsum)


max_stock_tuple=(0,0,0)
max_ticker=""
for ind in sec_df.index:
    stock_data_list=company_subarray(psa("prices-split-adjusted.csv"),sec_df["Ticker symbol"][ind])
    if stock_data_list!=[]:
        stock_tuple=MSSDAC(stock_data_list,0,len(stock_data_list))
        if stock_tuple[2]>max_stock_tuple[2]:
            max_stock_tuple=stock_tuple
            max_ticker=sec_df["Ticker symbol"][ind]
        print(ind,max_ticker,max_stock_tuple)


dates_df=psa("prices-split-adjusted.csv")
max_dates_df = dates_df[dates_df["symbol"] == max_ticker]
max_dates_df.reset_index(inplace=True)
max_symbol=max_dates_df["symbol"][0]
magic_index=sec_df[sec_df['Ticker symbol'] == max_symbol].index.tolist()
max_company=sec_df["Security"][magic_index[0]]
buy_date=max_dates_df["date"][max_stock_tuple[0]]
sell_date=max_dates_df["date"][max_stock_tuple[1]]
print("Best stock to buy:",max_company,"on",buy_date,"and sell on", sell_date, "with profit of", max_stock_tuple[2])
