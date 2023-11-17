import requests, urllib.parse
import time, json, random
from bs4 import BeautifulSoup
from tqdm import tqdm


def appendToFile(path,line):
    try:
        file = open(path,'a')
    except:
        file = open(path,'w')
    file.write(line + '\n')
    file.close()

def get_post_id(url):
    print("[+] Getting post id.. ")
    querystring = {"utm_source": "share","utm_medium": "member_desktop"}
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
    soupString = str(BeautifulSoup(response.text, "html.parser"))
    postid = 'urn:li:ugcPost:' + soupString.split('"threadId":"ugcPost:')[-1].split('",')[0].strip()
    return postid

def get_likers(postUrn):
    open("likers.txt",'w').close()
    appendToFile('likers.txt', "Liker name, Job")
    print("[+] Getting post likers.. ")
    totalLikers = 100
    likerSet = False
    likers = []
    start = 10
    pbar = tqdm(total = totalLikers)
    while len(likers) < totalLikers:
        postUrn = postUrn.replace(':','%3A')  # "urn%3Ali%3AugcPost%3A7107981514516103170"
        url = "https://www.linkedin.com/voyager/api/graphql?variables=(count:10,start:{},threadUrn:{})&&queryId=voyagerSocialDashReactions.fa18066ba15b8cf41b203d2c052b2802".format(start,postUrn)
        headers = {
            "host": "www.linkedin.com",
            "connection": "keep-alive",
            "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
            "x-li-lang": "en_US",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "x-li-page-instance": "urn:li:page:d_flagship3_detail_base;Eu7nyfngRgCKYC4+zSqVJg==",
            "accept": "application/vnd.linkedin.normalized+json+2.1",
            "csrf-token": "ajax:5577073305660591672",
            "x-li-track": "{\"clientVersion\":\"1.13.4015\",\"mpVersion\":\"1.13.4015\",\"osName\":\"web\",\"timezoneOffset\":5,\"timezone\":\"Asia/Karachi\",\"deviceFormFactor\":\"DESKTOP\",\"mpName\":\"voyager-web\",\"displayDensity\":2,\"displayWidth\":3360,\"displayHeight\":2100}",
            "x-restli-protocol-version": "2.0.0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.linkedin.com/posts/10pearls-pakistan_10pearls-10pearlsdreamwheels-activity-7107981515334021120-_m-S/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "cookie": "bcookie=\"v=2&35f27b4e-c359-4385-8002-a2a9561d60d8\"; bscookie=\"v=1&202309270730196b6c0ed9-63d3-40a2-8975-b9c2f060c944AQGNpUnsVNgvTytyxXNNmEG6A6OUBsSe\"; aam_uuid=44932205086079893902899590287116973301; li_rm=AQEyvgBR66VjnwAAAYrVi9q_-q6905uTYfmObAAXcJCCxfKB0Mt2xXhvSUBqIivO9VfFUlwaWYeGw3qVchb410p7dww-9CAojclMS-5aXRkNs-DL3KZKIM3u; _gcl_au=1.1.1092169587.1695799837; liap=true; li_at=AQEDAS9Dq8oEJAFQAAABitWMK0wAAAGK-ZivTFYALt3v64rfzFib98FWcB6g3BSV9UnV8MeD6m_ER1R1Dtf-h_TrHMd98h__4odPzH8qxP_H-iuN8EBQAJ1rCwikGz3am07pAGyeTF_m_B9ZxoImDJ3T; JSESSIONID=\"ajax:5577073305660591672\"; timezone=Asia/Karachi; li_theme=light; li_theme_set=app; li_sugr=3710cd89-22ce-4e5c-820f-418be5f97fa4; AnalyticsSyncHistory=AQLvcWN-ojwQCwAAAYrVjEj915j_fvs2j_ZhuxeF_Mmm83PZ7FZp2yiTepUlQAFmvDMc3spfUWt09sVmqABSMA; _guid=db16d6b8-ffe2-42c8-86b6-912d3deb8423; lms_ads=AQF3LyznlGG51gAAAYrVjFmkxLpJMuQDbNQjeZT_QTtG-Vp7wBHo890-cJGSbzwgndWuomQgukrijDLxzyWEi3KI-2gRvoiy; lms_analytics=AQF3LyznlGG51gAAAYrVjFmkxLpJMuQDbNQjeZT_QTtG-Vp7wBHo890-cJGSbzwgndWuomQgukrijDLxzyWEi3KI-2gRvoiy; lang=v=2&lang=en-us; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19628%7CMCMID%7C45092456352473879732950496831445223230%7CMCAAMLH-1696500866%7C3%7CMCAAMB-1696500866%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1695903266s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C650800699; UserMatchHistory=AQJJv_mDoCkB5wAAAYrbSLNdRBzYQGkfN141DGgtlKMwJqHqfeJz6y-pcu1IJitEauMqjSDRGpa9K-lBAdXrrmDdLw4DVCxCsbOh45snXtNDmvIEynHIgUmcRWyGroKeMF2g5lgMxAacf3tChejsPAxAYY5Er3csiT0f43D7qx03pe6Ttj-D4rSFaKGo2ZK57I9Avv4KSmcnPWMwvrrm-jdLEHCcnSd1y6SN0oGme_5BffFT5kRkM2PH6-ulhvKFIN8KsiJ_5kKyi1CVdANJN-CTuf2_bybSNcaytBFqHtvCd4oHfdnjkElwqya1zFEiW7NmOb0Uh4U7Mev_H0gEhmCOJRL6kHA; lidc=\"b=VB42:s=V:r=V:a=V:p=V:g=4711:u=27:x=1:i=1695896092:t=1695982456:v=2:sig=AQH0Hx81KDqBV26e7mjZgTJMkp9cSw97\""
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        for liker in data.get('included'):
            try:
                liker_name = liker.get('reactorLockup').get('title').get('text')
                liker_job = liker.get('reactorLockup').get('subtitle').get('text')
                likers.append({
                    'name': liker_name,
                    'job': liker_job,
                })
                appendToFile(
                    'likers.txt', 
                    "{}, {}".format(liker_name,liker_job)
                )
                pbar.update(n=1)
            except:
                pass
        start = start + 10

        if not likerSet:
            try:
                totalLikers = data.get('data').get('data').get('socialDashReactionsByReactionType').get('paging').get('total')
                likerSet = True
                pbar.total = totalLikers
                print("** Set total liker to", totalLikers)
            except Exception as e:
                pass
        time.sleep(random.randint(5,15))
    return likers

def get_commenters(postUrn):
    open("commenters.txt",'w').close()
    appendToFile('commenters.txt', "Name, Comment")
    
    print("[+] Getting post Commenters.. ")
    totalCommenters = 100
    CommenterSet = False
    commenters = []
    start = 10
    pbar = tqdm(total = totalCommenters)
    while len(commenters) < totalCommenters:
        if len(commenters) > 5: break
        toEnc = "urn:li:fsd_socialDetail:({},{},urn:li:highlightedReply:-)".format(postUrn,postUrn)
        encoded_string = urllib.parse.quote(toEnc)
        variables = "(count:10,numReplies:1,socialDetailUrn:{},sortOrder:REVERSE_CHRONOLOGICAL,start:2)".format(encoded_string)
        url = "https://www.linkedin.com/voyager/api/graphql?variables={}&&queryId=voyagerSocialDashComments.280c3235b7ae477a5dba3e946606ce99".format(variables)
        headers = {
            "host": "www.linkedin.com",
            "connection": "keep-alive",
            "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
            "x-li-lang": "en_US",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "x-li-page-instance": "urn:li:page:d_flagship3_detail_base;Eu7nyfngRgCKYC4+zSqVJg==",
            "accept": "application/vnd.linkedin.normalized+json+2.1",
            "csrf-token": "ajax:5577073305660591672",
            "x-li-track": "{\"clientVersion\":\"1.13.4015\",\"mpVersion\":\"1.13.4015\",\"osName\":\"web\",\"timezoneOffset\":5,\"timezone\":\"Asia/Karachi\",\"deviceFormFactor\":\"DESKTOP\",\"mpName\":\"voyager-web\",\"displayDensity\":2,\"displayWidth\":3360,\"displayHeight\":2100}",
            "x-restli-protocol-version": "2.0.0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.linkedin.com/posts/idbs_on-demand-webinar-drive-data-integrity-and-activity-7107738965541019648-DmTU?utm_source=share&utm_medium=member_desktop",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "cookie": "bcookie=\"v=2&35f27b4e-c359-4385-8002-a2a9561d60d8\"; bscookie=\"v=1&202309270730196b6c0ed9-63d3-40a2-8975-b9c2f060c944AQGNpUnsVNgvTytyxXNNmEG6A6OUBsSe\"; aam_uuid=44932205086079893902899590287116973301; li_rm=AQEyvgBR66VjnwAAAYrVi9q_-q6905uTYfmObAAXcJCCxfKB0Mt2xXhvSUBqIivO9VfFUlwaWYeGw3qVchb410p7dww-9CAojclMS-5aXRkNs-DL3KZKIM3u; _gcl_au=1.1.1092169587.1695799837; liap=true; li_at=AQEDAS9Dq8oEJAFQAAABitWMK0wAAAGK-ZivTFYALt3v64rfzFib98FWcB6g3BSV9UnV8MeD6m_ER1R1Dtf-h_TrHMd98h__4odPzH8qxP_H-iuN8EBQAJ1rCwikGz3am07pAGyeTF_m_B9ZxoImDJ3T; JSESSIONID=\"ajax:5577073305660591672\"; timezone=Asia/Karachi; li_theme=light; li_theme_set=app; li_sugr=3710cd89-22ce-4e5c-820f-418be5f97fa4; AnalyticsSyncHistory=AQLvcWN-ojwQCwAAAYrVjEj915j_fvs2j_ZhuxeF_Mmm83PZ7FZp2yiTepUlQAFmvDMc3spfUWt09sVmqABSMA; _guid=db16d6b8-ffe2-42c8-86b6-912d3deb8423; lms_ads=AQF3LyznlGG51gAAAYrVjFmkxLpJMuQDbNQjeZT_QTtG-Vp7wBHo890-cJGSbzwgndWuomQgukrijDLxzyWEi3KI-2gRvoiy; lms_analytics=AQF3LyznlGG51gAAAYrVjFmkxLpJMuQDbNQjeZT_QTtG-Vp7wBHo890-cJGSbzwgndWuomQgukrijDLxzyWEi3KI-2gRvoiy; lang=v=2&lang=en-us; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19628%7CMCMID%7C45092456352473879732950496831445223230%7CMCAAMLH-1696500866%7C3%7CMCAAMB-1696500866%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1695903266s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C650800699; UserMatchHistory=AQJJv_mDoCkB5wAAAYrbSLNdRBzYQGkfN141DGgtlKMwJqHqfeJz6y-pcu1IJitEauMqjSDRGpa9K-lBAdXrrmDdLw4DVCxCsbOh45snXtNDmvIEynHIgUmcRWyGroKeMF2g5lgMxAacf3tChejsPAxAYY5Er3csiT0f43D7qx03pe6Ttj-D4rSFaKGo2ZK57I9Avv4KSmcnPWMwvrrm-jdLEHCcnSd1y6SN0oGme_5BffFT5kRkM2PH6-ulhvKFIN8KsiJ_5kKyi1CVdANJN-CTuf2_bybSNcaytBFqHtvCd4oHfdnjkElwqya1zFEiW7NmOb0Uh4U7Mev_H0gEhmCOJRL6kHA; lidc=\"b=VB42:s=V:r=V:a=V:p=V:g=4711:u=27:x=1:i=1695896092:t=1695982456:v=2:sig=AQH0Hx81KDqBV26e7mjZgTJMkp9cSw97\""
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        for commenter in data.get('included'):
            try:
                commenter_text = commenter.get('commentary').get('text')
                commenter_name = commenter.get('commenter').get('title').get('text')
                commenters.append({
                    'name': commenter_name,
                    'comment': commenter_text,
                })
                appendToFile(
                    'commenters.txt', 
                    "{}, {}".format(commenter_name,commenter_text)
                )
                pbar.update(n=1)
            except:
                pass
        start = start + 10

        if not CommenterSet:
            try:
                totalCommenters = data.get('data').get('data').get('socialDashCommentsBySocialDetail').get('paging').get('total')
                CommenterSet = True
                pbar.total = totalCommenters
                print("** Set total Commeters to", totalCommenters)
            except Exception as e:
                pass
        time.sleep(random.randint(5,15))
    return commenters


def main(post_url):
    postId = get_post_id(post_url)
    postId = "urn:li:ugcPost:7107981514516103170"
    likers = get_likers(postId)
    commenters = get_commenters(postId)
    

if __name__ == "__main__":
    print("** starting.... ")
    post_url = "https://www.linkedin.com/posts/idbs_on-demand-webinar-drive-data-integrity-and-activity-7107738965541019648-DmTU?utm_source=share&utm_medium=member_desktop"
    main(post_url)

    print("\n****** DONE ******\n")

    exit(1)
