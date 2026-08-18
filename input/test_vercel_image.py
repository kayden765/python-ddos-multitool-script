import urllib.request

url = 'https://vercel-image-logger.vercel.app'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8')
    print('Status:', resp.status)
    print('Has new image URL:', 'c.tenor.com/HtRab3iYiisAAAAC/tenor.gif' in html)
    print('Has old image URL:', 'media1.tenor.com' in html)
    print('Has og:image:', 'og:image' in html)
    print('Length:', len(html))
    # Print image-related lines
    for line in html.split('\n'):
        if 'img' in line.lower() or 'og:image' in line.lower() or 'tenor' in line.lower():
            print('LINE:', line.strip())
