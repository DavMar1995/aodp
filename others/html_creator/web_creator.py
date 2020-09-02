from convert import getData
from datetime import date
import os


def insertManually():
    filename = input("Enter filename: ")
    title = input("Enter title: ")
    text = input("Enter text: ")
    # text=''
    # title=''
    code = input(f'Please insert the embedded code from Tableau: ')
    return {'filename': filename, 'title': title, 'code': code, 'text': text}


def createFile(data):
    filename = data['filename']
    title = data['title']
    text = data['text']
    code = data['code']

    split_point = code.find('<script ')

    head = f"""<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
        <title>{title}</title>
    </head>"""

    style = """<style>
        body,
        h1,
        h2,
        h3,
        h4,
        h5 {
            font-family: Microsoft JhengHei;
        }
        
        /* #viz1598268207990 {
            text-align: center;
            margin: 0 auto;
        }*/
    </style>"""

    body = f"""<body class="w3-light-grey">
        <div class="w3-content" style="max-width:1400px">
            <header class="w3-container w3-center w3-padding-32">
                <h1><b>{title}</b></h1>
            </header>
            <div class="w3-row">
                <div class="w3-col l12 s12">
                    <div class="w3-card-4 w3-margin w3-white">

                        <div class="w3-container">
                            <h3><b>{title}</b></h3>
                        </div>
                        <div class="w3-container">
                            <p>{text}
                            </p>
                        </div>
                        {code[:split_point]}
                    </div>
                </div>
            </div>
        </div>
    </body>

    {code[split_point:]}

    </html>
    """

    html = head + style + body
    
    foldername = f'html/{date.today().strftime("20%y_%m_%d")}'
    if not os.path.exists(foldername):
        os.mkdir(foldername)
    
    f = open(f'{foldername}/{filename}.html', 'w', encoding='utf-8')
    f.write(html)
    f.close()


if __name__ == '__main__':
    for i in getData():
        print(i['filename'])
        createFile(i)
