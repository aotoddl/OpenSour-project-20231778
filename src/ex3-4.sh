#!/bin/sh

echo "리눅스가 재미있나요? (yes / no)"
read mind
case "$mind" in
	[yY]*)
		echo "yes";;
	[nN]*)
		echo "no";;
	*)
		echo "yes of no로 입력해 주세요.";;
esac


exit 0
