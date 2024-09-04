#!/bin/bash

# Navigate to the application directory
cd /home/ubuntu/simple-web-server

# Kill any existing server instances
pkill -f simple_web_server.py || true

# Start the web server
nohup python3 simple_web_server.py &
