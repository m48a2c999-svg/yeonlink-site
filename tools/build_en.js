// index.html(한국어) → en/index.html(영어 정적 페이지). 사용법: node tools/build_en.js
// 페이지에 들어 있는 번역 사전(T)을 그대로 적용해 굳힌 뒤, 주소·메타·구조화 데이터를 영어용으로 바꾼다.
const { chromium } = require('playwright'); const fs=require('fs'), path=require('path');
(async()=>{
  const root=path.resolve(__dirname,'..'); let src=fs.readFileSync(path.join(root,'index.html'),'utf8');
  src=src.replace('<html lang="ko">','<html lang="en" data-page-lang="en">');
  const tmp=path.join(root,'_en_build.html'); fs.writeFileSync(tmp,src);
  const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1280,height:900}});
  await p.route('**/*',r=>{const u=r.request().url(); if(u.startsWith('file:'))r.continue(); else r.abort()});   // 외부 스크립트 없이(애니메이션이 구워지지 않게)
  await p.goto('file://'+tmp); await p.waitForTimeout(800);
  let html=await p.evaluate(()=>{
    document.getElementById('bar')&&document.getElementById('bar').classList.remove('scrolled');
    ['trackA','trackB'].forEach(i=>{const e=document.getElementById(i); if(e)e.innerHTML=''});      // 다시 그려지는 부분은 비워 둔다
    const c=document.getElementById('copied'); if(c)c.textContent='';
    const n=document.querySelector('.card .num'); if(n&&/^19/.test(n.textContent))n.innerHTML='18<small>+</small>';
    return '<!doctype html>\n'+document.documentElement.outerHTML;
  });
  await b.close(); fs.unlinkSync(tmp);
  const rep=(a,b)=>{ if(!html.includes(a)) throw new Error('찾지 못함: '+a.slice(0,60)); html=html.split(a).join(b); };
  // 메타
  html=html.replace(/<title>[^<]*<\/title>/,'<title>Yeonlink · Answers first. The dating app with one question a day</title>');
  html=html.replace(/<meta name="description" content="[^"]*">/,'<meta name="description" content="Answers before photos. Answer one question a day and read what people near you said. Yeonlink is a location-based dating app for adults 18+ (19+ in Korea).">');
  html=html.replace(/<meta property="og:title" content="[^"]*">/,'<meta property="og:title" content="Yeonlink — Words first. Feel closer.">');
  html=html.replace(/<meta property="og:description" content="[^"]*">/,'<meta property="og:description" content="One question a day, answers from people nearby, and a conversation that starts when you both connect.">');
  html=html.replace(/<meta name="keywords" content="[^"]*">/,'<meta name="keywords" content="Yeonlink, dating app, question of the day, meet people nearby, conversation first">');
  rep('<link rel="canonical" href="https://yeonlink.com/">','<link rel="canonical" href="https://yeonlink.com/en/">');
  rep('<meta property="og:url" content="https://yeonlink.com/">','<meta property="og:url" content="https://yeonlink.com/en/">');
  rep('<meta property="og:locale" content="ko_KR">','<meta property="og:locale" content="en_US">');
  rep('<meta property="og:site_name" content="연링크 Yeonlink">','<meta property="og:site_name" content="Yeonlink">');
  // 주소: 한 단계 아래 폴더이므로
  html=html.replace(/(src|href)="img\//g,'$1="../img/');
  html=html.replace(/href="privacy\.html"/g,'href="../en.html#privacy"').replace(/href="terms\.html"/g,'href="../en.html#terms"').replace(/href="location\.html"/g,'href="../en.html#location"');
  html=html.replace(/href="(licenses|child-safety|delete-account)\.html"/g,(m,n)=>'href="'+(n==='licenses'?'../licenses.html':'/en/'+n+'/')+'"').replace(/href="safety-policy\.html"/g,'href="../safety-policy.html"');
  // 화면 사진 설명·접근성 이름
  const ALT={'오늘의 질문에 답을 쓰는 앱 화면':'App screen for answering today\'s question','근처 사람들이 거리 구간으로 표시된 앱 화면':'App screen showing people nearby by distance band','받은 고리 목록 앱 화면':'App screen listing links you received','두 사람의 고리가 이어진 앱 화면':'App screen where two people have connected','대화 화면과 사진 공개 요청':'Chat screen with a photo-sharing request','사이트':'Site','바닥글':'Footer'};
  for(const k in ALT) html=html.split('"'+k+'"').join('"'+ALT[k]+'"');
  const TXT={'>나<':'>Me<','>민<':'>M<','>서<':'>S<','>정책<':'>Policies<','>블로그<':'>Blog<',
    '>엘모컴퍼니(ELMO COMPANY)<':'>ELMO COMPANY<','>대표 조승완<':'>Representative: Seungwan Cho<','>사업자등록번호 108-18-93619<':'>Business registration no. 108-18-93619<',
    '>위치기반서비스사업 신고 제1985호<':'>Location-based service registration no. 1985<','>통신판매업 신고 제2026-서울동작-1363호<':'>Mail-order business registration no. 2026-Seoul Dongjak-1363<',
    '>서울특별시 동작구 상도로 410, 2층<':'>2F, 410 Sangdo-ro, Dongjak-gu, Seoul 07075, Republic of Korea<','>02-3482-2701<':'>+82-2-3482-2701<',
    '"연링크 Yeonlink 처음으로"':'"Yeonlink home"','"정책"':'"Policies"','"오늘 남겨진 답변 예시"':'"Examples of answers left today"',
    '"내 위치를 1km 칸으로 흐리게 표시하고 주변 사람을 거리 구간으로 보여주는 그림"':'"Illustration: your location blurred to a 1 km cell, with people nearby shown by distance band"'};
  for(const k in TXT) html=html.split(k).join(TXT[k]);
  // 구조화 데이터: 화면의 FAQ 를 그대로 영어로
  const faq=[...html.matchAll(/<details[^>]*><summary[^>]*>([\s\S]*?)<\/summary><p[^>]*>([\s\S]*?)<\/p><\/details>/g)].map(m=>({'@type':'Question',name:m[1].replace(/<[^>]+>/g,'').trim(),acceptedAnswer:{'@type':'Answer',text:m[2].replace(/<[^>]+>/g,'').trim()}}));
  if(faq.length<5) throw new Error('FAQ 를 찾지 못함');
  html=html.replace(/<script type="application\/ld\+json">\{"@context":"https:\/\/schema\.org","@type":"FAQPage"[\s\S]*?<\/script>/,'<script type="application/ld+json">'+JSON.stringify({'@context':'https://schema.org','@type':'FAQPage',mainEntity:faq})+'</script>');
  html=html.replace(/<script type="application\/ld\+json">\{"@context":"https:\/\/schema\.org","@type":"MobileApplication"[\s\S]*?<\/script>/,'<script type="application/ld+json">'+JSON.stringify({'@context':'https://schema.org','@type':'MobileApplication',name:'Yeonlink',alternateName:['연링크','Yeonlink'],operatingSystem:'iOS',applicationCategory:'SocialNetworkingApplication',description:'Answers before photos. One question a day, answers from people near you, and conversations that start when you both connect.',url:'https://yeonlink.com/en/',publisher:{'@type':'Organization',name:'ELMO COMPANY'}})+'</script>');
  fs.mkdirSync(path.join(root,'en'),{recursive:true}); fs.writeFileSync(path.join(root,'en','index.html'),html);
  // 남은 한글 보고 (번역 사전의 data-ko 원문, 스크립트 안 사전은 제외)
  const vis=html.replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>/g,'').replace(/ data-ko="[^"]*"/g,'');
  const left=[...new Set((vis.match(/[^<>"]*[가-힣][^<>"]*/g)||[]).map(x=>x.trim()))];
  console.log('en/index.html', html.length, '바이트 · 남은 한글', left.length, '종'); left.forEach(x=>console.log('  ·',x.slice(0,100)));
})();
