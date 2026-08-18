import urllib.request
import json

logs_url = 'https://vercel-image-logger.vercel.app/api/logs'
req = urllib.request.Request(logs_url, headers={'User-Agent': 'Mainframe-Monitor'})
with urllib.request.urlopen(req, timeout=10) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    print('Total logs:', len(data))
    for i, log in enumerate(data):
        print(f'Log {i}: ip={log.get("ip")}, url={log.get("url")}, ua={log.get("userAgent", log.get("user_agent"))[:50]}')
