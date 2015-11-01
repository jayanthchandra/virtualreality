# import urllib
# input_file = open('links.txt','r')
# for line in input_file:
#     URL= line
#     IMAGE = URL.rsplit('/',1)[1]
#     urllib.urlretrieve(URL, IMAGE)
import urllib2

def get_image(url, image_save_name):
    try:
        image = urllib2.urlopen(url).read()
        image_save_name.write(image)
        image_save_name.close()
        # with open(image_save_name + '.' + url.split('.')[-1], 'wb') as image_file:
        #     image_file.write(image)
        #     image_file.close()
    except Exception as e:
        print (e)

count=0
input_file = open('links.txt','r')
for line in input_file:

    URL= line
    count+=1
    filename="file_" + str(count)
    get_image(URL, filename)
