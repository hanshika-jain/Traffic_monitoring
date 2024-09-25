import unittest
import pandas as pd
from src.traffic_monitor_system import TrafficMonitor 
class TestTrafficMonitor(unittest.TestCase):
    
    def setUp(self):
        # Create a sample dataset for testing
        data = {
            'vehicle_count': [100, 200, 300, 400],
            'time_of_day': ['08:00', '09:00', '10:00', '11:00'],
            'location': ['Location A', 'Location B', 'Location C', 'Location D'],
            'average_speed': [10, 20, 5, 15]
        }
        self.df = pd.DataFrame(data)
        self.traffic_monitor = TrafficMonitor(self.df)

    def test_calculate_peak_hours(self):
        peak_hours = self.traffic_monitor.calculate_peak_hours()
        self.assertEqual(len(peak_hours), 1)  # Expecting one peak hour
        self.assertEqual(peak_hours['vehicle_count'].values[0], 400)  # Check peak count

    def test_recommend_alternative_routes(self):
        recommendations = self.traffic_monitor.recommend_alternative_routes(speed_threshold=15)
        self.assertEqual(len(recommendations), 2)  # Expecting recommendations for two entries
        self.assertIn("Recommendation: Avoid Location A at 08:00 due to slow traffic (speed: 10 km/h).", recommendations)
        self.assertIn("Recommendation: Avoid Location C at 10:00 due to slow traffic (speed: 5 km/h).", recommendations)

    def test_incorrect_data_format(self):
        with self.assertRaises(KeyError):
            self.traffic_monitor = TrafficMonitor(pd.DataFrame({'incorrect_column': [1, 2, 3]}))
            self.traffic_monitor.calculate_peak_hours()

    def test_missing_entries(self):
        # Introduce NaN values
        self.df.at[0, 'vehicle_count'] = None
        self.traffic_monitor = TrafficMonitor(self.df)
        recommendations = self.traffic_monitor.recommend_alternative_routes()
        self.assertEqual(len(recommendations), 2)  # Still expecting recommendations for two entries

if __name__ == '__main__':
    unittest.main()
