s=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
echo $s > random_string.txt
while true; do echo $(date) $s; sleep 5; done
