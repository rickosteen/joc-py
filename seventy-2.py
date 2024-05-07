import pandas as pd

def analyze_sudden_increases(file_path):
    # Load the dataset
    data = pd.read_csv(file_path, sep=';', names=['DateTime', 'Last Price', 'Bid Price', 'Ask Price', 'Volume'])
    
    # Convert 'DateTime' to datetime format
    data['DateTime'] = pd.to_datetime(data['DateTime'], format='%Y%m%d %H%M%S %f', errors='coerce')
    
    # Calculate the point change in 'Last Price' between consecutive ticks
    data['Point Change'] = data['Last Price'].diff()
    
    # Filter for sudden increases defined as changes of 10 points or more
    sudden_increases = data[data['Point Change'] >= 10]
    
    # Extract the hour from each sudden increase instance
    sudden_increases['Hour'] = sudden_increases['DateTime'].dt.hour
    
    # Analyze the distribution of sudden increases by hour
    hour_distribution = sudden_increases['Hour'].value_counts(normalize=True).sort_index().cumsum()
    
    # Determine the hours during which 70% of sudden increases occur
    target_hours = hour_distribution[hour_distribution <= 0.7]
    return target_hours

if __name__ == "__main__":
    file_path = r'C:\Users\rick\downloads\RTY03-24Last.txt'  # Update this to your dataset's file path
    result = analyze_sudden_increases(file_path)
    print("Hours during which 70% of sudden increases occur:")
    print(result)
