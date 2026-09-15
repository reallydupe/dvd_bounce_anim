echo installing pyinstaller if not installed
pip install pyinstaller
echo Done!
pyinstaller main_logoSupport.py --onefile --name "DVD Bounce" --icon icon.ico --add-data "logo.png;." --noconsole
echo Done
echo "Cleaning pyinstaller temp files"
del build
del "DVD Bounce.spec"
echo Done!
pause