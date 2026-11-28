# -*- coding: utf-8 -*-
"""2026-11-28 약관·방침 보강 (ko/en 동시). 한 번만 돌린다."""
import io
def edit(path, pairs):
    s=io.open(path,encoding='utf-8').read()
    for a,b in pairs:
        assert s.count(a)==1,(path,a[:50],s.count(a)); s=s.replace(a,b)
    io.open(path,'w',encoding='utf-8').write(s)

# ───── 한국어 (세 파일이 같은 본문을 담고 있다) ─────
KO=[
 ('      <tr><td>Apple Inc.</td><td>앱 배포, 인앱결제 처리(유료 서비스 도입 시), 알림 전송(Apple 푸시 알림 서비스)</td></tr>',
  '      <tr><td>Apple Inc.</td><td>앱 배포, 인앱결제 처리, Apple로 로그인, 알림 전송(Apple 푸시 알림 서비스)</td></tr>\n'
  '      <tr><td>Google LLC</td><td>Google Play를 통한 앱 배포, 인앱결제 처리(Android 결제 도입 시), Google로 로그인, Android 기기 알림 전송(Firebase Cloud Messaging, 해당 기능 도입 시)</td></tr>'),
 ('<td>전송 후 Apple의 보관 정책에 따름. 회사는 알림을 끄거나 탈퇴하면 기기 식별값을 삭제</td></tr>',
  '<td>전송 후 Apple의 보관 정책에 따름. 회사는 알림을 끄거나 탈퇴하면 기기 식별값을 삭제</td></tr>\n'
  '      <tr><td>Google LLC (support.google.com/policies/contact/general_privacy_form)</td><td>미국</td><td>Google로 로그인할 때의 계정 식별값·이메일 주소, Android 알림용 기기 식별값과 알림 제목·문구, Google Play 구매 식별값</td><td>Google로 로그인, Android 기기 알림 전송, 인앱결제 확인</td><td>해당 기능을 쓸 때마다 암호화된 네트워크로 전송</td><td>Google의 보관 정책에 따름. 회사는 탈퇴하면 식별값을 삭제</td></tr>'),
 ('<p>만 19세 이상인 개인만 가입할 수 있으며,', '<p>대한민국에서는 만 19세 이상, 그 밖의 나라에서는 만 18세 이상인 개인만 가입할 수 있으며,'),
 ('  <p>이 약관은 대한민국 법을 따르며, 분쟁은 「민사소송법」상 관할 법원에서 해결합니다.</p>',
  '  <p>이 약관은 대한민국 법을 따르며, 분쟁은 「민사소송법」상 관할 법원에서 해결합니다. 다만 회원이 대한민국 밖에 거주하는 소비자인 경우, 거주하는 나라의 강행규정이 소비자에게 주는 보호는 이 조항으로 배제되지 않습니다.</p>\n'
  '  <p>서비스는 현재 유럽경제지역(EEA)·영국·스위스에 거주하는 분께는 제공하지 않습니다.</p>\n'
  '  <p>회사는 회원의 신원이나 범죄경력을 조회하지 않습니다. 안전하게 만나는 방법과 회사의 조치는 <a href="safety-policy.html">안전 정책(Safety Policy)</a>에, 아동 안전 기준은 <a href="child-safety.html">아동 안전 표준</a>에 있습니다.</p>'),
]
for f in ('terms.html','privacy.html','location.html'): edit(f,KO)

# ───── 영어 ─────
EN=[
 # 표 4행 모두 3칸
 ('<td>10 links a day, see who read your answer, 300-character notes,', '<td rowspan="4">10 links a day, see who read your answer, 300-character notes,'),
 # 복사 알림
 ("msg.textContent='선택했어요. 길게 눌러 복사하세요.'", "msg.textContent='Selected. Press and hold to copy.'"),
 ("msg.textContent='복사했어요'", "msg.textContent='Copied'"),
 # 가입 자격: EEA·영국 미제공, 아동
 ('<p>You must be at least 18 years old, or at least 19 if you are in the Republic of Korea.',
  '<p>You must be at least 18 years old, or at least 19 if you are in the Republic of Korea. The Service is not currently offered to people who live in the European Economic Area, the United Kingdom or Switzerland, and you may not sign up from those places. We do not knowingly collect personal data from anyone under 18 (under 19 in Korea); if we learn that we have, we close the account and delete the data.</p>\n  <p>'),
 # 미국 안전 고지 + 호주
 ('  <h2>6. Reports and restrictions</h2>',
  '  <h2>5A. Safety notice</h2>\n'
  '  <p style="font-size:16px;font-weight:800;line-height:1.6;text-transform:uppercase">Yeonlink does not conduct criminal background checks or identity verification on its members, and does not inquire into the background of its members. You are responsible for your own safety when you communicate with or meet other members.</p>\n'
  '  <p><b>Meeting safely.</b> There is no substitute for acting with caution when you communicate with a stranger who wants to meet you. Do not include your last name, home address, workplace or other identifying details in your profile or first messages. Never send money or financial information to someone you met on the Service, however convincing the reason. Meet for the first time in a public place, tell a friend or family member where you are going and when you expect to be back, arrange your own transport, and leave if you feel uncomfortable. Stop communicating with anyone who pressures you for personal or financial information, and report them to us. Anyone who is able to commit identity theft can also falsify a dating profile.</p>\n'
  '  <p><b>Colorado users: <a href="safety-policy.html">our safety policy</a>.</b> It applies to every member wherever they live.</p>\n'
  '  <p><b>Image-based abuse, grooming and sexual exploitation.</b> You must not share, or threaten to share, an intimate image or video of another person without their consent; you must not try to befriend or persuade anyone under 18 for a sexual purpose; and you must not use the Service for sexual exploitation, sextortion or trafficking of any person. We remove such content, ban the account and cooperate with law enforcement. If you are in Australia you can also report image-based abuse and other serious online harm to the eSafety Commissioner at esafety.gov.au/report.</p>\n\n'
  '  <h2>6. Reports and restrictions</h2>'),
 # 위치약관의 아동 조항
 ('<p>The Service is for adults only, so the provisions on guardians of children aged 8 and under do not apply.</p>',
  '<p>The Service is for adults only (18 and over, 19 and over in Korea). We do not knowingly collect location data from anyone younger, so the provisions on guardians of children aged 8 and under do not apply.</p>'),
 # 개인정보 8조 머리에 미제공 명시
 ('  <p>Our legal basis for handling your data is the performance of our contract',
  '  <p>The Service is not currently offered to people who live in the European Economic Area, the United Kingdom or Switzerland. If you are nevertheless there, the following applies to any data we hold about you.</p>\n  <p>Our legal basis for handling your data is the performance of our contract'),
]
edit('en.html',EN)
print('약관 보강 완료')
