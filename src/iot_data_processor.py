"""
Agricultural IoT Data Processor
Processes sensor data from agricultural IoT devices for analytics
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from typing import Dict, List, Optional
import json

class AgricultureIoTProcessor:
    """Process and analyze agricultural IoT sensor data"""
    
    def __init__(self, seed: int = 42):
        np.random.seed(seed)
        random.seed(seed)
        
        self.sensor_types = [
            'soil_moisture', 'soil_temperature', 'air_temperature', 
            'air_humidity', 'light_intensity', 'ph_level',
            'nitrogen_level', 'phosphorus_level', 'potassium_level'
        ]
        
        self.crop_types = [
            'Soja', 'Milho', 'Algodão', 'Cana-de-açúcar', 
            'Café', 'Trigo', 'Arroz', 'Feijão'
        ]
        
        self.farm_locations = [
            'Mato Grosso', 'Goiás', 'Minas Gerais', 'São Paulo',
            'Paraná', 'Rio Grande do Sul', 'Bahia', 'Mato Grosso do Sul'
        ]
    
    def generate_sensor_data(self, num_sensors: int = 100, days_back: int = 30) -> pd.DataFrame:
        """Generate IoT sensor data for agricultural monitoring"""
        sensor_data = []
        
        for sensor_id in range(1, num_sensors + 1):
            # Sensor metadata
            sensor_type = np.random.choice(self.sensor_types)
            farm_location = np.random.choice(self.farm_locations)
            crop_type = np.random.choice(self.crop_types)
            
            # Generate readings for the past days
            for day in range(days_back):
                # Multiple readings per day (every 4 hours)
                for hour in [0, 4, 8, 12, 16, 20]:
                    timestamp = datetime.now() - timedelta(days=day, hours=hour)
                    
                    # Generate realistic sensor values based on type
                    if sensor_type == 'soil_moisture':
                        value = max(0, min(100, np.random.normal(45, 15)))
                        unit = '%'
                    elif sensor_type == 'soil_temperature':
                        value = np.random.normal(22, 5)
                        unit = '°C'
                    elif sensor_type == 'air_temperature':
                        value = np.random.normal(25, 8)
                        unit = '°C'
                    elif sensor_type == 'air_humidity':
                        value = max(0, min(100, np.random.normal(60, 20)))
                        unit = '%'
                    elif sensor_type == 'light_intensity':
                        # Higher during day hours
                        base_value = 800 if 6 <= hour <= 18 else 50
                        value = max(0, np.random.normal(base_value, 200))
                        unit = 'lux'
                    elif sensor_type == 'ph_level':
                        value = max(4, min(9, np.random.normal(6.5, 0.8)))
                        unit = 'pH'
                    else:  # nutrient levels
                        value = max(0, np.random.normal(50, 20))
                        unit = 'ppm'
                    
                    # Add some seasonal variation
                    seasonal_factor = 1 + 0.2 * np.sin(2 * np.pi * day / 365)
                    value *= seasonal_factor
                    
                    reading = {
                        'sensor_id': f'SENSOR_{sensor_id:03d}',
                        'sensor_type': sensor_type,
                        'timestamp': timestamp,
                        'value': round(value, 2),
                        'unit': unit,
                        'farm_location': farm_location,
                        'crop_type': crop_type,
                        'latitude': -15.0 + np.random.uniform(-10, 10),
                        'longitude': -55.0 + np.random.uniform(-10, 10),
                        'battery_level': max(10, np.random.normal(80, 15)),
                        'signal_strength': max(-100, np.random.normal(-60, 20))
                    }
                    
                    sensor_data.append(reading)
        
        return pd.DataFrame(sensor_data)
    
    def generate_weather_data(self, days_back: int = 30) -> pd.DataFrame:
        """Generate weather data for correlation analysis"""
        weather_data = []
        
        for location in self.farm_locations:
            for day in range(days_back):
                date = datetime.now().date() - timedelta(days=day)
                
                # Generate realistic weather data
                temp_high = np.random.normal(28, 6)
                temp_low = temp_high - np.random.uniform(5, 15)
                humidity = max(0, min(100, np.random.normal(65, 20)))
                rainfall = max(0, np.random.exponential(2))
                wind_speed = max(0, np.random.normal(15, 8))
                
                weather = {
                    'date': date,
                    'location': location,
                    'temperature_high': round(temp_high, 1),
                    'temperature_low': round(temp_low, 1),
                    'humidity': round(humidity, 1),
                    'rainfall_mm': round(rainfall, 1),
                    'wind_speed_kmh': round(wind_speed, 1),
                    'uv_index': max(0, min(11, np.random.normal(6, 2)))
                }
                
                weather_data.append(weather)
        
        return pd.DataFrame(weather_data)
    
    def generate_crop_yield_data(self) -> pd.DataFrame:
        """Generate crop yield prediction data"""
        yield_data = []
        
        for location in self.farm_locations:
            for crop in self.crop_types:
                # Historical yield data
                base_yield = {
                    'Soja': 3200, 'Milho': 5500, 'Algodão': 1600,
                    'Cana-de-açúcar': 75000, 'Café': 1200, 'Trigo': 2800,
                    'Arroz': 4200, 'Feijão': 1800
                }.get(crop, 2000)
                
                # Add location and year variation
                location_factor = np.random.uniform(0.8, 1.2)
                year_factor = np.random.uniform(0.9, 1.1)
                
                predicted_yield = base_yield * location_factor * year_factor
                actual_yield = predicted_yield * np.random.uniform(0.85, 1.15)
                
                yield_record = {
                    'location': location,
                    'crop_type': crop,
                    'planting_date': datetime.now().date() - timedelta(days=np.random.randint(60, 120)),
                    'harvest_date': datetime.now().date() + timedelta(days=np.random.randint(30, 90)),
                    'area_hectares': np.random.uniform(50, 500),
                    'predicted_yield_kg_ha': round(predicted_yield, 0),
                    'actual_yield_kg_ha': round(actual_yield, 0),
                    'irrigation_type': np.random.choice(['Drip', 'Sprinkler', 'Flood', 'Rain-fed']),
                    'fertilizer_usage_kg_ha': np.random.uniform(100, 400)
                }
                
                yield_data.append(yield_record)
        
        return pd.DataFrame(yield_data)
    
    def analyze_sensor_patterns(self, sensor_df: pd.DataFrame) -> Dict:
        """Analyze patterns in sensor data"""
        analysis = {}
        
        for sensor_type in self.sensor_types:
            type_data = sensor_df[sensor_df['sensor_type'] == sensor_type]
            
            if len(type_data) > 0:
                analysis[sensor_type] = {
                    'avg_value': type_data['value'].mean(),
                    'min_value': type_data['value'].min(),
                    'max_value': type_data['value'].max(),
                    'std_value': type_data['value'].std(),
                    'readings_count': len(type_data),
                    'locations': type_data['farm_location'].nunique()
                }
        
        return analysis
    
    def detect_anomalies(self, sensor_df: pd.DataFrame) -> pd.DataFrame:
        """Detect anomalies in sensor readings"""
        anomalies = []
        
        for sensor_type in self.sensor_types:
            type_data = sensor_df[sensor_df['sensor_type'] == sensor_type].copy()
            
            if len(type_data) > 10:
                # Calculate z-score for anomaly detection
                mean_val = type_data['value'].mean()
                std_val = type_data['value'].std()
                type_data['z_score'] = abs((type_data['value'] - mean_val) / std_val)
                
                # Flag anomalies (z-score > 2.5)
                anomaly_data = type_data[type_data['z_score'] > 2.5]
                
                for _, row in anomaly_data.iterrows():
                    anomaly = {
                        'sensor_id': row['sensor_id'],
                        'sensor_type': row['sensor_type'],
                        'timestamp': row['timestamp'],
                        'value': row['value'],
                        'expected_range': f"{mean_val-2*std_val:.1f} - {mean_val+2*std_val:.1f}",
                        'severity': 'High' if row['z_score'] > 3 else 'Medium',
                        'farm_location': row['farm_location']
                    }
                    anomalies.append(anomaly)
        
        return pd.DataFrame(anomalies)

if __name__ == "__main__":
    # Generate agricultural IoT data
    processor = AgricultureIoTProcessor()
    
    print("Generating IoT sensor data...")
    sensor_data = processor.generate_sensor_data(50, 30)
    
    print("Generating weather data...")
    weather_data = processor.generate_weather_data(30)
    
    print("Generating crop yield data...")
    yield_data = processor.generate_crop_yield_data()
    
    print("Analyzing sensor patterns...")
    patterns = processor.analyze_sensor_patterns(sensor_data)
    
    print("Detecting anomalies...")
    anomalies = processor.detect_anomalies(sensor_data)
    
    # Save data
    import os
    os.makedirs('../data', exist_ok=True)
    
    sensor_data.to_csv('../data/iot_sensor_data.csv', index=False)
    weather_data.to_csv('../data/weather_data.csv', index=False)
    yield_data.to_csv('../data/crop_yield_data.csv', index=False)
    anomalies.to_csv('../data/sensor_anomalies.csv', index=False)
    
    # Save analysis results
    with open('../data/sensor_analysis.json', 'w') as f:
        json.dump(patterns, f, indent=2, default=str)
    
    print(f"\n=== Dataset Summary ===")
    print(f"IoT Sensor Readings: {len(sensor_data)} records")
    print(f"Weather Data: {len(weather_data)} records")
    print(f"Crop Yield Data: {len(yield_data)} records")
    print(f"Anomalies Detected: {len(anomalies)} records")
    print(f"Sensor Types: {sensor_data['sensor_type'].nunique()}")
    print(f"Farm Locations: {sensor_data['farm_location'].nunique()}")
    print(f"Crop Types: {yield_data['crop_type'].nunique()}")

