#! /bin/bash
file=$1
echo "Top 5 largest requests that failed with client error" > largest_req_out.txt
grep '" 4[0-9][0-9] ' $file | sort -nk10 -r | cut -f 1,7,9,10 -d ' ' | head -5 >> largest_req_out.txt
