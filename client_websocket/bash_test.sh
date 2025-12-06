# #!/usr/bin/env bash
# echo "Shebang works! Running on $(date)"









# #!/usr/bin/env bash
# name="Alice"
# age=25
# empty=""
# echo "Name: $name"
# echo "Age: $age"
# echo "Empty length: ${#empty}"










# #!/usr/bin/env bash
# today=$(date +%Y-%m-%d)
# user=$(whoami)
# echo "Today: $today"
# echo "User: $user"












# #!/usr/bin/env bash
# ((sum = 10 + 5))
# echo "Sum: $sum"

# # This will cause runtime error
# echo "10 / 0 = $((10 / 0))"











# #!/usr/bin/env bash
# echo "enter your marks:"
# read score

# if (( score >= 90 )); then
#     echo "Grade: A"
# elif (( score >= 80 )); then
#     echo "Grade: B"
# else
#     echo "Grade: C or below"
# fi








# #!/usr/bin/env bash
# fruit="banana"

# if [[ $fruit == "banana" ]]; then
#     echo "It's banana"
# elif [[ $fruit == "apple" ]]; then
#     echo "It's apple"
# fi









# #!/usr/bin/env bash
# touch /tmp/testfile
# if [[ -f /tmp/testfile ]]; then
#     echo "File exists"
#     rm /tmp/testfile
# else
#     echo "File missing"
# fi





# #!/usr/bin/env bash
# for i in 1 2 3 4 5; do
#     echo "Count: $i"
# done








# #!/usr/bin/env bash
# count=1
# while (( count <= 3 )); do
#     echo "While: $count"
#     ((count++))
# done








# #!/usr/bin/env bash
# count=1
# until (( count > 3 )); do
#     echo "Until: $count"
#     ((count++))
# done














# #!/usr/bin/env bash
# greet() {
#     echo "Hello, $1!"
# }
# greet "Bob"
# greet "Alice"










# #!/usr/bin/env bash
# colors=("red" "green" "blue")
# echo "First: ${colors[0]}"
# echo "All: ${colors[@]}"
# echo "Length: ${#colors[@]}"









# #!/usr/bin/env bash
# declare -A user
# user[name]="Rahul"
# user[city]="Delhi"
# echo "Name: ${user[name]}"
# echo "City: ${user[city]}"








# #!/usr/bin/env bash
# echo "Enter your name:"
# read username
# echo "Hello, $username!"







# #!/usr/bin/env bash
# read -p "Enter age: " age
# echo "You are $age years old."





# #!/usr/bin/env bash
# read -s -p "Enter password: " pass
# echo
# echo "Password length: ${#pass}"









# #!/usr/bin/env bash
# if read -t 5 -p "Type something in 5 sec: " input; then
#     echo "You typed: $input"
# else
#     echo "Timeout! No input."
# fi



# #!/usr/bin/env bash
# echo "Saved to file" > /tmp/output.txt
# cat /tmp/output.txt
# rm -r /tmp/output.txt






# #!/usr/bin/env bash
# echo "Line 1" > /tmp/log.txt
# echo "Line 2" >> /tmp/log.txt
# cat /tmp/log.txt
# echo "------------"
# echo "line 3" > /tmp/log.txt
# cat /tmp/log.txt
# rm -r /tmp/log.txt





# #!/usr/bin/env bash
# echo -e "apple\nbanana\ncherry" | grep "a"




# #!/usr/bin/env bash
# ls /nonexistent 2>/dev/null
# if [[ $? -ne 0 ]]; then
#     echo "Command failed (as expected)"
# else
#     echo "Command succeeded"
# fi




# #!/usr/bin/env bash
# this_command_does_not_exist
# echo "This won't print"
# echo -e "apple\nbanana\ncherry" | grep "a"







# #!/usr/bin/env bash
# if true; then
#     echo "Missing fi below"
# # fi  # ← Remove this line to trigger error


# #!/usr/bin/env bash
# msg="This quote is never closed
# echo "$msg"






# #!/usr/bin/env bash
# [ 5 -gt ]






# #!/usr/bin/env bash
# arr=(a b c)
# echo "${arr[10]}"
# echo "Script continues..."





# #!/usr/bin/env bash
# set -e
# echo "This will print"
# false
# echo "This will NOT print"






# #!/usr/bin/env bash
# set -x
# name="Debug"
# echo "Name is $name"
# set +x
# echo "Debug off"





# #!/usr/bin/env bash
# cat << EOF
# This is line 1
# This is line 2
# EOF






echo "-----------"
echo "--> pwd"
pwd
echo "-----------"
echo "--> ls -l"
ls -l
echo "-----------"
echo "--> cd .."
cd ..
echo "-----------"
echo "--> pwd"
pwd
echo "-----------"
echo "--> ls -l"
ls -l
echo "-----------"
echo "--> cd .."
cd ..
echo "-----------"
echo "--> pwd"
pwd
echo "-----------"
echo "--> ls -l"
ls -l
echo "-----------"















