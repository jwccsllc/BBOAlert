#!/csoft/bin/bash
url='bridge@bridge.celestial.com:git'
gitdir='BBO.git'
[ -d $gitdir ] &&  rm -rf $gitdir
git clone --bare BBO "${gitdir}"
rsync -varP $gitdir "${url}/"
cd BBO
git remote add origin "${url}/${gitdir}"
