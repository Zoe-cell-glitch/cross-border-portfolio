import re, sys
sys.stdout.reconfigure(encoding='utf-8')
content = open('C:\\Users\\admin\\Documents\\运营助理\\index.html','r',encoding='utf-8').read()
print('FILE SIZE:', len(content), 'bytes =', round(len(content)/1024,1), 'KB')
print()
print('=== SECTION SIZES ===')
sections = ['Hero','Marquee','About','Skills','Projects','Contact']
for s in sections:
    m = re.search(r'/\* === ' + s + r' === \*/', content)
    if m: print(f'  {s}: at byte {m.start()}')
print()

# Count external resources
scripts = re.findall(r'<script[^>]+src=\"([^\"]+)\"', content)
print('=== EXTERNAL SCRIPTS (', len(scripts), ') ===')
for s in scripts: print(' ', s)

styles = re.findall(r'<link[^>]+href=\"([^\"]+)\"', content)
print('=== EXTERNAL CSS (', len(styles), ') ===')
for s in styles: print(' ', s)

videos = re.findall(r'<source[^>]+src=\"([^\"]+)\"', content)
print('=== VIDEOS ===')
for s in videos: print(' ', s)

imgs = re.findall(r'<img[^>]+src=\"([^\"]+)\"', content)
marquee_imgs_count = content.count('motionsites.ai')
print('=== IMAGES ===')
for s in imgs: print(' ', s)
print('  Marquee gifs (motionsites.ai):', marquee_imgs_count)
about_imgs = re.findall(r'img:\"([^\"]+)\"', content)
print('  Projects img fields:', len(about_imgs))
print()

# Check font sizes
fonts = re.findall(r'fontSize:\"([^\"]+)\"', content)
print('=== FONT SIZES USED ===')
for f in sorted(set(fonts)): print(' ', f)
print()

# Check GSAP animations
gsap_count = len(re.findall(r'gsap\.', content))
scrolltrigger_count = len(re.findall(r'ScrollTrigger', content))
print('=== GSAP ===')
print('  gsap calls:', gsap_count)
print('  ScrollTrigger refs:', scrolltrigger_count)

# Check scroll listeners
scroll_events = len(re.findall(r'scroll', content))
print('  scroll event refs:', scroll_events)

# Check for setTimeout/setInterval
intervals = len(re.findall(r'setInterval', content))
timeouts = len(re.findall(r'setTimeout', content))
print('  setInterval calls:', intervals)
print('  setTimeout calls:', timeouts)
print()

# Check curb loading
curtain = content.find('curtain')
preload = content.find('preload')
lazy = content.find('loading=\"lazy\"')
print('=== LOADING ===')
print('  Curtain loader:', 'YES' if curtain >= 0 else 'NO')
print('  preload attr:', 'YES' if preload >= 0 else 'NO')
print('  lazy loading:', lazy, 'occurrences')
