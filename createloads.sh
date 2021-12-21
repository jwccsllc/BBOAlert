#!/csoft/bin/bash
for conf in *.conf; do
	name=`basename $conf .conf`
	load=load$name.txt
	test -s $load || {
		echo $name $load
		echo "Import,https://raw.githubusercontent.com/jwccsllc/BBOAlert/master/${name}.txt" >> $load
	}
done
