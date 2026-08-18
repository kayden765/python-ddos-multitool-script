import re

sample_output = """https://vercel-image-logger-ktwxqsjy0-magmagts-projects.vercel.app  Inspect
  Production      https://vercel-image-logger-ktwxqsjy0-magmagts-projects.vercel.app
Building…
Running build in Washington, D.C., USA (East) – iad1
Build machine configuration: 2 cores, 8 GB
Retrieving list of deployment files...
Previous build caches not available.
Downloading 4 deployment files...
Running "vercel build"
Vercel CLI 58.1.0
Installing dependencies...
up to date in 411ms
Warning: Node.js functions are compiled from ESM to CommonJS. If this is not intended, add "type": "module" to your package.json file.
Compiling "track.js" from ESM to CommonJS...
Build Completed in /vercel/output [750ms]
Deploying outputs...
[2K[1A[2K[G  Production      https://vercel-image-logger-ktwxqsjy0-magmagts-projects.vercel.app
Completing…
▲ Aliased         https://vercel-image-logger.vercel.app
✓ Ready in 9s
Due to `builds` existing in your configuration file, the Build and Development Settings defined in your Project Settings will not apply. Learn More: https://vercel.link/unused-build-settings"""

combined = sample_output

alias_match = re.search(r'Aliased\s+(https?://[^\s]+\.vercel\.app)', combined)
url_match = re.search(r'https?://[^\s]+\.vercel\.app', combined)

if alias_match:
    print('Alias URL:', alias_match.group(1))
elif url_match:
    print('Deployment URL:', url_match.group(0))
else:
    print('No URL found')
