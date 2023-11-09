
#!/bin/sh

weight=$1
height_cm=$2

height_m=$(echo " $height_cm / 100" | bc -l)

BMI=$(echo " scale=2; $weight / ($height_m * $height_m) " | bc -l) 
if [ $(echo "$BMI < 18.5" | bc) -eq 1 ]
then
	echo "저체중입니다."
elif [ $(echo "$BMI >= 18.5" | bc) -eq 1 ] && [ $(echo "$BMI < 23.5" | bc) -eq 1 ]
then
	echo "정상체중입니다."
elif [ $(echo "$BMI >= 23" | bc) -eq 1 ]
then
	echo "과체중입니다."
else 
	echo "오류"
fi

exit 0
