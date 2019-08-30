import requests

def scrape():
    y = 2013
    m = 1

    while True:
        url = f"https://www.elections.virginia.gov/media/Registration-Statistics/{y}/{'{:02}'.format(m)}/Registrant_Count_By_Congressional.csv"
        r = requests.get(url, allow_redirects=True)

        open(f'registration-{y}-{m}.csv', 'wb').write(r.content)

        if y == 2019 and m == 7:
            break
        elif m == 12:
            m = 1
            y += 1
        else: 
            m += 1

try:
    scrape()
except:
    if m == 12:
        m = 1
        y += 1
    else: 
        m += 1
    scrape()