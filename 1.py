import urllib.request
import urllib.parse
import re
import pandas as pd

def get_jdlist(keyword, pattern):
    jdlist = list()
    for x,y in zip(range(1,2*3+2,2),range(0,60*3+1,60)):
        url = 'https://search.jd.com/Search?keyword=%s&psort=3&psort=3&page=%d&s=%d&click=1' % (keyword, x, y)
        data = None
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',\
                   'Cookie': 'shshshfpa=dd4b020b-97d1-b9cc-1ccb-bc19d3876a0c-1584623771; shshshfpb=h%20H2KySmlZ5pp5aeTTHd6lA%3D%3D; __jdu=1585107290326843200549; _pst=jd_521525720271a; pin=jd_521525720271a; _tp=fGuZV6qBatFQJrYCY%2BmkjqQa0pRsTAlhMtGWt3Wx66g%3D; qrsc=3; pinId=cyKCDhYJDi7W-WBsh3hTP7V9-x-f3wj7; TrackID=1E5Wq3rsEujy1HP66C3ZP03XvTKbb4P5ZcTlCiANSNmbvzjCSt0zLWM9OtExSxEdxVAVd63zlLjZhv-x-SNucphcVxwPv6KbMqR7KVjwPWTw; unick=%E5%BC%A6%E6%AD%8C0070; user-key=ac0be319-bb85-41a8-a015-a5465244a764; areaId=17; 3AB9D23F7A4B3C9B=3UVDCVBTBR4OAUF7MYS5IEVN6TH6H572IRHIXXUHGJUNTW42LGOYHVKRBKLNWBELZFZP4KXTDY2I6VXMMWKLKEHJUE; ipLoc-djd=17-1381-50713-52576.905442282; cn=6; ipLocation=%u6e56%u5317; shshshfp=3be8fdd7c6396499f2db6afb8b41f2e1; unpl=V2_ZzNtbRFfQhV0XxEGfxoJBGIFR1URXkNCdA5FUHofVFFjAkFdclRCFnQUR1BnGlwUZwMZX0tcQx1FCEdkfh1eAmUzIlxyVEMlfThGUHIdXARhABpcQFREHHAKRVV6HVkNVzMVbXIMFntwD0AHKxkMBWcAQApKZ0MQdwhBVX4bXw1XAiJdR15EHXEKRVJ%2fKRdrZk4SWUtTQxRzC05VeRpbDGIBEVxDU0YdRQl2Vw%3d%3d; CCC_SE=ADC_UW3lDMbpeC0JSW6AEy6K2mkfI%2fs5kq%2bH6Swu0EACb6CgP8Gp7j9aCV%2bpMzEGe9p4mx14cfTp%2b3WQH86anWjFbTrGgF813Gqic10Y6urfBftYWudweCLqu7d2E9cMj7wgvs0aGdAk8UiXUMD61C%2bTLR%2bBauwuhnYpHMenA7yPu8CYGs97UBIldkT1eZfYq62%2bh2BHSbOI45pc0eSxT4BRUzLkkLzytdL0NFKGD0cc1pi9aFFkuPtdeCH5CK1LeCwHMdMDoArmDT6%2bX5rdhUkWTJqUXMHCkmXjF8j0RddbT0Rah3%2bq%2bTJ9BEwXBKaGKfEEpZQ8i%2b3dDpg5EkDzCaD01zXinuX%2frF6PdMhfBldWm8FYVk28Em0oledBiAktPxjW06jGfjqJYF%2faYBqvcNQI105TP5CpHL2CJEZfeUc1U1VcUKfJTUeh9r1HWIOyavt9jpkn8cRS2GIWtlJ31CXMg7m1kdcEu2xcSxZm3xzBNRmkNbSalr1%2fSnbMlF7Erk6SwZSBxm9ht2x1%2bvjisQrsTb%2ftUZHSb%2fo1TOsW7oEBN%2fI%3d; __jdv=76161171|www.infinitynewtab.com|t_45363_|tuiguang|b9010ffc52d047d9b81f0725079e50b1|1590032299001; __jdc=122270672; rkv=V0300; __jda=122270672.1585107290326843200549.1585107290.1590054427.1590058575.18'}
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)

        list1 = re.findall(pattern, html)
        jdlist.extend(list1)
        print('第%d页爬取成功,共爬取了%d个商品' % ((x+1)/2, len(jdlist)))
    return jdlist

def save_excel(jdlist):
    df = pd.DataFrame(jdlist)
    #df.columns = ['价格', '商品编码', '商品名称', '店铺名称']
    df.to_excel(r'C:\Users\28020\Desktop\%s.xlsx' % word)
    
                   
                   

if __name__ == '__main__':
    while True:
        word = input('输入京东商品名：')
        keyword = urllib.parse.quote(word)
        pattern = (r'<em>￥</em><i>(.*?)</i>.*?'
                   r'<i class_="promo-words" id="J_AD_(\d+?)">(.*?)</i>.*?'
                   r'" title="(.*?)">.*?+</a>')
        save_excel(get_jdlist(keyword,pattern))
                   
