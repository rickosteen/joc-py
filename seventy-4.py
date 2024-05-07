import pandas as pd

def analyze_sudden_increases(file_path):
    # Load the dataset
    data = pd.read_csv(file_path, sep=';', names=['DateTime', 'Last Price', 'Bid Price', 'Ask Price', 'Volume'])
    
    # Convert 'DateTime' to datetime format
    data['DateTime'] = pd.to_datetime(data['DateTime'], format='%Y%m%d %H%M%S %f', errors='coerce')
    
    # Calculate the point change in 'Last Price' between consecutive ticks
    data['Point Change'] = data['Last Price'].diff()
    
    # Filter for sudden increases defined as changes of 10 points or more
    data.loc[:, 'Hour'] = data['DateTime'].dt.hour
    sudden_increases = data[data['Point Change'] >= 2]
    
    if sudden_increases.empty:
        print("No sudden increases of 10 points or more were found.")
        return
    
    # Analyze the distribution of sudden increases by hour
    hour_distribution = sudden_increases['Hour'].value_counts(normalize=True).sort_index().cumsum()
    
    # Determine the hours during which 70% of sudden increases occur
    target_hours = hour_distribution[hour_distribution <= 0.7]
    return target_hours

if __name__ == "__main__":
    file_path = r'C:\Users\rick\downloads\RTY03-24Last.txt'  # Use raw string for Windows paths
    result = analyze_sudden_increases(file_path)
    if result is not None:
        print("Hours during which 70% of sudden increases occur:")
        print(result)
    else:
        print("Adjust your criteria or check your dataset.")
