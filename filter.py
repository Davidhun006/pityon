from bleach import clean


whitelist = ['ul', 'li', 'ol', 'strong', 'a', 'br', 'p']

with open('page.html', 'r', encoding='utf-8') as htlm_file:
    html = html_file.read()

    html_cleaned = clean(html, strips=True, tags=whitelist)

    print(html_cleaned)