import urllib.request

url = 'https://vercel-image-logger.vercel.app'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    print('Status:', resp.status)
    print('Content-Type:', resp.headers.get('Content-Type'))
    print('Content-Length:', resp.headers.get('Content-Length'))
    data = resp.read()
    print('Is GIF:', data[:3] == b'GIF')
    print('Bytes:', len(data))
