import urllib2

def get_image(url, image_save_name):
    try:
        image = urllib2.urlopen(url).read()
        with open(image_save_name + '.' + url.split('.')[-1], 'wb') as image_file:
            image_file.write(image)
            image_file.close()
    except Exception as e:
        print (e)

get_image('http://farm3.staticflickr.com/2277/2046712361_77f514172f_z.jpg', 'image_save_name')
