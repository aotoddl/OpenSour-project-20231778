name=$1
phone=$2
db="DB.txt"

if [ ! -f "$db" ];
then
	touch "$db"
fi


echo "$name $phone" >> "$db"

exit 0
