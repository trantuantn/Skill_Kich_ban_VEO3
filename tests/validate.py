"""Structural checks only; never evaluates generated Veo video."""
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ['SKILL.md','README.md','CHANGELOG.md','agents/openai.yaml']
REQUIRED += ['references/'+x+'.md' for x in ['prompt-framework','character-lock','style-scene-lock','camera-motion','image-to-video','multi-scene-workflow','educational-content','dialogue-audio','quality-control','lessons-learned']]
REQUIRED += ['templates/'+x+'.md' for x in ['quick-veo','pro-veo','image-keyframe','image-to-video','storyboard']]
REQUIRED += ['examples/'+x+'.md' for x in ['classroom','butterfly','cinematic-scene','multi-scene-story']]
REQUIRED += ['tests/test-cases.md','tests/validation-report.md','tests/forward-test.md','tests/validate.py']

def validate(root):
    checks = []
    def check(name, condition):
        checks.append((name, bool(condition)))
    for name in REQUIRED:
        p = root/name
        check('nonempty '+name, p.is_file() and p.stat().st_size > 0)
    text = (root/'SKILL.md').read_text()
    parts = text.split('---',2)
    meta = yaml.safe_load(parts[1]) if len(parts)==3 and not parts[0].strip() else {}
    check('YAML fields', set(meta)=={'name','description'})
    check('skill name', meta.get('name')=='veo-prompt-pro')
    check('name syntax', bool(re.fullmatch(r'[a-z0-9-]{1,64}',meta.get('name',''))))
    check('trigger description', all(w in meta.get('description','') for w in ['Veo','image-to-video','thoại','sửa']))
    check('concise entrypoint', len(text.splitlines())<150)
    for p in root.rglob('*.md'):
        content=p.read_text()
        check('no TODO '+str(p.relative_to(root)), not re.search(r'\b(TODO|TBD|FIXME)\b',content))
        for link in re.findall(r'\]\(([^)]+)\)',content):
            if not re.match(r'https?://|#',link):
                check('link '+link,(p.parent/link.split('#')[0]).is_file())
    ui=yaml.safe_load((root/'agents/openai.yaml').read_text())['interface']
    check('UI invocation', '$veo-prompt-pro' in ui['default_prompt'])
    check('license withheld', not (root/'LICENSE').exists())
    story=(root/'examples/multi-scene-story.md').read_text()
    check('expanded character repeated',story.count('An, cô gái Việt Nam trưởng thành, khuôn mặt trái xoan, tóc đen ngang vai, áo khoác vàng trơn, quần xanh đậm, ba lô nâu.')==3)
    check('story right hand', story.count('tay phải')>=6)
    for name,ok in checks:
        print(('PASS ' if ok else 'FAIL ')+name)
    print(f'{sum(ok for _,ok in checks)}/{len(checks)} structural assertions passed; video NOT RUN')
    return all(ok for _,ok in checks)

if __name__=='__main__':
    raise SystemExit(0 if validate(ROOT) else 1)
