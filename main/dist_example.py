"""""
Dist file for holding sensitive information. Blocked from commit via .gitignore
"""
import os

client_id = os.environ['APP_CLIENT_ID']
token = os.environ['APP_BOT_USER_TOKEN']
postgresql = 'postgresql://user:password@host/database'
