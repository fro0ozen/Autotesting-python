import sys
import json

jsonify = "--json" in sys.argv

unsorted_dct = {}
sorted_dict = {}
with open(sys.argv[1]) as f:
    lst = [i.split()[6] for i in f]
    for i in lst:
        if unsorted_dct.get(i, False):
            unsorted_dct[i] += 1
        else:
            unsorted_dct[i] = 1

    sorted_values = sorted(unsorted_dct.values(), reverse=True)
    for i in sorted_values:
        for k in unsorted_dct.keys():
            if unsorted_dct[k] == i:
                sorted_dict[k] = unsorted_dct[k]
                unsorted_dct.pop(k)
                break

with open("frequent_req_out.txt", "w") as f:
    if jsonify:
        json_lst = []
        for i in list(sorted_dict.keys())[:10]:
            json_lst.append({"requests_number_for_url": sorted_dict[i], "url": i})
        f.write(json.dumps(json_lst))
    else:
        f.write("Top 10 most frequent searches\n")
        for i in list(sorted_dict.keys())[:10]:
            f.write(f"{sorted_dict[i]} {i}\n")
