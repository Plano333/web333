#!/usr/bin/env python3
"""Run after `jekyll build`: python3 check_site.py. No dependencies."""
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent / '_site'
EXPECTED = ('', 'biblioteca', 'contactos', 'dicas-para-usar-um-radio-portatil',
            'faq', 'historia', 'mapa', 'mapa-plano-3-3-3', 'mesh-3-3-3',
            'plano-3-3-3', 'politica-de-cookies', 'politica-de-privacidade',
            'radio-comunicacoes-cb-e-pmr-446-off-grid', 'treino-semanal')
errors = []

class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if not value:
                continue
            urls = [value] if key in ('href', 'src') else []
            if key == 'srcset':
                urls = [part.strip().split()[0] for part in value.split(',')]
            if key == 'style':
                urls = re.findall(r'url\([\'\"]?([^\'\")]+)', value)
            for url in urls:
                path = unquote(urlsplit(url).path)
                if not url.startswith('/') or url.startswith('//'):
                    continue
                target = ROOT / path.lstrip('/')
                if path.endswith('/'):
                    target /= 'index.html'
                if not target.is_file():
                    errors.append(f'{current}: missing {path}')

for route in EXPECTED:
    current = route or 'home'
    file = ROOT / route / 'index.html'
    if not file.is_file():
        errors.append(f'{current}: page missing')
        continue
    text = file.read_text(encoding='utf-8')
    if '{%' in text or '{{' in text:
        errors.append(f'{current}: unrendered Liquid')
    if '/wp-content/' in text or '/wp-includes/' in text:
        errors.append(f'{current}: WordPress asset reference')
    for tag in ('header', 'main', 'footer', 'title'):
        if len(re.findall(r'<' + tag + r'\b', text)) != 1:
            errors.append(f'{current}: expected exactly one {tag}')
    if not re.search(r'<title>\s*[^<\s]', text):
        errors.append(f'{current}: empty page title')
    ids = set(re.findall(r'\bid="([^"]+)"', text))
    for fragment in re.findall(r'href="#([^"]+)"', text):
        if unquote(fragment) not in ids:
            errors.append(f'{current}: missing anchor #{fragment}')
    Links().feed(text)

for stylesheet in ROOT.rglob('*.css'):
    current = str(stylesheet.relative_to(ROOT))
    for url in re.findall(r'url\([\'\"]?([^\'\")]+)', stylesheet.read_text(encoding='utf-8')):
        if url.startswith(('data:', 'https:', 'http:', '//', '#')):
            continue
        path = unquote(urlsplit(url).path)
        target = ROOT / path.lstrip('/') if path.startswith('/') else stylesheet.parent / path
        if not target.is_file():
            errors.append(f'{current}: missing {path}')

assert not errors, '\n'.join(errors)
print(f'PASS: {len(EXPECTED)} pages; HTML/CSS assets resolve; no Liquid or WordPress assets remain.')
