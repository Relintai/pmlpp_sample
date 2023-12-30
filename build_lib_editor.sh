
if [ -z "$1" ]; then 
	scons bel_strip_slim -j4 editor_docs=no pmlpp_shared=yes 
else 
	scons bel_strip_slim -j4 editor_docs=no pmlpp_shared=yes bin/libpmlpp.x11.opt.tools.64.so
fi


