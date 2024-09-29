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
  "authorization": f"Bearer {api_token}",
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
    "cookie": "lang=en-US; AMCVS_5DB5123F5245B1D20A490D45%40AdobeOrg=1; s_ecid=MCMID%7C83556319646641189680875986861822171402; lms-dtc=eyJUYWciOnsiWFp6M25zdkRUWW92QmU5clhrTEZUb3BQQ1hUQ3NNclVQMGZDTEkzNnBzdz0iOnsiRGV2aWNlVGFnIjoiODM2Y2EyMTYtM2NlNS00YWJlLTllNDMtZDJlMzYxM2U5MDc4IiwiRGF0ZVRpbWUiOiIyMDI0LTA5LTIxVDE3OjMwOjExLjc3NFoifX19; lms-dtag=eyJUYWciOnsiWFp6M25zdkRUWW92QmU5clhrTEZUb3BQQ1hUQ3NNclVQMGZDTEkzNnBzdz0iOnsiRGV2aWNlVGFnIjoiODM2Y2EyMTYtM2NlNS00YWJlLTllNDMtZDJlMzYxM2U5MDc4IiwiRGF0ZVRpbWUiOiIyMDI0LTA5LTIxVDE3OjMwOjExLjc3NFoifX19; pstate=s||LZZCOIOZL||||n|||||; __RequestVerificationToken=_Qcg4YMLFOTH5Dc-t9f5TOa7XDsdPWgLLEeFzSIc-8ZBdi_ZVG05wo4iBoypuHHXYB_DvZD-nEjoJ6s3W-Zl3feEiJk1; optimizelyEndUserId=oeu1726946125420r0.5505164550439636; PIM-SESSION-ID=bFB5BaWsThqd0KfL; dom.referrer=Bing Referred; _mkto_trk=id:916-SSU-236&token:_mch-schwab.com-1726951312149-32978; _gcl_au=1.1.1453995879.1726951312; _rtagid=66ef2fa1c56801178e2abb94; _fbp=fb.1.1726951329653.43931196492388036; _rdt_uuid=1726951329659.e799e8e5-508e-4970-b9b6-53271d527f31; _pin_unauth=dWlkPU9XWTFZMlJtWXpJdFpUTXhNaTAwT1RBeExXSmlabU10TURVME16QTVNbVpqWXpJMg; s_vi=[CS]v1|337797D1558BF964-400016D402FA51DD[CE]; trwv.uid=charlesschwabco-1726951313428-f67388cd%3A1; _uetvid=eea929b0785911efb478670ec47483ec; ak_bmsc=5735E73E64398982FFBBE90D0A1C591A~000000000000000000000000000000~YAAQWA3eF2DJeiuSAQAAG6gJPxnWOHIgPGKBOi7AKeNCaPiaERvaYXTuLkbBoX6kVNNjQKjqaZLf4G+qcuVrfTioBazuy3CjUYj7CRJT5mQP4d+fvT7AnFwtfa4mu6f4kmPgsVjsAcZD96Vnf8xhVlTVE6J5jkgjjU5WNvdP6Vuk0b26Jmb9fFCUhjbLb1xLRumac50PmDudq2QvAilf9COM1aShwwou+QKesMF4FL8D2UZKy1Kk3/GoKTk2fhy9eWDEW2LStYlCeXYurGB0Vj1OwAdQYrywdtT6dh9JwsSVpADH+muAPkCTdS7IidJGyyGjLAGlI0jLjUEloDLx1SH1J9qB7ICksqyqKaeYRbFmMjbaHPCY2FKNIMiVKlXgLNEEf5FEEHYmQQo=; AMCV_5DB5123F5245B1D20A490D45%40AdobeOrg=1585540135%7CMCIDTS%7C19995%7CMCMID%7C83556319646641189680875986861822171402%7CMCAAMLH-1728239253%7C7%7CMCAAMB-1728239253%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1727641653s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; pp2=|PK-86-AS-16-XO-91|XM-09-IB-29-WQ-24|KT-22|LS-09-PK-29-WQ-24|SA-11|n|AB-32|COUK-CM|DOMINTL-CM|CLI-COUK-CM|CLI-DOMINTL-CM|INTL-MSG-CM|INTL-CO-NULL|; utag_previous=page_type:$page_subtype:$page_section:; LSP=655738356|https://client.schwab.com/clientapps/accounts/summary/; pod=1; utag_main=v_id:019215a205340049728a5322a96405075006b06d00d57$_sn:9$_se:2$_ss:0$_st:1727636301235$vapi_domain:schwab.com$ses_id:1727634453035%3Bexp-session$_pn:3%3Bexp-session$_prevpage:%2Fclient_center%2Fclientapps%2Faccounts%2Fsummary%3Bexp-1727638056854; s_pers=%20s_vnum%3D2158939792984%2526vn%253D9%7C2158939792984%3B%20s_invisit%3Dtrue%7C1727636301245%3B%20s_prevCh%3D%252Fprospects%7C1727636301247%3B%20s_depth%3D3%7C1727636301247%3B%20s_prevUrl%3Dhttps%253A%252F%252Fclient.schwab.com%252FAreas%252FAccess%252FLogin%253FLoggedOff%253Dy%7C1727636301248%3B%20s_gpv_pn%3D%252Fprospects%252FAreas%252FAccess%252FLogin%7C1727636301248%3B; s_sess=%20s_hid_persist%3D827fdc883e0a286a3ec0719fdbab7cc1fbc82178798f69d5455fe17bff5e1af2%3B%20s_tp%3D3405%3B%20s_ppv%3D%252Fprospects%252Fpublic%252Fschwab%252Flegal%252Fdata_aggregation_faqs__charles_schwab%252C100%252C27%252C3405%3B%20s_sq%3DMAPPED%253D%252526pid%25253Dhttps%2525253A%2525252F%2525252Fdeveloper.schwab.com%2525252Fdashboard%2525252Fapps%252526oid%25253Dhttps%2525253A%2525252F%2525252Fdeveloper.schwab.com%2525252Fproducts%252526ot%25253DA%3B%20s_linkTracking%3D%3B%20s_cc%3Dtrue%3B; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Sep+29+2024+14%3A28%3A21+GMT-0400+(Eastern+Daylight+Time)&version=202211.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0003%3A1%2CC0004%3A1%2CC0001%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=US%3BGA; OptanonAlertBoxClosed=2024-09-29T18:28:21.280Z; _abck=3F80ED81FCE8CDD1FAAD0C377C75F015~-1~YAAQUg3eF96lpS2SAQAAmrUKPwyBBCEp65t1ucN58iAos3sfAwR4mUAigBw/bgjMtaJiLHRQHE8Hte8c6UqXzA3JvOD1LOb8TiweYjZH+fghCjScQnp3TteU8+zmaEtVB0a3eJKot2EpI5l1JYwqOQJkJAZH8Uc2L5vdHGD2DvfLhavrFCxsxPZfkBZ7kf3/BrYLDVMQ2KOUkSsBCwrluHEDbcytib7p5NvwwHY9GIrCuHMtYYySqBA8YLGOlPi/yD3AbYci4l/xaLjZ5KH5r6QzoAc4F40h8o3It1YIAoUKIbby+P+UfGGkmS0APB8aYFveSCm41ZYjwHBi7cgvcm7DH1guItRLpC5cTeOlIa4qiRdDpG6aWLZT1vay0S3gaC7pzKEF84lEZsd8o+s8eCMymCb09O8oE0aH5ahHcZpTgchlJcrYyu9rEopkM55p10xI7YH8CMRhM8ud5Plr9wVa3ElR+HVc2SzRTXDPx2Xig7mnDOtlGNUREpCp7udV2bRm8JTvSnz1rJuiQsv8+pVsoOLq8kyg70WNs8P5hqfu2en2b2kksCkPIACrX1RS6qd9AHoKnUJOoCWnknHJtA1+RD+CHg==~-1~-1~-1; ASP.NET_SessionId=iaxrdknnkrxifo4b0cxbicw0; MobileWeb=no; NP2=SS_PINN|icwtwwg4fvq2dtj1ogjovyi1|2024-09-29|I|N||||S1A00|1727634519|||||; NS2=||I8vuR-6AAAAMAw8KCwEJAA||Y|||||||||Y|E|||||||||Y|d122||||||N||||||||; SessionInfo=0; SS2=|||N|N||; O2=N|*N*||n|N|N|N|N|N|N|N|; AcctInfo=0*F2|1*N|2*Y|3*|4*%28800%29%20435-4000|5*S1|6*S1A00|7*|8*N|9*|10*N|11*IN|12*N|13*N|14*20230905|15*Y|16*N|17*Y|18*N|19*|20*U|21*|22*Y|23*Y|24*0; CustAccessANCInfo=||||||; CtgyListSave=11*619873795|12*|13*|14*|15*0|16*|17*|18*|; ST=09/29/2024 14:28:40; auth=1F6175BA957AFCF9E42FDBBC4D08D08EF0B58BED36A0088B0147B581131EB17417A0EBA1AC22A3FDA3A84B61FB4F308F28A5715733645C91233E752E1ED05ADB60277BDAEEBD7D1247910360F14E2AFED01D99EAD6561A6B9E585A7A607F5D58EFE9EF8D1C373027883EC9CB81888B54E59A6884CBED1DB8FE7FCD9B927C1276F0A41A7D904732B5919007A318080D3D1895D484B35CBE746F062AE2302F253B323053D29C6F6D0C489045C7C510228CF2F613E8761183AB02B1950799FAE41440549B68F15EFDECFEEC07882099CD0814EB532462CB17EF3D5DFEDD568CD8826246A813ECAFDF476C754DF4F28E9AEAF5067BF1D3099566909666197B93FB72A8DE5CD26A9DB4CF26663975D6AED6BB16DD741EB9BE8608B355A56EE5C6E5E7D801A7C3; CustAccessInfo=ZSSSALAOS1+++IND++YZUSAAALTS1+++IND++YAZOOOLTLS1+++IND++Y0000|655738356|AllAccts; sstate=||client.schwab.com||||0||N|||3||60|Y|d97ef38a-e341-42fe-b98a-8cb6310dac07|; bm_sv=2B4FC19E5F7E9591A37824DF30948A67~YAAQUg3eFxmmpS2SAQAAo7gKPxm+NJldQydW+2pRRz0FATBlM1lViptYLZWvKreZh0zLTdGWnxPXzoqztoCRE8o12jO3XvX+BHPSTe3pTPtPjwfVYwMN5Ymu+6Ke/WDKAmhfd3EMhCCqtcJH4KDwCzydL/vXlNqKJvgsBB57Lp35gQaj1BzJ1qb949UKHIvdYw/Oiz9i4BQQi9nwKXysubfNa5Mbx7lN2pRmZgi4dclWnZFmANbyaCEDo1REDHR7sg==~1; bm_sz=A8FD33AEF63114B944523908CD37D308~YAAQUg3eFxqmpS2SAQAAo7gKPxkjHAkn1xGUss77YMvn6wOh/GNWkAxkUvU84iiYINs4Wu4ef3DfuzVm9dx8ZuJEDwPUfK+3AV6UpMwZfWgqxYVlHmaF6124zVpdo44DYCkIb6SVjYiRchgBSBfNEzO3JhCevhYXsVAfEIgM9waGG+PCQDQ/nvQIkCT4ouGV6RMMFDeM0cyVoVWJjUhC4xMOrN57xdOq7rORQ0ikvZY68Yc9ya9SMjyeQnOWZn2PF7WIdaDqErCoocyMxXLYriWeYb8kXmTUBuOIb/lIU/b6D9yLiajpN5aODNFmFxT52oVyDpTWCAWDGwWMl4w7YBbdCm4fTu3RQzlbr2q77DEQJJ1b+SkRl2BcUl2xAfSAM20obXc//kHXocLngea+Bz3jHBR1YHpRiwmgKinbW7uXBwG4StLFgtTCRjACxdie1pxwpwe89u4gSPOrVqPMMv/H7ezP~3621168~3356997; RT='z=1&dm=schwab.com&si=eb617615-8f0c-4f2e-8df7-698564a12936&ss=m1nwy0yh&sl=3&tt=3oy&bcn=%2F%2F173bf10f.akstat.io%2F'",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}