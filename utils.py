import os
import re

def find_latest_name(directory, plain_name, regex_pattern):
    latest_num = -1
    latest_item = None
    found_plain = False

    for itemname in os.listdir(directory):
        if itemname == plain_name:
            found_plain = True
            continue
        
        match = re.fullmatch(regex_pattern, itemname)
        if match:
            found_num = int(match.group(1))
            if found_num > latest_num:
                latest_num = found_num
                latest_item = itemname

    if latest_item is not None:
        return os.path.join(directory, latest_item)
    elif found_plain:
        return os.path.join(directory, plain_name)
    else:
        return None

def find_latest_weights_dir(directory):
    latest_dir = find_latest_name(directory, 'train', r'train(\d+)')
    return os.path.join(latest_dir, "weights")

def find_latest_checkpoint(directory):
    return find_latest_name(directory, 'last.pt', r'last_(\d+)\.pt')