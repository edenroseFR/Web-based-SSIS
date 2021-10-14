

def search_by_field(rows=None, keyword=None, field='id'):
    result = []
    for row in rows:
        row_allcaps = [str(cell).upper() for cell in row if cell != '']

        if field == 'all':
            if keyword in row_allcaps:
                result.append(row)
        if field == 'id':
            if keyword in row_allcaps[0]:
                result.append(row)
        elif field == 'firstname':
            if keyword in row_allcaps[1]:
                result.append(row)
        elif field == 'middlename':
            if keyword in row_allcaps[2]:
                result.append(row)
        elif field == 'lastname':
            if keyword in row_allcaps[3]:
                result.append(row)
        elif field == 'gender':
            if keyword in row_allcaps[4]:
                result.append(row)
        elif field == 'yearlevel':
            if keyword in row_allcaps[5]:
                result.append(row)
        elif field == 'course':
            if keyword in row_allcaps[8]:
                result.append(row)

    return result