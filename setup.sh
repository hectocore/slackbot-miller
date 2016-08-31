echo "$(tput setaf 4)--> This script will install/update Miller Slackbot.$(tput sgr 0)"
echo "$(tput setaf 3)--> Warning! python 3 and virtualenv must be installed on your machine.$(tput sgr 0)"
echo "$(tput setaf 4)--> Updating slackbot-miller from git$(tput sgr 0)"
git pull
echo "$(tput setaf 4)--> Creating VirtualEnv .env$(tput sgr 0)"
virtualenv .env
echo "$(tput setaf 4)--> Entering VirtualEnv$(tput sgr 0)"
source .env/bin/activate
echo "$(tput setaf 4)--> Installing Python plugins$(tput sgr 0)"
pip install --upgrade slackbot
echo "$(tput setaf 4)--> Leaving VirtualEnv$(tput sgr 0)"
deactivate
echo "$(tput setaf 4)--> End of installation.$(tput sgr 0)"
echo "$(tput setaf 4)--> Done.$(tput sgr 0)"
