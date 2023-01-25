async def get_structure(text):
    text = str(text)
    structure_list = []
    index_p = 1
    index_li = 1

    while index_p >0:
        index_li = text.find('<ul>')
        index_p = text.find('<p>')
        # print('UL', index_li)
        # print('P', index_p)

        if index_p < index_li and index_p != -1:
            structure_list.append('p')
            text = text[index_p + 2:]
            # print('**P**')
            # print('len', len(text))
        else:
            if index_li != -1:
                structure_list.append('ul')
                text = text[index_li + 2:]
                # print('**UL**')
                # print('len', len(text))
            else:
                structure_list.append('p')
                text = text[index_p + 2:]
                # print('**P**')
                # print('len', len(text))
    while index_li > 0:
        index_li = text.find('<ul>')
        structure_list.append('ul')
        text = text[index_li + 2:]

    # match = re.findall(r'\<li\>', str(text))
    # for i in range(0, len(match)):
    #     structure_list.append('li')

    print(structure_list)
    return structure_list

async def get_structure_advance(text):
    text = str(text)
    structure_list = []
    index_p = 1
    index_li = 1

    while index_p >0:
        index_li = text.find('<ul>')
        index_p = text.find('<strong>')
        # print('UL', index_li)
        # print('P', index_p)

        if index_p < index_li and index_p != -1:
            structure_list.append('p')
            text = text[index_p + 2:]
            # print('**P**')
            # print('len', len(text))
        else:
            if index_li != -1:
                structure_list.append('ul')
                text = text[index_li + 2:]
                # print('**UL**')
                # print('len', len(text))
            else:
                structure_list.append('p')
                text = text[index_p + 2:]
                # print('**P**')
                # print('len', len(text))
    while index_li > 0:
        index_li = text.find('<ul>')
        if index_li >0:
            structure_list.append('ul')
            text = text[index_li + 2:]

    # match = re.findall(r'\<li\>', str(text))
    # for i in range(0, len(match)):
    #     structure_list.append('li')

    print(structure_list)
    return structure_list