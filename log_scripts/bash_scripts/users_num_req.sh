#! /bin/bash
file=$1
echo "Top 5 users by the number of requests that ended with a server error" > users_num_req_out.txt
grep '" 5[0-9][0-9] ' $file | cut -d ' ' -f 1 | sort | uniq -c | sort -rn | head -5 >> users_num_req_out.txt
