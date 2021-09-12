import random, string
import json
from pathlib import Path


def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)


def json_make(path: Path, obj: dict) -> None:
    ls = None
    with open(path, 'r+') as f:
        ls = f.readlines()
        if ls == []:
            ls.append('[\n')
        if ls[-1] == ']':
            ls[-1] = ','
        ls.insert(len(ls), f'{json.dumps(obj, indent=4 ,ensure_ascii=False)}')
        ls.insert(len(ls), '\n]')

    with open(path, 'w') as f:
        f.writelines(ls)

def select_photo_url():
    lst = ["man.jpg", "man2.jfif", "woman1.jfif", "woman2.jfif"]
    ran = random.randrange(4) # 0～3
    return lst[ran]
    

def main():
    path = 'users.json'
    for i in range(100):
        dict_obj = {
            'uid':randomname(28), 
            'displayname':f'ツギツギ{i+1}',
            'photo_url': select_photo_url()
        }
        json_make(path, dict_obj)


if __name__ == '__main__':
    main()