import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_excel(
    '/Users/eugene/UCI/Freshman Summer Quarter/AI4C Internship/nba-player-data.xlsx')
win_games_data = pd.read_csv('/Users/eugene/UCI/Freshman Summer Quarter/AI4C Internship/final_data.csv')

# Calculating PER (Player Efficiency Rating) based on the provided formula
# The formula components are mapped to the column names from the dataset
df['FT_Miss'] = (df['FTA'] - df['FT'])
df['FG_Miss'] = (df['FGA'] - df['FG'])

df['PER'] = (
    df['FG'] * 85.910 +
    df['STL'] * 53.897 +
    df['3P'] * 51.757 +
    df['FT'] * 46.845 +
    df['BLK'] * 39.190 +
    df['ORB'] * 39.190 +
    df['AST'] * 34.677 +
    df['DRB'] * 14.707 -
    df['PF'] * 17.174 -
    df['FT_Miss'] * 20.091 -
    df['FG_Miss'] * 39.190 -
    df['TOV'] * 53.897
) * (1 / df['MP'])

# Merge W_rate with the NBA player data
win_games_data = win_games_data[['PLAYER_NAME', 'W_rate']]
win_games_data.rename(columns={'PLAYER_NAME': 'Player'}, inplace=True)

# Merge the W_rate into the nba player data based on Player name
updated_data = pd.merge(df, win_games_data, on='Player', how='left')

# Filter out players with G < 20
filtered_df = updated_data[updated_data['G'] >= 20]

# Save the filtered and updated data to a new Excel file
updated_file_path = '/Users/eugene/UCI/Freshman Summer Quarter/AI4C Internship/updated_nba_player_data.xlsx'
filtered_df.to_excel(updated_file_path, index=False)

