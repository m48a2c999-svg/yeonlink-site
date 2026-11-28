# -*- coding: utf-8 -*-
"""2026-11-28 전수 점검 반영 — index.html 의 사실과 다른 표시 정정. 한 번만 돌린다."""
import io, re, json
p='index.html'; s=io.open(p,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:50],s.count(a)); s=s.replace(a,b)

# 1) 플러스 카드
rep('<span class="tag">Plus · 준비 중</span>','<span class="tag">Plus</span>')
rep('<p class="amt">9,900<small>원 / 월</small></p>',
    '<ul class="prices"><li><strong>1주</strong><span>3,000원</span></li><li><b>1개월</b><span>9,900원</span></li><li><b>3개월</b><span>24,900원</span></li><li><b>6개월</b><span>39,900원</span></li></ul>')
OLD_FINE='1주 3,000원 · 3개월 24,900원 · 6개월 39,900원. 첫 버전은 모든 기능을 무료로 열어 두고, 플러스는 다음 업데이트에서 시작해요.'
NEW_FINE='지금 App Store에서 구독할 수 있어요. 위 금액이 기간마다 실제로 결제되는 금액이고, 끝나기 24시간 전까지 해지하지 않으면 자동으로 갱신돼요. 답변, 하루 고리 3개, 대화, 신고·차단은 계속 무료예요.'
rep('<p class="fine">'+OLD_FINE+'</p>','<p class="fine">'+NEW_FINE+'</p>')
rep('.plan .amt small{font-size:.32em;','.plan .prices{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:10px 18px}\n.plan .prices li{display:flex;justify-content:space-between;align-items:baseline;gap:10px;font-size:clamp(18px,2vw,22px);font-weight:700;letter-spacing:-.03em;border-bottom:1px solid rgba(255,255,255,.14);padding-bottom:8px}\n.plan .prices li b{font-weight:600;opacity:.75}\n.plan .amt small{font-size:.32em;')

# 2) 가입 대상 (FAQ + JSON-LD)
OLD_WHO='만 19세 이상이면 이메일로 가입할 수 있어요. 지금은 대한민국에서만 이용할 수 있어요.'
NEW_WHO='한국에서는 만 19세 이상, 그 밖의 나라에서는 만 18세 이상이면 가입할 수 있어요. 지금은 iPhone에서 이용할 수 있고, Android는 준비 중이에요.'
rep(OLD_WHO,NEW_WHO,3)

# 3) 언어 선택기: 번역이 끝나지 않은 일본어·베트남어는 내린다. 영어는 /en/ 정적 페이지.
rep('<option value="ja">日本語</option><option value="vi">Tiếng Việt</option>','')
rep("    if (LANGS.indexOf(l)<0) l='ko';","    if (l!=='ko'&&l!=='en') l='ko';")
rep("""    applyLang(saved || (LANGS.indexOf(nav)>=0 ? nav : 'ko'), false);
    document.getElementById('lang').addEventListener('change', function(e){ applyLang(e.target.value, true); });""",
"""    var PAGE=document.documentElement.getAttribute('data-page-lang')||'ko';
    applyLang(PAGE, false);
    document.getElementById('lang').addEventListener('change', function(e){ var v=e.target.value; if(v===PAGE)return; try{ localStorage.setItem('yl_lang', v); }catch(_){} location.href = v==='en' ? '/en/' : '/'; });""")
rep('<link rel="canonical" href="https://yeonlink.com/">','<link rel="canonical" href="https://yeonlink.com/">\n<link rel="alternate" hreflang="ko" href="https://yeonlink.com/">\n<link rel="alternate" hreflang="en" href="https://yeonlink.com/en/">\n<link rel="alternate" hreflang="x-default" href="https://yeonlink.com/">')

# 4) 영문 문구 (T 사전: [영어, 일본어, 베트남어] — 뒤 두 칸은 쓰지 않지만 자리만 맞춘다)
m=re.search(r'var T=(\{.*?\});\n',s,re.S); T=json.loads(m.group(1))
def setT(k,en): T[k]=[en,en,en]
T.pop('Plus · 준비 중',None); T.pop(OLD_FINE,None); T.pop(OLD_WHO,None)
setT(NEW_FINE,"Available now on the App Store. The amounts above are what you are actually charged each period, and the subscription renews automatically unless cancelled at least 24 hours before it ends. Answers, three links a day, conversations, reporting and blocking stay free.")
setT(NEW_WHO,"Anyone 18 or older can sign up (19 or older in Korea). It's available on iPhone now; Android is coming.")
setT('1주','1 week'); setT('1개월','1 month'); setT('3개월','3 months'); setT('6개월','6 months')
setT('3,000원','₩3,000'); setT('9,900원','₩9,900'); setT('24,900원','₩24,900'); setT('39,900원','₩39,900')
setT('생년월일로 만 19세 미만은 가입할 수 없어요.',"Anyone under 18 (under 19 in Korea) can't sign up.")
setT('© 2026 ELMO COMPANY. 연링크는 만 19세 이상만 이용할 수 있어요.','© 2026 ELMO COMPANY. Yeonlink is for adults aged 18 and over (19 and over in Korea).')
setT('개인정보처리방침','Privacy Policy'); setT('이용약관','Terms of Service'); setT('위치기반서비스 약관','Location Terms')
s=s[:m.start(1)]+json.dumps(T,ensure_ascii=False)+s[m.end(1):]
io.open(p,'w',encoding='utf-8').write(s)
print('index.html 정정 완료, T', len(T))
