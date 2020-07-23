import ronbbut
import shutil
import requests

def run():
    while True:
        try:
            datax = ronbbut.latest()
            post_id = datax['post_id']
            with open('checkpoint.txt','r') as f:
                data =f.readline()
                f.close()
            if str(post_id) == data:
                pass
            else:
                with open('checkpoint.txt','w') as f:
                    f.write(post_id)
                    f.close()
                if str(datax['image']) == 'None':
                    #actual_text = '😮 '+datax['text'].replace(' ','🍆')+' 💦' [You can modify This]
                    actual_text = datax[text]
                    post =ronbbut.onlytext(text=actual_text)
                    print(post)
                else:
                    response = requests.get(datax['image'], stream=True)
                    with open('img.png', 'wb') as out_file:
                        shutil.copyfileobj(response.raw, out_file)
                    del response
                    #actual_text = '😮 '+datax['text'].replace(' ','🍆')+' 💦'
                    actual_text = datax[text]
                    ronbbut.photowithcaption(text=actual_text)
        except:
            pass

            #print(actual_text)

run()
