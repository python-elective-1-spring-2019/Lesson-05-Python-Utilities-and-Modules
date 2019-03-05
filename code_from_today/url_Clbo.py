def open_url():
    try: 
        res = urlopen('https://dr.dk/')
        html = res.read().decode('utf-8')
        file = open('dr.html', 'w')
        file.write(html)

        subprocess.run(['open', 'dr.html'])

    except HTTPError as err:
        print(err)
    except Exception as err:
        print(err)