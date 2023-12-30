
if [ -z "$1" ]; then 
	scons bh_slim -j4 pmlpp_shared=yes 
else 
	scons bh_slim -j4 pmlpp_shared=yes bin/libpmlpp.x11.opt.debug.64.so
fi


