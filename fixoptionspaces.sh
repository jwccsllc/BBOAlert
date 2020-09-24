#!/csoft/bin/bash
# Needed for BBOalert 2.6.1 and later

shtool subst \
	-e '/^Option,.*\@/s/ /_/g' \
	"$@"
