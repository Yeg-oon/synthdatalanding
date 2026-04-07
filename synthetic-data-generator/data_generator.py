import pandas as pd
import random
import string
from faker import Faker
from datetime import datetime, timedelta

class SyntheticDataGenerator:
    def __init__(self):
        self.fake = Faker()
        
    def generate_value(self, data_type):
        """Generate a single value based on data type"""
        if data_type == "Name":
            return self.fake.name()
        elif data_type == "Email":
            return self.fake.email()
        elif data_type == "Address":
            return self.fake.address().replace('\n', ', ')
        elif data_type == "Phone Number":
            return self.fake.phone_number()
        elif data_type == "Company Name":
            return self.fake.company()
        elif data_type == "Date":
            return self.fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d')
        elif data_type == "Integer":
            return random.randint(1, 10000)
        elif data_type == "Float":
            return round(random.uniform(1.0, 10000.0), 2)
        elif data_type == "Text/Job Title":
            return self.fake.job()
        elif data_type == "Country":
            return self.fake.country()
        else:
            return ""
    
    def add_noise(self, value, data_type):
        """Add noise/imperfection to a value"""
        if value is None or value == "":
            return value
            
        noise_type = random.choice(['null', 'typo'])
        
        if noise_type == 'null':
            return None
        elif noise_type == 'typo' and isinstance(value, str):
            # Introduce simple typos
            if len(value) > 3:
                typo_positions = random.sample(range(len(value)), min(2, len(value)//4))
                value_list = list(value)
                for pos in typo_positions:
                    if value_list[pos].isalpha():
                        value_list[pos] = random.choice(string.ascii_letters)
                    elif value_list[pos].isdigit():
                        value_list[pos] = random.choice(string.digits)
                return ''.join(value_list)
        return value
    
    def generate_data(self, columns, row_count, noise_level):
        """Generate synthetic data with specified parameters"""
        data = {}
        
        for column_name, data_type in columns.items():
            column_data = []
            
            for _ in range(row_count):
                value = self.generate_value(data_type)
                
                # Apply noise based on noise level
                if random.random() < (noise_level / 100):
                    value = self.add_noise(value, data_type)
                
                column_data.append(value)
            
            data[column_name] = column_data
        
        return pd.DataFrame(data)
    
    def generate_csv(self, columns, row_count, noise_level):
        """Generate CSV content"""
        df = self.generate_data(columns, row_count, noise_level)
        return df.to_csv(index=False)
