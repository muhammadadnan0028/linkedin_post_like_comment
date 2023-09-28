import requests
from bs4 import BeautifulSoup
import json

url = "https://www.linkedin.com/posts/10pearls-pakistan_10pearls-10pearlsdreamwheels-ugcPost-7107981514516103170-p2vx?utm_source=share&utm_medium=member_desktop"

querystring = {
    "utm_source": "share",
    "utm_medium": "member_desktop"
}

headers = {
    "host": "www.linkedin.com",
    
    "connection": "keep-alive",
    "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cookie": "lang=v=2&lang=en-us; bcookie=\"v=2&3d2e865d-d747-469f-8c58-2e29dc584b03\"; bscookie=\"v=1&20230927074725c9f56aba-9bbf-42cf-8d12-cdaaeaf85edbAQHYiWR3NYLxkzSVzspr66_bGlezdUcy\"; li_rm=AQE16H5DJZZt1QAAAYrVpU903dS0byyAaC-DhTTXDGp5picPctVfVxBy3KsLIChlbRyCItI4CC3Tj7CvnZtf0d5b_hLBPruCfgCmWJ3dTIx2lnOlLW5QM3Ip; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19628%7CMCMID%7C59083114968878770061752044298780067070%7CMCAAMLH-1696406300%7C3%7CMCAAMB-1696406300%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1695808700s%7CNONE%7CvVersion%7C5.1.1; aam_uuid=58506390681593646771774326158204745525; _gcl_au=1.1.1584096380.1695801537; g_state={\"i_l\":0}; li_at=AQEDAUUL1ckCiXHWAAABitWmi6kAAAGK-bMPqVYAkcDsapT74Jgbzz6k2e2xHRAv2GSULC1y28qsdd1OQ-Us9LvB2bPnbOAo33cExhpuF2PzmvlgXYD9J6YpAD9YJptKARDu0Zu6-Xbq_8rHL_FAsaZC; liap=true; JSESSIONID=\"ajax:2543190964918171007\"; timezone=Asia/Karachi; li_theme=light; li_theme_set=app; li_sugr=a840ba66-03ac-4074-9225-d3ff1b98ff7e; UserMatchHistory=AQIvPO8r12FHwAAAAYrVpqmvZ2nK5-tyAfJDr0FwNcFaOeWGMBUSegYUYGTAbEHkbFy45UJKhjWu2wWs52KIUkIIehPaAg9iqz4Jq5bh2C6n90e_f5tRIakQeMZ1CjPqU0SvF5rTQ3D0iuAN5qxDeROztA72NjJpXS6juNWFDtCRrPhOPlyBYoN9XGQ_xwcj_HsbQjoVddXnixwPwsTTaRC6KNvF2hpXOO_5u3a2F62NmVKwhA7YRWeoD86GrAaE6-i1bO3A4xEZKJNH12yL6IwH-GPSYPuRKQYAaCHm5YTpsF8BDl_s6UvRzZKXg4-IqYoPPsKn9xb-dBpXUtU2Tl-GutPNlt4; AnalyticsSyncHistory=AQIFiXwul8WppQAAAYrVpqmvlafOyoE9AOwyWKeKRwB6gIHXU3GeQeefuaogzcxffSfYGOGeBaAagDJamHS7eQ; _guid=6539a5fa-47b1-452d-9821-b10cd33d1742; lms_ads=AQF7GiEtR3J_vgAAAYrVpq6qNovm405H3ulbIdL9k0A4mmmFfSWKVDUE9tjCsXSXOpr6beR4nI79kI57xjUr8A3Y7wRbEWPD; lms_analytics=AQF7GiEtR3J_vgAAAYrVpq6qNovm405H3ulbIdL9k0A4mmmFfSWKVDUE9tjCsXSXOpr6beR4nI79kI57xjUr8A3Y7wRbEWPD; lidc=\"b=VB29:s=V:r=V:a=V:p=V:g=7219:u=5:x=1:i=1695801586:t=1695887976:v=2:sig=AQHIlfMeIY9KrT6K_p4IWkhw4HPOVach\""
}

response = requests.get(url, headers=headers, params=querystring)
soup = BeautifulSoup(response.text, "html.parser")
codes = soup.findAll('code')

likes_comments = []
comments = [] # {'USER': , COMMENT: }
for code in codes:
    try:
        jsonString = code.get_text().strip()
        data = json.loads(jsonString)

        included = data.get("included", [])

        for item in included: 
            numLikes = item.get("numLikes", None)
            numComments = item.get("numComments", None)
            if numLikes is not None and numComments is not None:
                if numComments > 2 or numLikes > 2:
                    likes_comments.append((numLikes, numComments))
    except:
        pass

    count=0
    for item in included:
        if "commenterForDashConversion" in item:
            count+=1
            user_name = item["commenterForDashConversion"].get("title", None)
            user_url = item["commenterForDashConversion"].get("navigationUrl", None)
            comment_text = item["commentV2"].get("text", None)
            if comment_text is not None:
                comments.append({
                    'user': user_url,
                    'name': user_name['text'],
                    'text': comment_text

                })

# Sort the list in descending order based on Likes
likes_comments.sort(reverse=True, key=lambda x: x[0])

# Print the first value
if likes_comments:
    first_likes, first_comments = likes_comments[0]
    print("Total Likes:", first_likes)
    print("Total Comments:", first_comments)
else:
    print("No valid data found.")
 
print(comments)