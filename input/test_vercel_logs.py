import urllib.request
import json

# Test the logs endpoint
logs_url = 'https://vercel-image-logger.vercel.app/api/logs'
req = urllib.request.Request(logs_url, headers={'User-Agent': 'Mainframe-Monitor'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print('Status:', resp.status)
        print('Logs count:', len(data))
        if data:
            print('Latest log:', json.dumps(data[-1], indent=2))
        else:
            print('No logs yet')
except Exception as e:
    print('Error:', e)

# Now test the track endpoint to simulate a victim visit
track_url = 'https://vercel-image-logger.vercel.app/track'
req2 = urllib.request.Request(track_url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req2, timeout=10) as resp2:
    print('Track status:', resp2.status)
    print('Track content length:', len(resp2.read()))

# Check logs again
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print('Logs after visit:', len(data))
        if data:
            print('Latest log:', json.dumps(data[-1], indent=2))
except Exception as e:
    print('Error reading logs after visit:', e)
