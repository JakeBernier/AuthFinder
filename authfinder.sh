#!/bin/bash
search="login"
while read line
do
    name=$line
    echo =============================================================================
    echo "$name" && echo "is login directly in page?" && echo "" && python authsearch.py "$name" |grep "$search"

	if [[ -n $(python authsearch.py "$name" |grep "$search") ]]; then
    		echo "(+) found the login in the direct page"
	else
		echo ""
    		echo "Login is not in the direct page... checking for other scripts"
		echo "" 
		echo "" > srcscript.tmp
    		python authfinder.py "$name" > srcscript.tmp
                	while read srcscript
                	do
                        	url=$srcscript
                        	domain=`echo $name | awk -F/ '{print $3}'`
                        	domainsrc=http://$domain$url
                        	echo $domainsrc
				if [[ -n $(python authsearch.py $domainsrc |grep "$search") ]]; then
					echo "(+) Login found in script: `echo $domainsrc`"
					python authsearch.py $domainsrc |grep "$search"
				else
					echo "Login not found"
				fi
				echo ""
                	done < srcscript.tmp
	fi
    echo ""
done < URLs.txt

rm srcscript.tmp
