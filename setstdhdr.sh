#!/csoft/bin/bash

for conf in "$@"; do #{
	cp $conf $conf.bak
	shtool subst \
		-e '/modules/s/=/= stdhdr.txt/' \
		$conf
done #}
