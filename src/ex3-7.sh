#!/bin/sh

mkdir -p $1
cd $1
for i in `seq 0 4`
do		
	file_name=file$i
	touch $file_name.txt
	mkdir -p $file_name
	ln -s ../$file_name.txt $file_name/
done

exit 0
