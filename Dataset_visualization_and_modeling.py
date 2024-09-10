import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from scipy.stats import zscore
import os


def menu():
    print("This program started.")
    print("Please input \'graph\' to create a scatterplot.")
    print("Please input \'linear_regression\' to execute linear regression modeling.")
    print("Please input \'outliers_espn\' to show \"X\" player based on espn modeling.")
    print("Please input \'outliers_ai\' to show \"X\" player based on artificial intelligence modeling.\n")

def scatterplot(dataset):
    # Extract the relevant columns
    per = dataset['PER']
    w_rate = dataset['W_rate']

    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(per, w_rate, color='blue', alpha=0.5)
    plt.title('Scatter Plot of PER vs W_rate for NBA Players')
    plt.xlabel('Player Efficiency Rating (PER)')
    plt.ylabel('Win Rate (W_rate)')
    plt.grid(True)
    plt.show()

def linear_regression(dataset):
    # Select the relevant columns 'PER' and 'W_rate' for linear regression analysis
    selected_data = dataset[['PER', 'W_rate']]

    # Check for any missing values in the selected data
    selected_data.isnull().sum()

    # Remove rows with missing values in 'W_rate'
    cleaned_data = selected_data.dropna()

    # Prepare the data for modeling
    X = cleaned_data['PER'].values.reshape(-1, 1)  # Predictor (independent variable)
    y = cleaned_data['W_rate'].values  # Response (dependent variable)

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(X, y)
    X_with_constant = sm.add_constant(X)
    model_sm = sm.OLS(y, X_with_constant).fit()
    print(model_sm.summary())

def outlier_espn(dataset):
    # Extract the relevant columns: PER and W_rate
    per_w_rate_data = dataset[['PER', 'W_rate']].copy()

    # Remove rows with NaN values in PER or W_rate columns
    per_w_rate_data_cleaned = per_w_rate_data.dropna(subset=['PER', 'W_rate'])

    # Calculate the Z-scores to identify outliers
    per_w_rate_data['PER_zscore'] = zscore(per_w_rate_data_cleaned['PER'])
    per_w_rate_data['W_rate_zscore'] = zscore(per_w_rate_data_cleaned['W_rate'])

    # Identify outliers with a Z-score threshold of 3
    outliers = per_w_rate_data[(per_w_rate_data['PER_zscore'].abs() > 3) | (per_w_rate_data['W_rate_zscore'].abs() > 3)]

    # Merge the outliers data with the original dataset to provide detailed information
    outliers_with_details = dataset.loc[outliers.index]

    # Display the outliers
    outliers_list = outliers_with_details[['Player', 'PER', 'W_rate']]
    print(outliers_list)

def outlier_ai():
    current_directory = os.getcwd()
    nba_player_data_path = current_directory + '/nba-player-data.xlsx'
    final_data_path = current_directory + '/final_data.csv'

    nba_player_data = pd.read_excel(nba_player_data_path)
    final_data = pd.read_csv(final_data_path)

    # Merge the datasets on player name and team name
    merged_data = pd.merge(
        nba_player_data,
        final_data,
        left_on="Player",
        right_on="PLAYER_NAME",
        suffixes=("_nba", "_final")
    )

    # Define a threshold to identify top players in each category (top 20%)
    points_threshold = merged_data['PTS_nba'].quantile(0.2)
    assists_threshold = merged_data['AST_nba'].quantile(0.2)
    fg_pct_threshold = merged_data['FG%'].quantile(0.2)
    three_pt_pct_threshold = merged_data['3P%'].quantile(0.2)
    dreb_threshold = merged_data['DREB_RANK'].quantile(0.2)
    stl_threshold = merged_data['STL_RANK'].quantile(0.2)
    blk_threshold = merged_data['BLK_RANK'].quantile(0.2)
    efficiency_threshold = merged_data['Efficiency'].quantile(0.2)
    plus_minus_threshold = merged_data['PLUS_MINUS'].quantile(0.2)
    win_rate_threshold = merged_data['W_rate'].quantile(0.2)

    # Filter players based on these thresholds (offensive, defensive, and efficiency stats)
    significant_players = merged_data[
        (merged_data['PTS_nba'] >= points_threshold) &
        (merged_data['AST_nba'] >= assists_threshold) &
        (merged_data['FG%'] >= fg_pct_threshold) &
        (merged_data['3P%'] >= three_pt_pct_threshold) &
        (merged_data['DREB_RANK'] <= dreb_threshold) &
        (merged_data['STL_RANK'] <= stl_threshold) &
        (merged_data['BLK_RANK'] <= blk_threshold) &
        (merged_data['Efficiency'] >= efficiency_threshold) &
        (merged_data['PLUS_MINUS'] >= plus_minus_threshold) &
        (merged_data['W_rate'] >= win_rate_threshold)
        ]

    # Select relevant columns to display
    significant_players_list = significant_players[
        ['Player', 'PTS_nba', 'AST_nba', 'FG%', '3P%', 'DREB_RANK', 'STL_RANK', 'BLK_RANK', 'Efficiency', 'PLUS_MINUS',
         'W_rate']]

    # Display the list of significant players
    print(significant_players_list)


def run():
    # Get the current working directory
    current_directory = os.getcwd()
    file_path = current_directory + '/updated_nba_player_data.xlsx'
    data = pd.read_excel(file_path)
    while True:
        menu()
        user_input = input("Enter your command: ")
        if user_input.lower() == 'graph':
            scatterplot(data)
        elif user_input.lower() == 'linear_regression':
            linear_regression(data)
        elif user_input.lower() == 'outliers_espn':
            outlier_espn(data)
        elif user_input.lower() == 'outliers_ai':
            outlier_ai()
        elif user_input.lower() == 'q':
            print('Program Ends.')
            break
        else:
            print('Incorrect! Please input valid command.')


if __name__ == "__main__":
    run()

