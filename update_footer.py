new_footer = open('footer.html', 'r').readlines()

pages = ['index.html', 'research.html', 'publications.html', 'contact.html']

for p in pages:
    found1 = False
    found2 = False
    page = open(p, 'r')
    lines = page.readlines()
    for i in range(len(lines)):
        if '<footer id="footer">' in lines[i]:
            start = i
            found1 = True
        if '</footer>' in lines[i]:
            end = i
            found2 = True
            break
    if not (found1 and found2):
        print(f'Footer tags not found in {p}. Skipping...')
        page.close()
        continue
    updated_page = lines[:start] + new_footer + ['\n'] +  lines[end+1:]

    page.close()

    page = open(p, 'w')
    page.writelines(updated_page)
    page.close()
    print('Footer updated successfully!')
