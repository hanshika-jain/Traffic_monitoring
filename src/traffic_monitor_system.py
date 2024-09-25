import pandas as pd

# Defining a TrafficMonitor class
class TrafficMonitor:
    def __init__(self, data):
    
        self.data = data
    
    def calculate_peak_hours(self):
        
        # Identifying peak hours based on the highest vehicle count.
        
        peak_hours = self.data.loc[self.data['vehicle_count'] == self.data['vehicle_count'].max()]
        return peak_hours
    
    def recommend_alternative_routes(self, speed_threshold=15):
        """
        Recommend alternative routes when average speed is below the threshold.
        Default speed threshold is set to 15 km/h.
        """
        slow_traffic = self.data.loc[self.data['average_speed'] < speed_threshold]
        recommendations = []
        
        for index, row in slow_traffic.iterrows():
            recommendations.append(f"Recommendation: Avoid {row['location']} at {row['time_of_day']} due to slow traffic (speed: {row['average_speed']} km/h).")
        
        return recommendations

    def interactive_monitor(self):
        
        #Interactive method that allows users to select functionality: peak hours or recommendations.
        
        while True:
            print("\nWhat would you like to do?")
            print("1. Check peak hours for traffic congestion.")
            print("2. Get recommendations for alternative routes.")
            print("3. Exit.")
            
            choice = input("Enter your choice (1/2/3): ")
            
            if choice == '1':
                peak_hours = self.calculate_peak_hours()
                print("\nPeak Hours for Traffic Congestion:")
                print(peak_hours)
            
            elif choice == '2':
                speed_threshold = input("Enter the speed threshold for slow traffic (default is 15 km/h): ")
                speed_threshold = float(speed_threshold) if speed_threshold else 15
                recommendations = self.recommend_alternative_routes(speed_threshold)
                
                print("\nAlternative Route Recommendations:")
                for rec in recommendations:
                    print(rec)
            
            elif choice == '3':
                print("Exiting the program.")
                break
            
            else:
                print("Invalid choice, please try again.")


# Reading the dataset
df = pd.read_csv('D:/traffic_monitoring/data/traffic_data.csv')

# Instantiate the TrafficMonitor class
traffic_monitor = TrafficMonitor(df)

# Call the interactive monitor
traffic_monitor.interactive_monitor()
