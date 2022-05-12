compile c:
	rm -fr build dist *.spec
	
	pyinstaller app.py \
		--onefile \
		-n hera
	
	mv dist/* .
	rm -fr build dist *.spec
		