import os
from dotenv import load_dotenv

load_dotenv()

api_token = os.environ["TOKEN"]

payload = {"exportType":"Json",
           "includeOptionsInSearch":False,
           "selectedTransactionTypes":["CorporateActions","Trades"],
           "symbol":"","timeFrame":"Last6Months",
           "bookmark":None,"shouldPaginate":True,
           "selectedAccountId":"95333616",
           "sortColumn":"Date",
           "sortDirection":"Descending",
           "accountNickname":"Individual"
           }

headers = {
  "authority": "ausgateway.schwab.com",
  "method": "POST",
  "path": "/api/is.TransactionHistoryWeb/TransactionHistoryInterface/TransactionHistory/brokerage/transactions/export",
  "scheme": "https",
  "accept": "application/json",
  "accept-encoding": "gzip, deflate, br, zstd",
  "accept-language": "en-US,en;q=0.9",
  "authorization": "Bearer I0.b2F1dGgyLmNkYy5zY2h3YWIuY29t.EHtcDtVF-x-Zcpbq6GJnxiyUSY29TwD8Gkuo8A2aryk@",
  "cache-control": "no-cache",
  "content-length": "486",
  "content-type": "application/json",
  "correlatorid": "f863b1aa-16fc-46f3-b2c9-c1e0a6fc2dd5",
  "method": "POST",
  "origin": "https://client.schwab.com",
  "pragma": "no-cache",
  "priority": "u=1, i",
  "referer": "https://client.schwab.com/",
  "schwab-client-appid": "AD00002298",
  "schwab-client-channel": "IO",
  "schwab-client-correlid": "8e7ea1be-72ed-f349-26d1-7fbb1b68cfbb",
  "schwab-env": "PROD",
  "schwab-environment": "PROD",
  "schwab-environment-region": "",
  "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"macOS\"",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-site",
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

auth_headers = {
    "method": "GET",
    "path": "/api/auth/authorize/scope/api",
    "scheme": "https",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "lang=en-US; AMCVS_5DB5123F5245B1D20A490D45%40AdobeOrg=1; s_ecid=MCMID%7C83556319646641189680875986861822171402; lms-dtc=eyJUYWciOnsiWFp6M25zdkRUWW92QmU5clhrTEZUb3BQQ1hUQ3NNclVQMGZDTEkzNnBzdz0iOnsiRGV2aWNlVGFnIjoiODM2Y2EyMTYtM2NlNS00YWJlLTllNDMtZDJlMzYxM2U5MDc4IiwiRGF0ZVRpbWUiOiIyMDI0LTA5LTIxVDE3OjMwOjExLjc3NFoifX19; lms-dtag=eyJUYWciOnsiWFp6M25zdkRUWW92QmU5clhrTEZUb3BQQ1hUQ3NNclVQMGZDTEkzNnBzdz0iOnsiRGV2aWNlVGFnIjoiODM2Y2EyMTYtM2NlNS00YWJlLTllNDMtZDJlMzYxM2U5MDc4IiwiRGF0ZVRpbWUiOiIyMDI0LTA5LTIxVDE3OjMwOjExLjc3NFoifX19; __RequestVerificationToken=_Qcg4YMLFOTH5Dc-t9f5TOa7XDsdPWgLLEeFzSIc-8ZBdi_ZVG05wo4iBoypuHHXYB_DvZD-nEjoJ6s3W-Zl3feEiJk1; optimizelyEndUserId=oeu1726946125420r0.5505164550439636; PIM-SESSION-ID=bFB5BaWsThqd0KfL; dom.referrer=Bing Referred; _mkto_trk=id:916-SSU-236&token:_mch-schwab.com-1726951312149-32978; _gcl_au=1.1.1453995879.1726951312; _rtagid=66ef2fa1c56801178e2abb94; _fbp=fb.1.1726951329653.43931196492388036; _pin_unauth=dWlkPU9XWTFZMlJtWXpJdFpUTXhNaTAwT1RBeExXSmlabU10TURVME16QTVNbVpqWXpJMg; s_vi=[CS]v1|337797D1558BF964-400016D402FA51DD[CE]; trwv.uid=charlesschwabco-1726951313428-f67388cd%3A1; pod=1; NS2=||I4TLof6AAAAHAggFDA0OCA||Y|||||||||Y|E|||||||||Y|d122||||||N||||||||; ak_bmsc=3053A7512538925440C28DF3AA38BA37~000000000000000000000000000000~YAAQxZUqF4zIPDCSAQAAqXoFRBkgpLTdQYlqVfA/+tLZdEYNcHUMbFpzqdnjRLU2ekM4ibtc/9tjgD0I1r8RNsfhUSh3JUsqP4n605RLohTFilfAf+7SwP4bIrnBoGOQ96omdCfaxnRXVVikFzAE3tN3RS0Uvh/Dsox25cPNF89e09ry+9OnGIAqO9CSBQJRxQtOsJ535fF8NH0cQLgs0AS7YeUbhoo5UZNZUUoclkCkS7MNOFqjd76FSXMbhCAvKbtUtwZU6qZ/lBLWj+LVJU+6hrDtkccZOoR+gqh4x3Wk/PUE740DguepQUtbW3cR1mY09i2cPz66e3G5eAsfZIVjK+RvSP5iEeRStrrhTRHIzD4GP6iTIKmNyJ4KNJ0sQk8h8xUjPjK7uw==; pstate=s||LZZCOIOZL||||n|||1727718063178.undefined| |; AMCV_5DB5123F5245B1D20A490D45%40AdobeOrg=1585540135%7CMCIDTS%7C19997%7CMCMID%7C83556319646641189680875986861822171402%7CMCAAMLH-1728322863%7C7%7CMCAAMB-1728322863%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1727725263s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; _gcl_aw=GCL.1727718064.Cj0KCQjwmOm3BhC8ARIsAOSbapUSM5-2e5JaAoiqjhmL0C2BrMR0HeEgWMt2q-wE3bwVCFy09GPLeCsaAmt8EALw_wcB; _gcl_gs=2.1.k1$i1727718062; _rdt_uuid=1726951329659.e799e8e5-508e-4970-b9b6-53271d527f31; _uetsid=2a21b7607f5311ef890e3db62243af85; _uetvid=eea929b0785911efb478670ec47483ec; pp2=|PK-86-AS-16-XO-91|XM-09-IB-30-WQ-24|KT-22|LS-09-PK-30-WQ-24|SA-11|n|AB-32|COUK-CM|DOMINTL-CM|CLI-COUK-CM|CLI-DOMINTL-CM|INTL-MSG-CM|INTL-CO-NULL|; utag_previous=page_type:$page_subtype:$page_section:; utag_main=v_id:019215a205340049728a5322a96405075006b06d00d57$_sn:11$_se:4$_ss:0$_st:1727719932989$vapi_domain:schwab.com$ses_id:1727718063444%3Bexp-session$_pn:5%3Bexp-session$_prevpage:%2Fclient_center%2Fclientapps%2Faccounts%2Fsummary%3Bexp-1727721709902; s_pers=%20s_vnum%3D2158939792984%2526vn%253D11%7C2158939792984%3B%20s_ev74%3D%255B%255B%2527SEM%2527%252C%25271727718063549%2527%255D%255D%7C1885484463549%3B%20s_invisit%3Dtrue%7C1727719933001%3B%20s_prevCh%3D%252Fprospects%7C1727719933002%3B%20s_depth%3D5%7C1727719933002%3B%20s_prevUrl%3Dhttps%253A%252F%252Fclient.schwab.com%252FAreas%252FAccess%252FLogin%7C1727719933003%3B%20s_gpv_pn%3D%252Fprospects%252FAreas%252FAccess%252FLogin%7C1727719933003%3B; s_sess=%20s_hid_persist%3D827fdc883e0a286a3ec0719fdbab7cc1fbc82178798f69d5455fe17bff5e1af2%3B%20s_tp%3D5446%3B%20s_gvo_v49%3Dmixer_component%2528221256-1%2529%3B%20s_ppv%3D%252Fprospects%252Fpublic%252Fschwab%252Fclient_home_new%252C16%252C16%252C875%3B%20s_gvo_v0%3DSEM%3B%20s_sq%3DMAPPED%253D%252526pid%25253Dhttps%2525253A%2525252F%2525252Fdeveloper.schwab.com%2525252Fdashboard%2525252Fapps%252526oid%25253Dhttps%2525253A%2525252F%2525252Fdeveloper.schwab.com%2525252Fproducts%252526ot%25253DA%3B%20s_linkTracking%3D%3B%20s_cc%3Dtrue%3B; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Sep+30+2024+13%3A42%3A13+GMT-0400+(Eastern+Daylight+Time)&version=202211.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0003%3A1%2CC0004%3A1%2CC0001%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=US%3BGA; OptanonAlertBoxClosed=2024-09-30T17:42:13.034Z; _abck=3F80ED81FCE8CDD1FAAD0C377C75F015~-1~YAAQx5UqFzh4izGSAQAAn6MGRAykzK1H7ThoLWopm3EjmHPegmDRZ3k/zYgTzUn4pg/rSIOpBfbnZXrIPnrCSfkWgV7uUwHDJZcAEWZke3k6m9FP3I87aPn+NfMtZJ/ALyWlYe8r2s09dg/fmG9B/DQmd1XtyV5AhmnXgFg/iz6LLr01JmQ2qiepruKEAcbznQhmPwcljGKcJ+if4LGV0flY92hkqiQPySZUM/pi4U0SCklQrumBovHjfps0fEs15NIWd20Tz1jajShjiEP9XBHaa0V5tNvwizOsWlhYzvH25wCK7a8wDK635m7vTHOeLHIP/6ZG/L4960ELB+FhCKBzVwWlkxzAVDGcaEtT5ukxw1eJhq191n/+LNWATY8SklkHifBA+P5jXoDwNEANaFuJPSp1An41VQcCH6MC1hyLKhQSmK+s05UYPVxx8QUcWKAtxc+7ZKxPoq6iD1YADbIwD35jtFveChvZQdTeSwQLvDzyOWfc1peTaFcZv8iw5eLfVXAPxdc2q9iGegAOUXWkVk9aX4jXutckPi3vnU19CN2K~-1~-1~-1; ASP.NET_SessionId=spy52zcni33033fh2of0lvxv; MobileWeb=no; NP2=SS_PINN|icwtwwg4fvq2dtj1ogjovyi1|2024-09-30|I|N||||S1A00|1727718138|||||; SessionInfo=0; SS2=|||N|N||; O2=N|*N*||n|N|N|N|N|N|N|N|; AcctInfo=0*F2|1*N|2*Y|3*|4*%28800%29%20435-4000|5*S1|6*S1A00|7*|8*N|9*|10*N|11*IN|12*N|13*N|14*20230905|15*Y|16*N|17*Y|18*N|19*|20*U|21*|22*Y|23*Y|24*0; CustAccessANCInfo=||||||; CtgyListSave=11*619873795|12*|13*|14*|15*0|16*|17*|18*|; ST=09/30/2024 13:42:19; auth=B55E4F3649397A5E5370B8625478BC7C24B24380D88E159233BF1CC29A9E42E4F097F35AC6D10B1F4C8059555C850FC55EA1ED22ECCC88CD5AEEB9576CB63929FA88BC251F3FB1D946C7AEE516FA19FA833C624F2DEABF7E6739397871ABC5E52FF808082A4EC2E3140655D074E841FAF58255B7752CBB44BAC18876F1D7DCF4EA93AF1A45951B2F01645BF916997AC4B9A008D2E7B69DC79740368D76258529A773D4A1A62E3A8617F5234EA51A651F62E04D2D8866B94D47AD55F59FDDC0CBC76B9ED5B60420AC22F9A9C989A9E646790A229FEE778AA3062A7B6C6185E593DDDECBFBA923283ABB53A3A07EE6D32B9646A5466B6503EC2ED37252D1871B21A760BA0062748583114827454DBBBC7D06D2C1B0E470C4417F225B5FE762D693F899850C; CustAccessInfo=ZSSSALAOS1+++IND++YZUSAAALTS1+++IND++YAZOOOLTLS1+++IND++Y0000|655738356|AllAccts; sstate=||client.schwab.com||||0||N|||3||60|Y|2e5dd20b-a676-445e-8550-1f9cf7211e6e|; bm_sv=AFCFE528B4E120902E4BF2B3BC3A9679~YAAQxZUqF9HfPDCSAQAALacGRBkAY6ewmyLh6xF4KPoVgU49zj8BaTjfe/flNm5mA4xM1P+VCf9bmeMf1RW8MQ843gN+h0WsFYF4zksKTvYco3Xw2ZXZzLCWDWiWsa7SB3Ptv+z+er4jjRDMV2MLJgka8L2aCRRVemMzNwGXrMM/v40AtBmmohJZaTIS1p7qiTMakas4dhO2JxArJ0hC+QpwbYYhUD7IxR4c/API3u0yoIACi5KhmF5Ecy5rHEsISg==~1; bm_sz=F27CBBD937B7B83B1F6673FF953589F6~YAAQxZUqF9LfPDCSAQAALacGRBkwCq6xql1D+HvLicxoOhcpfCDXFANgFqjeg13Sstf175ErcYxTDpp8ZqBOshTftBxln4YKpvcj/b9LJGz9xx+ICHkbnHE84NymTNpsprXUHkkyyx3AxujuxDmLVAC96kXdGKCr2uD8zIW3GiZWk7iw73QFqfU9gLMD5L1XOANFh7tL5cY5hZrOtRocpCQltIn491cjU3Oiv5YEBiDWrjJHbKfQA3BffqaNXk5i3LNTT7FQaYDN/xL/mcLIAv28KFFIav/jYt8pC9DQ+flspaBp66Yir/4+vw2uLaLokQuLBJcPDTub8NM9uEBG89oMs1TDed6YrhLikvDh/5jMU0B+RIPt5dHpg+1WcnBWVuD2O6LWTK28HSRe+HCWeAgzzzNj1aljqNzSv41CI4GNgQc6HaJPA+pxAIYgdrdbsyW5LfD/PuKkIa7nJX0rkO/HDh7sQXrfsX75ci/08A==~4343092~4602168; RT='z=1&dm=schwab.com&si=eb617615-8f0c-4f2e-8df7-698564a12936&ss=m1paq4bt&sl=5&tt=6sx&bcn=%2F%2F173bf106.akstat.io%2F'",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}