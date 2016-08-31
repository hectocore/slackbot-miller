echo "This script will install/update Miller Slackbot."
echo "Warning! python 3 and virtualenv must be installed on your 
machine."
echo "Updating slackbot-miller from git"
git pull
echo "Creating VirtualEnv .env"
virtualenv .env
echo "Entering .env"
source .env/bin/activate
pip install slackbot
deactivate
echo "End of installation."
echo "Done."
