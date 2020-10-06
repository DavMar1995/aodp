from datetime import date
import os


def create_file(file_name, html):
    folder_name = f'html/{date.today().strftime("20%y_%m_%d")}'
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    f = open(f'{folder_name}/{file_name}.html', 'w', encoding='utf-8')
    f.write(html)
    f.close()


def get_file(file_dict):

    name = file_dict['name']
    title = file_dict['title']
    code_dict = file_dict['code_dict']

    tableau_code = ''
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

    for data in code_dict:
        if data['changeLanguage']:
            data['code'] = data['code'].replace(
                "value='zh-Hant'", "value='en'")
        split_point = data['code'].find('<script')
        tableau_code += f"""
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

    html = head + style + front + tableau_code + end + script + '</html>'

    create_file(name, html)

    print(f'"{name}" has been completed!')


def insert_data():
    name = input('Insert filename: ')
    title = input('Insert title: ')
    code_list = []

    while True:
        code_list.append(insert_code())
        if is_continuted('Another tableau board in this page? (Y/N)', 2):
            break

    file = {
        'name': name,
        'title': title,
    }
    pass


def insert_code():
    if input('Need to change to English or not? (Y/N)  ') == 'Y':
        change_language = True
    else:
        change_language = False
    code = input('Please insert embed code from tableau')

    return {
        'change_language': change_language,
        'code': code}


def is_continuted():
    cont = input()
    if cont == 'Y' or cont == 'y':
        return True
    elif cont != 'N' or cont == 'n':
        return False
    else:


if __name__ == '__main__':

    FILE_DICT = [
        {
            'name': '',
            'title': '',
            'code_list': [
                {
                    'change_language': False,
                    'code': "",
                },
            ],
        },
    ]

    insert_data()

    for file in FILE_DICT:
        get_file(file)


