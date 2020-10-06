from datetime import date
import re
import os


def createFile(filename, title, dataset, changeLanguage=False):

    tableauCode = ''
    script = ''

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

    </style>"""

    front = f"""<body class="w3-light-grey">
        <div class="w3-content" style="max-width:1400px">
            <header class="w3-container w3-center w3-padding-32">
                <h1><b>{title}</b></h1>
            </header>
            <div class="w3-row">
                <div class="w3-col l12 s12">
    """

    for data in dataset:
        if changeLanguage:
            data['code'] = data['code'].replace(
                "value='zh-Hant'", "value='en'")
        split_point = data['code'].find('<script')
        tableauCode += f"""
                <div class = "w3-card-4 w3-margin w3-white" >
                    <div class = "w3-container" >
                        <h3 > <b > {data['caption']} </b > </h3 >
                    </div >
                    <div class = "w3-container" >
                        <p > {data['text']}
                        </p >
                    </div >
                    {data['code'][:split_point]}
                </div >
        """
        script += f'{data["code"][split_point:]}'

    end = """
                </div>
            </div>
        </div>
    </body>
    """

    html = head + style + front + tableauCode + end + script + '</html>'

    # print(html)

    foldername = f'html/{date.today().strftime("20%y_%m_%d")}'
    if not os.path.exists(foldername):
        os.mkdir(foldername)

    f = open(f'{foldername}/{filename}.html', 'w', encoding='utf-8')
    f.write(html)
    f.close()

    print(f'"{filename}" has been completed!')


    # print(html)
