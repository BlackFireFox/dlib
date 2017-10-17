pre=/usr/local/bin/

install:
	mkdir -p $(pre)
	cp dlib $(pre)dlib
	chmod +x $(pre)dlib

uninstall:
	rm $(pre)dlib

reinstall:
	rm $(pre)dlib
	cp dlib $(pre)dlib
	chmod +x $(pre)dlib
