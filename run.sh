echo "Entering VirtualEnv"
source .env/bin/activate
echo "Starting Bot..."
echo "Miller is ALIVE"
echo "Press Crtl + C to stop the bot..."
./bot/run.py
echo "Bot stoped."
echo "Leaving VirtualEnv..."
deactivate
echo "Done."
