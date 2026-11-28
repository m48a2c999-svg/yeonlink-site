# -*- coding: utf-8 -*-
"""영문 정적 페이지 3개: safety-policy.html, en/child-safety/, en/delete-account/"""
import io, os, re
base=io.open('child-safety.html',encoding='utf-8').read()
style=re.search(r'<style>[\s\S]*?</style>',base).group(0).replace('word-break:keep-all;','')
def page(path,title,desc,body,canon,depth,alts=''):
    up='../'*depth
    html=('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
      '<link rel="icon" type="image/png" href="%simg/favicon.png"><meta name="theme-color" content="#F3F1EE">\n<title>%s</title>\n<meta name="description" content="%s">\n'
      '<link rel="canonical" href="%s">\n%s<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&display=swap">\n%s</head><body><div class="wrap">\n%s\n</div></body></html>\n') % (up,title,desc,canon,alts,style.replace('"Noto Sans KR"','Inter,"Noto Sans KR"'),body)
    d=os.path.dirname(path)
    if d: os.makedirs(d,exist_ok=True)
    io.open(path,'w',encoding='utf-8').write(html)

OP='ELMO COMPANY · Representative: Seungwan Cho · Business registration no. 108-18-93619 · 2F, 410 Sangdo-ro, Dongjak-gu, Seoul 07075, Republic of Korea · +82-2-3482-2701 · <a href="mailto:help@yeonlink.com">help@yeonlink.com</a>'

# ── 안전 정책 (콜로라도 C.R.S. 6-1-731.5 (2)(a)~(j)) ──
page('safety-policy.html','Safety Policy · Yeonlink','Yeonlink safety policy: prohibited conduct, background screening, identity and age checks, suspensions and appeals, reporting, and safety resources.',
'''<p class="sub"><a href="/en/">← Yeonlink home</a> · <a href="#ko">한국어 요약</a></p>
<h1>Safety Policy</h1>
<p class="sub">Yeonlink app · Operated by ELMO COMPANY · Effective 28 November 2026</p>
<p>This policy applies to every Yeonlink member. It is also the safety policy required for members in Colorado.</p>

<h2>1. Prohibited content and conduct</h2>
<ul>
<li>Threatening, harassing, stalking or intimidating anyone, or encouraging violence or self-harm</li>
<li>Any sexual conduct with another person without that person's consent, and any attempt to arrange it</li>
<li>Sexual content involving, or sexual approaches to, anyone under 18 (see our <a href="/en/child-safety/">child safety standards</a>)</li>
<li>Sharing or threatening to share intimate images without consent; sextortion; trafficking or prostitution</li>
<li>Using someone else's photos or identity, or misstating your age</li>
<li>Asking members for money, promoting investments or gambling, or any other scam</li>
<li>Hate speech, and sexual or violent content in profiles, answers, notes or messages</li>
<li>Recording, screenshotting or sharing conversations or photos without the other person's agreement</li>
</ul>

<h2>2. Criminal background screening</h2>
<p><b>Yeonlink does not conduct criminal background screening on any member, at sign-up or afterwards.</b> Because we do not screen, we do not exclude members on the basis of a criminal conviction of any type unless it comes to our attention through a report or a request from law enforcement, in which case we review the account under section 4.</p>

<h2>3. Identity and age</h2>
<p><b>Yeonlink does not verify a member's identity.</b> Members state their date of birth when they sign up; the app and our servers refuse anyone under 18 (under 19 in the Republic of Korea). We do not check identity documents. In the Republic of Korea we may additionally require mobile-carrier identity verification. An account found to belong to a minor is closed.</p>

<h2>4. Suspending and barring members</h2>
<ul>
<li>We review every report within 24 hours. Reports about the safety of a child or about violence are handled first.</li>
<li>Depending on seriousness we issue a warning, suspend the account for a period, or bar the member permanently. Sexual misconduct, threats, content sexualising minors and scams lead to a permanent bar.</li>
<li>A member reported by several different members is hidden from others automatically until we finish the review.</li>
<li>When you report someone, they are blocked from you immediately and are not told who reported them.</li>
</ul>

<h2>5. Appeals</h2>
<p>A member who has been suspended or barred may appeal by writing to help@yeonlink.com from the email address on the account within 30 days, explaining why the decision was wrong. We review the appeal and reply within 14 days. A bar for conduct involving minors is not reversed unless the report is shown to be mistaken.</p>

<h2>6. Notice to other members</h2>
<p>Yeonlink does not currently notify members who were in contact with a reported or barred member. When a member is barred, their answers, links and conversations disappear from other members' screens. If law enforcement asks us to help contact members who may have been affected by a crime, we cooperate as the law allows.</p>

<h2>7. How to report</h2>
<ul>
<li><b>In the app:</b> open the menu at the top right of a profile or conversation, choose Report, and pick a reason. You can add a note.</li>
<li><b>By email:</b> help@yeonlink.com. You do not need an account to write to us.</li>
<li>If you are in immediate danger, call your local emergency number first (911 in the United States).</li>
</ul>
<p><b>Report honestly.</b> Do not make a report that you know to be false, or that is made out of malice or bias against a person's race, religion, sex, sexual orientation, gender identity, disability or other protected characteristic. Abusing the reporting system is itself a violation and may lead to suspension.</p>

<h2>8. Consent</h2>
<p><b>Engaging in sexual conduct with another person without that person's consent is a violation of this policy and is against the law. It may result in criminal and civil liability.</b></p>

<h2>9. Resources</h2>
<p>If you or someone you know has experienced sexual assault, domestic violence, stalking or another crime:</p>
<ul>
<li>Emergency: 911</li>
<li>National Sexual Assault Hotline (RAINN): 1-800-656-4673 · rainn.org</li>
<li>National Domestic Violence Hotline: 1-800-799-7233 · thehotline.org</li>
<li>Colorado Coalition Against Sexual Assault: ccasa.org</li>
<li>Violence Free Colorado: violencefreecolorado.org</li>
<li>Colorado Crisis Services: 1-844-493-8255 · coloradocrisisservices.org</li>
<li>Outside the United States, contact your local emergency number and local victim-support services.</li>
</ul>

<h2>10. Safety measures we take</h2>
<ul>
<li>Photos stay hidden from everyone until two members have exchanged six messages and both agree to share them. The server, not only the app, enforces this.</li>
<li>Your exact location is never stored or shown. It is rounded to about 1 km, and others see only an approximate distance.</li>
<li>Automatic filters screen profiles, answers, notes and messages for sexual and abusive language.</li>
<li>You can block or report any member at any time, turn location off, hide your answers, and delete your account in the app.</li>
<li>Adults only: date of birth is checked at sign-up and under-age accounts are closed.</li>
<li>No advertising and no advertising trackers.</li>
</ul>
<p><b>Dating safely.</b> Keep your surname, address and workplace out of your profile. Never send money to someone you met online. Meet in a public place for the first time, tell someone you trust where you are going, arrange your own transport, and leave if anything feels wrong.</p>

<h2>Contact</h2>
<p>'''+OP+'''</p>

<h2 id="ko">한국어 요약</h2>
<p>연링크는 회원의 범죄경력을 조회하지 않으며 신원을 확인하지 않습니다(대한민국에서는 통신사 본인인증을 추가로 요구할 수 있습니다). 가입할 때 생년월일로 만 18세(대한민국 만 19세) 미만을 막습니다. 신고는 24시간 안에 검토하고 경고·기간 정지·영구 정지 조치를 하며, 조치에 이의가 있으면 30일 안에 help@yeonlink.com으로 알려 주시면 14일 안에 답합니다. 상대의 동의 없는 성적 행위는 이 정책 위반이자 범죄이며 민형사상 책임을 질 수 있습니다. 처음 만날 때는 공공장소에서, 믿을 만한 사람에게 일정을 알리고, 돈을 보내지 마세요.</p>''',
'https://yeonlink.com/safety-policy.html',0)

