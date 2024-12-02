import pandas as pd

def aoc_day_1__pandas():
    data = pd.read_csv(
        "inputs/day_1_input.txt",
        sep="   ",
        engine='python',
        names=["source_id", "destination_id"]
    )

    sorted_source_ids = data[["source_id"]].sort_values(by=["source_id"])
    sorted_source_id_list = sorted_source_ids["source_id"].tolist()
    
    sorted_destination_ids = data[["destination_id"]].sort_values(by=["destination_id"])
    sorted_destination_id_list = sorted_destination_ids["destination_id"].tolist()

    total_distance_between = 0
    for source_id, destination_id in zip(sorted_source_id_list, sorted_destination_id_list):
        distance_between = abs(int(destination_id) - int(source_id))
        total_distance_between += distance_between

    return total_distance_between

# w/o Pandas
def aoc_day_1__no_pandas():
    source_ids = []
    destination_ids = []

    with open("inputs/day_1_input.txt") as f:
        data = f.readlines()
        for line in data:
            source_id, destination_id = line.split()
            source_ids.append(int(source_id))
            destination_ids.append(int(destination_id))

    total_distance_between = 0
    for source_id, destination_id in zip(sorted(source_ids), sorted(destination_ids)):
        distance_between = abs(destination_id - source_id)
        total_distance_between += distance_between

    return total_distance_between