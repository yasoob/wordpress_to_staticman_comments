import xmltodict
import time
import hashlib
import sys
import os
import traceback
from pprint import pprint
import yaml

if not os.path.exists(os.path.join(os.getcwd(), 'big_data.xml')):
    sys.exit("Please put the big_data.xml file in this folder")

total_count = 0
with open('big_data.xml') as fd:
    cfg = xmltodict.parse(fd.read())

for item in cfg['rss']['channel']['item']:
    foldername = '-'.join(item['link'].split('.com/')[1].split('/'))[:-1]
    try:
        if item.get('wp:comment') == None:
            continue
        for comment in item['wp:comment']:
            if comment['wp:comment_approved'] != '1' or comment['wp:comment_type'] == 'pingback':
                continue
            total_count += 1
            data_dict = {}
            folderpath = os.path.join(os.getcwd(), 'comments', foldername)
            total_count += 1
            if not os.path.exists(folderpath):
                try:
                    os.mkdir(folderpath)
                except Exception as e:
                    print("Error occured")
                    sys.exit()
            try:
                date_time = comment['wp:comment_date_gmt']
                pattern = '%Y-%m-%d %H:%M:%S'
                epoch = int(time.mktime(time.strptime(date_time, pattern)))
                comment_file = "comment-" + str(epoch) + ".yml"
            except:
                continue
            try:
                data_dict['_id'] = comment['wp:comment_id']
            except:
                pass
            try:
                data_dict['name'] = comment['wp:comment_author']
            except:
                pass
            try:
                if comment['wp:comment_parent'] != '0':
                    data_dict['reply_to'] = comment['wp:comment_parent']
            except:
                pass
            try:
                temp_email = comment['wp:comment_author_email']
                temp_email = temp_email.strip()
                temp_email = temp_email.lower()
                data_dict['email'] =  hashlib.md5(temp_email).hexdigest()
            except:
                pass
            try:
                data_dict['comment'] = comment['wp:comment_content']
            except:
                pass
            try:
                data_dict['date'] = comment['wp:comment_date_gmt']
            except:
                pass
            pprint(data_dict)
            with open(os.path.join(folderpath, comment_file), "w") as f:
                yaml.dump(data_dict, f)

    except Exception as e:
        traceback.print_exc() 
        pass

print("Total Count: " + str(total_count))
