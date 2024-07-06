import argparse
import pyarrow as pa
import pyarrow.csv as csv
import pyarrow.dataset as ds


def generate_csv(file):
    # create a list of dictionaries that will represent our dataset
    table = pa.table({'year': [2020, 2022, 2021, 2022, 2019, 2020, 2024],
                    'n_legs': [2, 2, 4, 4, 5, 100, 1],
                    'animal': ["Flamingo", "Parrot", "Dog", "Horse",
                                "Brittle stars", "Centipede", "Nick"]})

    # create a PyArrow dataset from the table
    dataset = ds.dataset(table)

    # create csv file with options
    options = csv.WriteOptions(include_header=True, batch_size=4096)
    csv.write_csv(table, file, options)

    # read the dataset back with options
    table = csv.read_csv(file, read_options=csv.ReadOptions(use_threads=True))

    # print the dataset
    print(table)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str,
                        help="CSV File to store")
    args = parser.parse_args()
    if args.file:
        generate_csv(args.file)


if __name__ == '__main__':
    main()