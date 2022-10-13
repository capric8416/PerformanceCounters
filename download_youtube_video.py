from ast import arg
import subprocess

from concurrent.futures.process import ProcessPoolExecutor
from multiprocessing import cpu_count


def download(name, index, url):
    url = url.strip()
    if len(url) > 0:
        args = ['proxychains4', 'wget', url, '--output-document', f'{name}{index}.mp4']
        subprocess.run(args=args)


def download_youtube_video(name, urls):
    pool = ProcessPoolExecutor(max_workers= 2 * cpu_count() // 3)
    pool.map(download, [(name, i, u) for i, u in enumerate(urls)])
    

if __name__ == '__main__':
    urls = [
        # 360
        'https://rr3---sn-5hnekn7z.googlevideo.com/videoplayback?expire=1661943964&ei=POwOY8ngHMb1yAWHqIewCQ&ip=194.32.122.47&id=o-ABw45MqwoHklRGqdOaswXzyYYiMwS_5l0wEb3e9DqYut&itag=396&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C308%2C315%2C394%2C395%2C396%2C397%2C398%2C399%2C400%2C401&source=youtube&requiressl=yes&spc=lT-Khrj0bgty_Vp5K1hRoSjyD2nQKlA&vprv=1&mime=video%2Fmp4&ns=b0sCpq_HmYc2bjSTGb0pEEEH&gir=yes&clen=18143338&dur=502.333&lmt=1661028692279379&keepalive=yes&fexp=24001373,24007246,24239128&beids=24239128&c=WEB&rbqsm=fr&txp=5532434&n=R4QBqN6Y4jMBsA&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAKqYRsc7wVXDEwZZsH5_qhh-9CPy_2N5ZWJV-CqGuJtgAiARCGHmFJlHVXOs9Twpv8PGAB7FuJlJH_BX10JPv9rRCg%3D%3D&rm=sn-cpux-8ovs7l,sn-f5fe67e&req_id=14e9b281f405a3ee&cmsv=e&redirect_counter=2&cms_redirect=yes&ipbypass=yes&mh=Wi&mip=104.245.96.193&mm=29&mn=sn-5hnekn7z&ms=rdu&mt=1661922798&mv=m&mvi=3&pl=21&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRgIhAJRG8wohJpzyAMseW-_tANhOxsnuuizUUXxtXOjGi8nLAiEA8FqY5RDe5L0NTtsZDZAH2YC4L0r33y07fUzMgHr5W2E%3D',
        # 480
        'https://rr3---sn-5hnekn7z.googlevideo.com/videoplayback?expire=1661943964&ei=POwOY8ngHMb1yAWHqIewCQ&ip=194.32.122.47&id=o-ABw45MqwoHklRGqdOaswXzyYYiMwS_5l0wEb3e9DqYut&itag=397&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C308%2C315%2C394%2C395%2C396%2C397%2C398%2C399%2C400%2C401&source=youtube&requiressl=yes&spc=lT-Khrj0bgty_Vp5K1hRoSjyD2nQKlA&vprv=1&mime=video%2Fmp4&ns=b0sCpq_HmYc2bjSTGb0pEEEH&gir=yes&clen=33417126&dur=502.333&lmt=1661032528146712&keepalive=yes&fexp=24001373,24007246,24239128&beids=24239128&c=WEB&rbqsm=fr&txp=5532434&n=R4QBqN6Y4jMBsA&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAJ2KLDFX3spIvYeMHTuJpLGHEO0shdcK0qMz07roDFbCAiBFsB-8vwrn1ipe5c0xRBOcQAcze_JeyRSsw1tHO85m_Q%3D%3D&rm=sn-cpux-8ovs7l,sn-f5fe77z&req_id=30ebbcc78389a3ee&cmsv=e&redirect_counter=2&cms_redirect=yes&ipbypass=yes&mh=Wi&mip=104.245.96.193&mm=29&mn=sn-5hnekn7z&ms=rdu&mt=1661922798&mv=m&mvi=3&pl=21&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgdqq9c-4v60TSViRPrWT1hbeQAV2tMGn54E65HL0WIUQCIQDzE70IhgFMisaIweTNkmygVco9-si9z6T12_Wguyymtg%3D%3D',
        # 720
        'https://rr3---sn-5hnekn7z.googlevideo.com/videoplayback?expire=1661943964&ei=POwOY8ngHMb1yAWHqIewCQ&ip=194.32.122.47&id=o-ABw45MqwoHklRGqdOaswXzyYYiMwS_5l0wEb3e9DqYut&itag=398&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C308%2C315%2C394%2C395%2C396%2C397%2C398%2C399%2C400%2C401&source=youtube&requiressl=yes&spc=lT-Khrj0bgty_Vp5K1hRoSjyD2nQKlA&vprv=1&mime=video%2Fmp4&ns=b0sCpq_HmYc2bjSTGb0pEEEH&gir=yes&clen=97589946&dur=502.333&lmt=1661030225217270&keepalive=yes&fexp=24001373,24007246,24239128&beids=24239128&c=WEB&rbqsm=fr&txp=5532434&n=R4QBqN6Y4jMBsA&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhALsGvqJQjmWUCyJLioYZf8b5J1cZ6GCFky4FKq51r9TsAiAgdglCdlLhEYB7KnhC2LtsRb9lTo5_5ddkZrTG-ZHh1Q%3D%3D&rm=sn-cpux-8ovs7l,sn-f5fe77z&req_id=1f49166fc30da3ee&cmsv=e&redirect_counter=2&cms_redirect=yes&ipbypass=yes&mh=Wi&mip=104.245.96.193&mm=29&mn=sn-5hnekn7z&ms=rdu&mt=1661922798&mv=m&mvi=3&pl=21&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRgIhAIyFiIeGo6Zz1teAsIdIB-iO8uEDcb-0vD2DTq_febTxAiEAy8XbxnU1EPRmZMoY5fjz5a-eWnWcXCGOVqHmju2L0dw%3D',
        # 1080
        'https://rr3---sn-5hnekn7z.googlevideo.com/videoplayback?expire=1661943964&ei=POwOY8ngHMb1yAWHqIewCQ&ip=194.32.122.47&id=o-ABw45MqwoHklRGqdOaswXzyYYiMwS_5l0wEb3e9DqYut&itag=399&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C308%2C315%2C394%2C395%2C396%2C397%2C398%2C399%2C400%2C401&source=youtube&requiressl=yes&spc=lT-Khrj0bgty_Vp5K1hRoSjyD2nQKlA&vprv=1&mime=video%2Fmp4&ns=b0sCpq_HmYc2bjSTGb0pEEEH&gir=yes&clen=184129104&dur=502.333&lmt=1661041436263744&keepalive=yes&fexp=24001373,24007246,24239128&beids=24239128&c=WEB&rbqsm=fr&txp=5532434&n=R4QBqN6Y4jMBsA&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMRIi8xCS7bLnC7HyXbB6fs4pXwRBLnGejqSklTRj88GAiB515PCIfXIVF3mpG8RjqXXWrHuq_zyXmG5ZZKnTdySpQ%3D%3D&rm=sn-cpux-8ovs7l,sn-f5fe77z&req_id=a98b3f85475ca3ee&cmsv=e&redirect_counter=2&cms_redirect=yes&ipbypass=yes&mh=Wi&mip=104.245.96.193&mm=29&mn=sn-5hnekn7z&ms=rdu&mt=1661922798&mv=m&mvi=3&pl=21&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRgIhAPNR4NgLNWA8gnbcUu9Fmgkni11B89TmT4rid0i95bDPAiEAm4HL6qZvHQHRBO8lI7ax9pl_9cJWedtWidy33pKFRjc%3D',
        # 1440
        'https://rr3---sn-5hnekn7z.googlevideo.com/videoplayback?expire=1661943964&ei=POwOY8ngHMb1yAWHqIewCQ&ip=194.32.122.47&id=o-ABw45MqwoHklRGqdOaswXzyYYiMwS_5l0wEb3e9DqYut&itag=308&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C308%2C315%2C394%2C395%2C396%2C397%2C398%2C399%2C400%2C401&source=youtube&requiressl=yes&spc=lT-Khrj0bgty_Vp5K1hRoSjyD2nQKlA&vprv=1&mime=video%2Fwebm&ns=b0sCpq_HmYc2bjSTGb0pEEEH&gir=yes&clen=697420824&dur=502.332&lmt=1661030920843386&keepalive=yes&fexp=24001373,24007246,24239128&beids=24239128&c=WEB&rbqsm=fr&txp=5532434&n=R4QBqN6Y4jMBsA&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAL0KbEuzYi4vxRXGJI8Omab73l5EfrT3fwkq4ysjgRtRAiBgmSLsamTa3g5ZcmuIMPlfMyEnCNRE0-ceruxjX6PC_g%3D%3D&rm=sn-cpux-8ovs7l,sn-f5fe77z&req_id=80c999a90e6a3ee&cmsv=e&redirect_counter=2&cms_redirect=yes&ipbypass=yes&mh=Wi&mip=104.245.96.193&mm=29&mn=sn-5hnekn7z&ms=rdu&mt=1661922798&mv=m&mvi=3&pl=21&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRAIgVq2UAnVM3uAtWJxGmlAoKQv2AhZkBoBw7Y2SCOY-hJsCIDU7t-1ZS_yGHtogDgvFlBJERp7yNk_qMGf4FRhTUPIO',
        # 2160
        'https://rr3---sn-5hnekn7z.googlevideo.com/videoplayback?expire=1661943964&ei=POwOY8ngHMb1yAWHqIewCQ&ip=194.32.122.47&id=o-ABw45MqwoHklRGqdOaswXzyYYiMwS_5l0wEb3e9DqYut&itag=315&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C308%2C315%2C394%2C395%2C396%2C397%2C398%2C399%2C400%2C401&source=youtube&requiressl=yes&spc=lT-Khrj0bgty_Vp5K1hRoSjyD2nQKlA&vprv=1&mime=video%2Fwebm&ns=b0sCpq_HmYc2bjSTGb0pEEEH&gir=yes&clen=1509533384&dur=502.332&lmt=1661034977235453&keepalive=yes&fexp=24001373,24007246,24239128&beids=24239128&c=WEB&rbqsm=fr&txp=5532434&n=R4QBqN6Y4jMBsA&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgSEVH0R98LL3seIIpSdUFKLqxgAQKeu9XdNHTmuwDfiACIQDMAoK1-jZs4ElM0VDYKRTkIa8YJufUanMN0wU98p0ACw%3D%3D&rm=sn-cpux-8ovs7l,sn-f5fe77z&req_id=c63625d24c33a3ee&cmsv=e&redirect_counter=2&cms_redirect=yes&ipbypass=yes&mh=Wi&mip=104.245.96.193&mm=29&mn=sn-5hnekn7z&ms=rdu&mt=1661922798&mv=m&mvi=3&pl=21&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRAIgVXAwfDidANuZ07Qo7Q9suw5OwRogArpyAE3v8skr2mACIChyvoSdCR4F0W33rAjXs3nh0s6NHZUgyMSNR7AHPU30',
    ]
    download_youtube_video(name='BlackMythWukong8MinuteExclusiveGameplay', urls=urls)