# ── 아동 안전 (Google Play CSAE 5항목) ──
page('en/child-safety/index.html','Child Safety Standards · Yeonlink','Yeonlink standards against child sexual abuse and exploitation (CSAE): what is prohibited, how to report, what we do, and who to contact.',
'''<p class="sub"><a href="/en/">← Yeonlink home</a> · <a href="/child-safety.html" hreflang="ko">한국어</a></p>
<h1>Child Safety Standards</h1>
<p class="sub">Yeonlink app · Operated by ELMO COMPANY · Effective 16 November 2026 (English page published 28 November 2026)</p>
<p>Yeonlink is a dating app for adults only: 18 and over, and 19 and over in the Republic of Korea. We do not tolerate child sexual abuse and exploitation (CSAE) in any form.</p>

<h2>1. What is prohibited</h2>
<ul>
<li>Uploading, sending, requesting or keeping child sexual abuse material (CSAM)</li>
<li>Any text, photo or conversation that sexualises a minor</li>
<li>Approaching or grooming a minor for a sexual purpose, or asking a minor to meet or to send images</li>
<li>Arranging prostitution involving a minor, sextortion, threats or demands for money</li>
<li>Use of the app by minors. An account opened with a false age is closed as soon as we find it.</li>
</ul>

<h2>2. How we prevent it</h2>
<ul>
<li>Date of birth is checked at sign-up, in the app and again on our servers. Anyone under 18 (under 19 in Korea) cannot join.</li>
<li>Automatic filters screen profiles, answers, notes and messages for sexual language and banned terms.</li>
<li>Photos are shared only after two members have exchanged six messages and both agree.</li>
<li>A member reported by several people is hidden automatically until our review is finished.</li>
</ul>

<h2>3. How to report</h2>
<ul>
<li><b>In the app:</b> on a profile or in a conversation, open the menu at the top right, choose <b>Report</b> and pick a reason. The person is blocked at once and is not told who reported them.</li>
<li><b>By email:</b> <a href="mailto:help@yeonlink.com">help@yeonlink.com</a>. You do not need to be a member.</li>
</ul>
<p>We review reports within 24 hours. Reports about child safety are handled first.</p>

<h2>4. What we do</h2>
<ul>
<li>When a violation is confirmed we remove the content and permanently ban the account.</li>
<li>Where we suspect CSAM or a crime against a minor, we report it to the police or other competent authority as the applicable law requires, and cooperate with the investigation.</li>
<li>We comply with applicable child safety laws, including the Korean Act on the Protection of Children and Youth against Sex Offenses and the Act on Promotion of Information and Communications Network Utilization and Information Protection.</li>
</ul>

<h2>5. Point of contact</h2>
<p>Child safety contact: Seungwan Cho, Chief Executive, ELMO COMPANY · <a href="mailto:help@yeonlink.com">help@yeonlink.com</a> · +82-2-3482-2701</p>''',
'https://yeonlink.com/en/child-safety/',2,'<link rel="alternate" hreflang="ko" href="https://yeonlink.com/child-safety.html">\n<link rel="alternate" hreflang="en" href="https://yeonlink.com/en/child-safety/">\n')

