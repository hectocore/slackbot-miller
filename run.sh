echo "$(tput setaf 4)--> Entering VirtualEnv$(tput sgr 0)"
source .env/bin/activate
echo "$(tput setaf 4)--> Starting Bot...$(tput sgr 0)"
echo "$(tput setaf 4)--> Miller is ALIVE!$(tput sgr 0)"
echo "Press Ctrl+C to stop the bot...$(tput sgr 0)"
./bot/run.py
echo "$(tput setaf 4)--> Bot stoped.$(tput sgr 0)"
echo "$(tput setaf 4)--> Leaving VirtualEnv...$(tput sgr 0)"
deactivate
echo "$(tput setaf 4)--> Done.$(tput sgr 0)"
