import pyarrow as pa
import pyarrow.csv as csv
import pyarrow.dataset as ds

DATA_CSV_FILE="samples.csv"

# create a list of dictionaries that will represent our dataset
table = pa.table({'year': [2020, 2022, 2021, 2022, 2019, 2020, 2024],
                  'n_legs': [2, 2, 4, 4, 5, 100, 1],
                  'animal': ["Flamingo", "Parrot", "Dog", "Horse",
                             "Brittle stars", "Centipede", "Nick"]})

# create a PyArrow dataset from the table
dataset = ds.dataset(table)

# create csv file with options
options = csv.WriteOptions(include_header=True, batch_size=4096)
csv.write_csv(table, DATA_CSV_FILE, options)

# read the dataset back with options
table = csv.read_csv(DATA_CSV_FILE, read_options=csv.ReadOptions(use_threads=True))

# print the dataset
print(table)
