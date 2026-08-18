export default async function handler(req, res) {
  const ip = req.headers['x-forwarded-for']?.split(',')[0]?.trim() || req.headers['x-real-ip'] || req.socket.remoteAddress || 'unknown';
  const userAgent = req.headers['user-agent'] || 'unknown';
  const timestamp = new Date().toISOString();

  const logEntry = { ip, userAgent, timestamp, url: req.url };
  const logLine = JSON.stringify(logEntry) + '\n';

  try {
    const fs = await import('fs');
    const path = await import('path');
    const os = await import('os');
    
    const logDir = path.join(os.tmpdir(), 'image-logger');
    const logFile = path.join(logDir, 'logs.jsonl');
    
    if (!fs.existsSync(logDir)) {
      fs.mkdirSync(logDir, { recursive: true });
    }
    fs.appendFileSync(logFile, logLine);
  } catch (e) {
    console.error('Log write failed:', e);
  }

  if (req.method === 'GET' && (req.url === '/logs' || req.url === '/api/logs')) {
    try {
      const fs = await import('fs');
      const path = await import('path');
      const os = await import('os');
      
      const logFile = path.join(os.tmpdir(), 'image-logger', 'logs.jsonl');
      if (fs.existsSync(logFile)) {
        const data = fs.readFileSync(logFile, 'utf8');
        const lines = data.trim().split('\n').filter(Boolean);
        const logs = lines.map(line => JSON.parse(line));
        res.setHeader('Content-Type', 'application/json');
        res.status(200).json(logs);
      } else {
        res.status(200).json([]);
      }
    } catch (e) {
      res.status(500).json({ error: 'Failed to read logs' });
    }
    return;
  }

  try {
    const https = await import('https');
    const imageUrl = 'https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif';
    
    https.get(imageUrl, (imageRes) => {
      const chunks = [];
      imageRes.on('data', (chunk) => chunks.push(chunk));
      imageRes.on('end', () => {
        const buffer = Buffer.concat(chunks);
        res.setHeader('Content-Type', 'image/gif');
        res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
        res.setHeader('Pragma', 'no-cache');
        res.setHeader('Expires', '0');
        res.setHeader('Content-Length', buffer.length);
        res.status(200).send(buffer);
      });
    }).on('error', () => {
      res.setHeader('Content-Type', 'text/html; charset=utf-8');
      res.status(200).send(`<!DOCTYPE html><html><head><meta property="og:image" content="https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif"></head><body><img src="https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif"></body></html>`);
    });
  } catch (e) {
    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    res.status(200).send(`<!DOCTYPE html><html><head><meta property="og:image" content="https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif"></head><body><img src="https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif"></body></html>`);
  }
}
