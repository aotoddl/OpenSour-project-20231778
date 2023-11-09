#!/bin/sh
number1=$1
operator=$2
number2=$3


if [ $operator = "+" ]
then
	echo `expr $number1 + $number2`
elif [ $operator = "-" ]
then
	echo `expr $number1 - $number2`
elif [ $operator = "/" ]
then
	echo `expr $number1 / $number2`
elif [ $operator = "*" ] 
then
	echo `expr $number1 \* $number2`
fi
	
exit 0
