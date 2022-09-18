conda info -e | grep open_url
if [ $? -eq 1 ]; then
	conda create -n open_url python=3.9 -y
	pip install selenium webdriver_manager
fi
source activate open_url
URLS=`python print_onetab_url.py $1`
open $URLS
