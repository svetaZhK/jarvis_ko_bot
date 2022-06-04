import pyexcel
# make sure you had pyexcel-xls installed
a_list_of_dictionaries = [
    # {
    #     "Name": 'Adam',
    #     "Address": 28
    # },
    # {
    #     "Name": 'Beatrice',
    #     "Address": 29
    # },
    # {
    #     "Name": 'Ceri',
    #     "Address": 30
    # },
    # {
    #     "Name": 'Dean',
    #     "Address": 26
    # }
]
for age in range(1, 1000):
    a_list_of_dictionaries.append({
        "Name": 'Adam',
        "Age": age
    })

pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xls")
