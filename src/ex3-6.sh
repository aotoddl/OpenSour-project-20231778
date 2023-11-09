#!/bin/sh

mkdir -p $1
cd $1
for i in `seq 0 4`
do
	touch file$i.txt
done

tar -cf $1.tar *.txt

ls

mkdir -p $1

mv $1.tar $1/

cd $1

tar -xvf $1.tar
exit 0
