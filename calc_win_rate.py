import pandas as pd

df = pd.read_csv('daily_result.csv')
print(df)
dates,games,wins = df['date'].values,df['game'].values,df['win'].values

out_df = pd.DataFrame()
len_out_df = len(dates) - 1
out_df_date,out_df_game,out_df_win_rate = [None]*len_out_df,[None]*len_out_df,[None]*len_out_df

for i in range(len_out_df):
    out_df_date[i] = f'{dates[i]}-{dates[i+1]}'
    n_game = games[i+1] - games[i]
    out_df_game[i] = n_game
    out_df_win_rate[i] = (wins[i+1] - wins[i]) / n_game
out_df['date'],out_df['game'],out_df['win_rate'] = out_df_date,out_df_game,out_df_win_rate
print(out_df)
    