# ── 계정 삭제 ──
page('en/delete-account/index.html','Delete your account and data · Yeonlink','How to delete your Yeonlink account and data, what is deleted immediately, and what is kept for a limited period.',
'''<p class="sub"><a href="/en/">← Yeonlink home</a> · <a href="/delete-account.html" hreflang="ko">한국어</a></p>
<h1>Delete your account and data</h1>
<p class="sub">Yeonlink app · Operated by ELMO COMPANY</p>
<p>You can delete your Yeonlink account and the data in it at any time, free of charge, in either of two ways.</p>

<h2>Option 1. Delete it in the app</h2>
<ol>
<li>Open Yeonlink and tap the <b>Me</b> tab at the bottom.</li>
<li>Under <b>Account</b>, tap <b>Delete account</b>.</li>
<li>Read the notice and confirm. The account is deleted immediately and cannot be restored.</li>
</ol>

<h2>Option 2. Ask by email</h2>
<p>If you cannot use the app, write to <a href="mailto:help@yeonlink.com?subject=Delete%20my%20account">help@yeonlink.com</a> from the email address on your account with the subject "Delete my account". After confirming it is you, we delete the account within 7 days and tell you when it is done.</p>
<p>You can also ask us at the same address to delete only part of your data (a profile photo or a particular answer, for example) while keeping the account. Profile photos and your introduction can be removed or changed directly in the Me tab.</p>

<h2>What is deleted</h2>
<div class="tw"><table>
<tr><th>Data</th><th>What happens</th></tr>
<tr><td>Email address, nickname, date of birth, gender, occupation and other profile details</td><td>Deleted immediately</td></tr>
<tr><td>Profile photos</td><td>Deleted immediately</td></tr>
<tr><td>Your answers to the daily question, links and notes</td><td>Deleted immediately</td></tr>
<tr><td>Conversations</td><td>Deleted immediately</td></tr>
<tr><td>Approximate location (rounded to about 1 km)</td><td>Deleted immediately</td></tr>
</table></div>

<h2>What is kept for a limited period, then deleted</h2>
<p>To comply with the law and to prevent abuse, only the following is kept separately for the period shown and then destroyed.</p>
<div class="tw"><table>
<tr><th>Data</th><th>How long</th></tr>
<tr><td>Records of account restrictions, to prevent abuse</td><td>6 months after you leave</td></tr>
<tr><td>Reports and how they were handled</td><td>1 year after handling is complete</td></tr>
<tr><td>Access logs</td><td>3 months (Korean Protection of Communications Secrets Act)</td></tr>
<tr><td>Contract and payment records, if you subscribed</td><td>5 years (Korean Act on Consumer Protection in Electronic Commerce)</td></tr>
<tr><td>Records confirming the use and provision of location data</td><td>The period set in the Location Services terms</td></tr>
</table></div>

<h2>If you have a subscription</h2>
<p>Deleting your account does not cancel a subscription in the store. Cancel it yourself in the subscription settings of the store you paid through (App Store or Google Play).</p>

<p class="sub">Details are in the <a href="/en.html#privacy">Privacy Policy</a>. Contact: '''+OP+'''</p>''',
'https://yeonlink.com/en/delete-account/',2,'<link rel="alternate" hreflang="ko" href="https://yeonlink.com/delete-account.html">\n<link rel="alternate" hreflang="en" href="https://yeonlink.com/en/delete-account/">\n')
print('pages ok')
