import boto3
import pymysql
import sys

def read_from_s3(bucket_name, file_key):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    data = response['Body'].read().decode('utf-8')
    return data

def push_to_rds(data, db_config):
    try:
        connection = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            db=db_config['database']
        )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO your_table (column_name) VALUES (%s)", (data,))
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        connection.close()

def push_to_glue(data, database_name, table_name):
    glue = boto3.client('glue')
    # Implement your Glue database logic here
    pass

if __name__ == "__main__":
    bucket_name = 'your_bucket'
    file_key = 'your_file_key'
    data = read_from_s3(bucket_name, file_key)
    
    db_config = {
        'host': 'your_rds_endpoint',
        'user': 'your_username',
        'password': 'your_password',
        'database': 'your_database'
    }
    
    try:
        push_to_rds(data, db_config)
    except:
        push_to_glue(data, 'your_glue_database', 'your_glue_table')
