from datetime import date
import re
import os


def getFile():
    global files
    # print(f'files: \n{files}')
    for i in files:
        yield i


def getTitle():
    global title
    file_gen = getFile()
    count = 0
    for i in file_gen:
        # print(f'file:\n {i}')
        if count in title:
            t = title[count]
        else:
            t = i[i.find('-')+1:i.find('.txt')]
        count += 1
        yield t


def getFileName():
    title_gen = getTitle()
    for i in title_gen:
        # print(f'title:\n {i}')
        yield i, i.replace(' ', '_')


def getText(id):
    global files
    with open(f'txt/{files[id]}', 'r', encoding="utf-8") as f:
        # print(f.read(), '\n')
        txt = re.split('\n+', f.read())
        p = ''
        for i in txt:
            if i == '':
                continue
            i = f'<p>{i}</p>'
            p += i
        return p


def getData(haveStart=False, start=0, length=0):
    global code
    for i, (title, filename) in enumerate(getFileName()):
        if haveStart:
            if start > i:
                # print(start, i)
                continue
            if start + length <= i:
                # print(start, length, i)
                break
        yield {
            'title': title,
            'filename': filename,
            'text': getText(i),
            'code': code[i],
        }


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

    # Paste the Tableau code into it as a str directly
    code = [
        # "<div class='tableauPlaceholder' id='viz1600181558788' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ko&#47;korea_tourismv2_0&#47;TouristNumberandGrowthRateofDifferentContinets&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='korea_tourismv2_0&#47;TouristNumberandGrowthRateofDifferentContinets' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ko&#47;korea_tourismv2_0&#47;TouristNumberandGrowthRateofDifferentContinets&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-Hant' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1600181558788');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>",
        "<div class='tableauPlaceholder' id='viz1600610110633' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;-_&#47;-_16006100223390&#47;sheet0&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='views&#47;-_16006100223390&#47;sheet0?:language=zh-Hant&amp;:embed=y&amp;:display_count=y&amp;publish=yes' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;-_&#47;-_16006100223390&#47;sheet0&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-Hant' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1600610110633');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>",
        
    ]

    # This file names must add '.txt' as postfix
    # For example: (This two board use same .txt file)
    files = [
        # "Tourist Number and Growth Rate of Different Continents.txt",
        # "Description-2017 vs. 2018 Foreign Visitors to South Korea By Country-of-Origin.txt",
        # "Description-2017 vs. 2018 Foreign Visitors to South Korea By Country-of-Origin.txt",
    ]

    # Add a custom title, the number starts from 0
    title = {
        # 1: 'Foreign Visitor to Korea(pie chart)',
        # 2: 'Foreign Visitor to Korea(bar chart)'
    }

    # If create all files, then set as False
    onlyPartFile = False

    # This shows the number you want to start, start from 0
    # For example, if want to create the file from NO.2(bar chart) then this should be set as 2
    startFrom = 2

    # This is the number of files you want to create
    length = 1

    for i in getData(onlyPartFile, startFrom, length):
        print(i['title'])
        createFile(i)
