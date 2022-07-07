import sys
import json

jsonify = "--json" in sys.argv

with open(sys.argv[1]) as f:
    line_count = 0
    for line in f:
        line_count += 1

with open("all_req_out.txt", "w") as f:
    if jsonify:
        f.write(json.dumps({"total_number_of_requests": line_count}))
    else:
        f.write(f"Total number of requests\n{line_count}")
