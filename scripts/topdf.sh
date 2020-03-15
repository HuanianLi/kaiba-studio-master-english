#!/bin/bash
#
# Merge pages of pdf document to a new pdf file
#

function exec_cmd
{
	echo "$(id -un)@$(hostname)\$ $*"
	eval "$*"
	typeset -i rc=$?
	echo ""
	return $rc
}

i_start=${1?"*** start ***"}
i_end=${2?"*** end ***"}

pages=""
for (( i = i_start; i <= i_end; i++ )); do
	id=$(printf "%04d" $i)
	pages+=" pg_${id}.pdf"
done

dst=/tmp/pg_f${i_start}t${i_end}.pdf
exec_cmd pdftk $pages cat output $dst
exit $?
