# Broker settings.
broker_url = 'pyamqp://guest@localhost//'

# Using the database to store task state and results.
result_backend = 'mongodb://localhost:27017/'
mongodb_backend_settings = {
    'database': 'celery',
    'taskmeta_collection': 'tasks_collection',
}
