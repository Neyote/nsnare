import hashlib
import os


def calculate_file_hash(filepath):
    """Calculate the SHA512 hash of a file."""
    hash_sha512 = hashlib.sha512()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha512.update(chunk)
        return hash_sha512.hexdigest()


def remove_old_baseline():
    if os.path.exists('nsnarebaseline.txt'):
        os.remove('nsnarebaseline.txt')


def collect_new_baseline():
    """Remove old baseline, create new one and populate it with
       file paths and the corresponding hash"""
    remove_old_baseline()
    target_directory = './files_to_scan/'
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    baseline_file_name = 'nsnarebaseline.txt'
    files = [x for x in os.listdir(target_directory)
             if os.path.isfile(os.path.join(target_directory, x))
             and not x.startswith('.')]
    with open(baseline_file_name, 'a') as baseline_file:
        for x in files:
            file_path = os.path.join(target_directory, x)
            file_hash = calculate_file_hash(file_path)
            baseline_file.write(f"{file_path}|{file_hash}\n")
    print(f"Baseline created at {target_directory}{baseline_file_name}")


def check_integrity():
    """Check for new, deleted, and changed files using the baseline
       file and the current state of the target directory"""
    target_directory = './files_to_scan'
    baseline_dictionary, current_dictionary = {}, {}
    changed_files, removed_files, added_files = [], [], []
    files = [x for x in os.listdir(target_directory)
             if os.path.isfile(os.path.join(target_directory, x))
             and not x.startswith('.')]
    """This will read the lines of the baseline file
       and populate a dictionary with the path and hash of each file"""
    with open('nsnarebaseline.txt', 'r') as baseline_file:
        for line in baseline_file.readlines():
            file_path = line.split('|')[0]
            file_hash = line.split('|')[1].strip('\n')
            baseline_dictionary[file_path] = file_hash
    """This will hash the current files in the target directory
       and populate a dictionary with the path and hash of each file"""
    for x in files:
        file_path = os.path.join(target_directory, x)
        file_hash = calculate_file_hash(file_path)
        current_dictionary[file_path] = file_hash
    """These will run all of the comparisons of the current state
       of the directory against the baseline file"""
    removed_files = [x for x in baseline_dictionary.keys()
                     if x not in current_dictionary]
    for current_file, current_file_hash in current_dictionary.items():
        if current_file not in baseline_dictionary:
            added_files.append(current_file)
        elif baseline_dictionary[current_file] != current_file_hash:
            changed_files.append(current_file)
        else:
            continue
    return added_files, removed_files, changed_files


def print_integrity_information(files_added, files_removed, files_changed):
    print("\n-----Here are the integrity check results-----\n\n")
    for file in files_added:
        print(f"[+] New file: {file}\n")
    for file in files_removed:
        print(f"[-] Removed file: {file}\n")
    for file in files_changed:
        print(f"[!] File changed: {file}\n")


def main():
    print("\nWhat would you like to do?\n")
    print("1) Create baseline")
    print("2) Check file integrity against baseline")
    response = input("Please enter your option number: ")
    match response:
        case "1":
            collect_new_baseline()
        case "2":
            integrity_results = check_integrity()
            print_integrity_information(integrity_results[0],
                                        integrity_results[1],
                                        integrity_results[2])
        case _:
            print("Please select a valid option.")
            main()


if __name__ == '__main__':
    main()
