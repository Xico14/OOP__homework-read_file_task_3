import os

current_directory = os.getcwd()
sorted_directory = os.path.join(current_directory, "sorted")

with open("result.txt", "w", encoding="utf-8") as result_file:
    file_names = os.listdir(sorted_directory)
    text_file_names = [file_name for file_name in file_names if file_name.startswith("txt_") and file_name.endswith(".txt")]
    file_info = [(file_name, sum(1 for _ in open(os.path.join(sorted_directory, file_name), encoding="utf-8"))) for file_name in text_file_names]
    file_info.sort(key=lambda x: x[1])

    for file_name, line_count in file_info:
        result_file.write(f"\n{file_name}\n{line_count}\n")

        with open(os.path.join(sorted_directory, file_name), "r", encoding="utf-8") as input_file:
            result_file.write(input_file.read())

# with open("result.txt", "r", encoding="utf-8") as result_file:
#     print(result_file.read())