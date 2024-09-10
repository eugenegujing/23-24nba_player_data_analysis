# 23-24nba_player_data_analysis


## Description
This study mainly explores the "X" players in the league, who have significant impact on their teams. 
We currently have two datasets for nba players. One is "https://www.kaggle.com/datasets/orkunaktas/nba-players-stats-2324/data",
and the other one is "https://www.kaggle.com/datasets/jackchen019/nba-2023-24-all-players-statsinclude-playoffs".
These two dataset are being downloaded and modified to "nba-player-data.xlsx" and "final_data.csv".
The file Dataset_update helps me to process these two files and integrate them to one clear file with more variables, named "updated_nba_player_data".
The file Dataset_visualization_and_modeling is the main file for this study. It has several functions described below:
1. **`menu()`**:
   - **Purpose**: Provides an interactive menu for the user to select different functionalities offered by the program.
   - **Functionality**:
     - Creating a scatter plot.
     - Running a linear regression model.
     - Identifying outliers using ESPN criteria.
     - Identifying outliers using artificial intelligence models.

2. **`scatterplot()`**:
   - **Purpose**: Generates a visual representation of the relationship between two variables in the dataset.
   - **Functionality**:
     - Plots "Player Efficiency Rating (PER)" on one axis and "Win Rate (W_rate)" on the other.
     - Uses `matplotlib` for plotting.
     - Includes labels, titles, and grid lines for clarity.
     - Helps in visually assessing correlations or patterns between the variables.

3. **`linear_regression()`**:
   - **Purpose**: Performs linear regression analysis to model the relationship between variables.
   - **Functionality**:
     - Uses libraries like `statsmodels` or `scikit-learn` to fit a linear model.
     - Specifies dependent and independent variables from the dataset.
     - Outputs statistical summaries including:
       - Coefficients of the model.
       - R-squared value indicating the model's explanatory power.
       - P-values to assess the significance of variables.

4. **`outliers_espn()`**:
   - **Purpose**: Detects outliers in the dataset based on predefined criteria or thresholds from ESPN.
   - **Functionality**:
     - Calculates statistical measures like mean and standard deviation.
     - Computes z-scores for relevant variables.
     - Flags data points that exceed a certain z-score threshold (e.g., beyond ±3 standard deviations).
     - Outputs a list of identified outliers for further investigation.

5. **`outliers_ai()`**:
   - **Purpose**: Utilizes artificial intelligence or machine learning techniques to identify outliers.
   - **Functionality**:
     - Implements algorithms such as:
       - Clustering methods (e.g., K-means, DBSCAN) to find anomalies.
       - Isolation Forests or One-Class SVM for anomaly detection.
     - Processes the dataset to train the model.
     - Identifies and outputs data points that are considered anomalies by the AI model.

6. **`main()`**:
   - **Purpose**: Serves as the entry point of the program.
   - **Functionality**:
     - Calls the `menu()` function to start the interactive session.
     - Manages the overall flow of the program based on user interactions.
     - Ensures proper execution and termination of the program when the user exits.

This modular design allows for easy maintenance and potential expansion of functionalities in the future.

