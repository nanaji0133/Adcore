import pandas as pd
import requests
from io import StringIO
from .models import course_schema

def load_and_store_data(mongo):
    url = 'https://api.mockaroo.com/api/501b2790?count=1000&key=8683a1c0'
    response = requests.get(url)
    
    # Print a small part of the raw CSV data for debugging
    print("Raw CSV data sample (first 500 characters):")
    print(response.text[:500])
    
    df = pd.read_csv(StringIO(response.text))

    # Print the DataFrame columns and course_schema keys for debugging
    print("DataFrame columns:")
    print(df.columns.tolist())

    print("Course schema keys:")
    print(course_schema.keys())

    # Explicitly map CSV column names to course_schema keys
    column_mapping = {
        'University': 'university',
        'City': 'city',
        'Country': 'country',
        'CourseName': 'course_name',
        'CourseDescription': 'course_description',
        'StartDate': 'start_date',
        'EndDate': 'end_date',
        'Price': 'price',
        'Currency': 'currency'
    }
    df.rename(columns=column_mapping, inplace=True)

    # Print the normalized DataFrame columns for debugging
    print("Mapped DataFrame columns:")
    print(df.columns.tolist())

    # Clear existing data
    mongo.db.courses.drop()

    # Normalize data
    data = df.to_dict(orient='records')
    
    # Check for missing keys and log records for debugging
    required_keys = course_schema.keys()
    valid_data = []
    
    for record in data:
        missing_keys = [key for key in required_keys if key not in record]
        if missing_keys:
            # print(f"Skipping record due to missing keys: {missing_keys}")
            # print(f"Record keys: {list(record.keys())}")
            continue
        for key, value in course_schema.items():
            record[key] = value(record[key])
        valid_data.append(record)
    
    # Insert new data
    if valid_data:
        mongo.db.courses.insert_many(valid_data)
    else:
        print("No valid data to insert.")
