python start.py &
if [ $? -eq 0 ]
then
   open -a "/Applications/Google Chrome.app" "http://localhost:8080/testapi.html"
fi
