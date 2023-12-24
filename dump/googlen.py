import requests
from selenium import webdriver
import timeit

start = timeit.default_timer()

def getPlate(imageUrl):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 2,
        }
    )
    web = webdriver.Chrome(options=options)

    web.get('https://lens.google.com/uploadbyurl?hl=en&lr=en&url=' + imageUrl)

    current_url = web.current_url
    web.quit()
    print(current_url)
    stop = timeit.default_timer()

    print('Time: ', stop - start)
    r = requests.get(current_url)

    start0 = "AF_initDataCallback"
    start1 = "UNIFIED_GRID"
    start2 = "text:0"
    start3 = "\",[[[\""

    end = "\"]],\""
    with open('data.html', 'w') as f:
        f.write(r.text)
    sp = r.text.find(start0)
    sp = r.text.find(start1, sp)
    sp = r.text.find(start2, sp)
    sp = r.text.find(start3, sp)
    ep = r.text.find(end, sp)

    return r.text[sp + len(start3):ep].split("\",\"")


# image = "https://i.ibb.co/b7vWY8w/nh-ch-p-m-n-h-nh-2023-12-12-235957.png"
# image = "https://cdn.thuvienphapluat.vn/uploads/tintuc/2023/07/12/bien-so-xe-loai-5-so.jpg"
image = "https://metalbyexample.com/wp-content/uploads/figure-65.png"

print(getPlate(image))

# mark 0 = text:0

# mark 1 =[[[[["
# mark 2 = "en",[[["15A-577.15"]]
#mark 3 = [[[[[[["

# print(r.text.count(find))

# with open('data.html', 'w') as f:
#     f.write(r.text)


#Your statements here

stop = timeit.default_timer()

print('Time: ', stop - start)