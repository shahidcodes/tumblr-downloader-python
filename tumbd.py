from urllib import urlopen, urlretrieve


doc = """
#####################################
#        Author: ShahidKhan         #
#       @shahidkh4n on GIT          #
#       @rkh4n  on FB               #
#   For Educational Purpose Only    #
"""

## todos
# some new blogs dont have data-highres attribute 


def getImages(url, tagged=False):
    if tagged:
        pageSourceObject = urlopen(url + "tagged/" + tagged)
    else:
        pageSourceObject = urlopen(url)
    pageSourceText  = pageSourceObject.read()
    # match the image url - Only HighRes
    import re
    images = re.findall(r'data-highres=\"(.*?)\"', pageSourceText)
    return images if (len(images) != 0) else False
    
def save(url, tagged=False):
    blogName = url.replace("http://", "").split('.')[0]
    # create directory to save image
    import os
    curDir = os.getcwd()
    path = os.path.join(curDir, blogName)
    try:
        os.makedirs(path)
    except:
        pass
    # get list of image_url 
    images = getImages(url, tagged)
    
    if images:
        for im in images:
            imName = im.split('/')[4]
            try:
                urlretrieve(im, path +"/"+ imName)
                print "[+] Saved: " ,imName
            except:
                print "[*] Cant Download ", im
    else:
        print "Either Last Page Or Something Else Because No Image Recieved!"
            
if __name__ == "__main__":
    print doc
    cmd = str(raw_input("[+] Blogname Please: "))
    
    tagged = True if str(raw_input("[+] With Tag? ")).lower() == "y" else False
    if tagged:
        # CURRENTY ONLY ONE TAG AT A MOMENT
        # MAY SUPPORT MORE IN FUTURE
        tagged = str(raw_input("[+] Enter Tag: ")) # rewrite tagged variable for simplicity
        
    scmd = cmd.split('.')
    if "tumblr" in scmd:
        # user passes the whole url but lets not trust the user do a lil checking
        if "http://" in scmd[0]:
            blogname = scmd[0][7:]
            url = blogname + + ".tumblr.com"
        elif len(scmd) == 3:
            # form of blog.tumblr.com
            url = scmd[0] + ".tumblr.com"
    else:
        url = cmd + ".tumblr.com"
    # print url, tagged
    url = "http://"+ url + "/"
    save(url, tagged)
