import urllib.request

url = 'https://vercel-image-logger.vercel.app'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8')
    print('Status:', resp.status)
    print('Has og:image:', 'og:image' in html)
    print('Has img src:', '<img src="https://media1.tenor.com' in html)
    print('Length:', len(html))
