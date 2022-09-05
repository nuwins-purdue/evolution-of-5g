import glob
import os

country_list = glob.glob("images/performance_plots/*") #relative path to performance plots
country_html_dict = {}
# breakpoint()
for country in country_list:
    if "worldwide" in country or "United States of America" in country:
        continue
    country = country.split("/")[-1]
    country_short = country.strip()
    #read template.html into list 
    template_content_list = []
    fh = open("template.html", "r")
    data = fh.readlines()
    for d in data:
        if "template_long" in d:
            d = d.replace("template_long", country)
        if "template_short" in d:
            d = d.replace("template_short", country_short + ".html")
        template_content_list.append(d)
    fh.close()

    #transfer template data to new file
    fh = open("" + country_short + ".html", "w+")
    for template_data in template_content_list:
        fh.write(template_data)
    fh.close()
    # os.system("cp template.html %s.html" %country_short)
    country_html_dict[country] = country_short

#modify index_mod.html data
index_content_list = []
fh = open("index_mod.html", "r")
data = fh.readlines()
for d in data:
    # list_elem = d.strip()
    list_elem = d
    index_content_list.append(list_elem)
    if "modification start specific_stat" in d:
        # <li><a href="usa.html">United States of America</a></li>
        for country in country_html_dict.keys():
            base = "<li><a href=\"%s\">%s</a></li>\n" %(country_html_dict[country]+".html", country)
            index_content_list.append(base)
    
    if "modification start dropdown" in d:
        # <a href="usa.html">United States</a>
        for country in country_html_dict.keys():
            base = "<a href=\"%s\">%s</a>\n" %(country_html_dict[country]+".html", country)
            index_content_list.append(base)

fh.close()
#transfer index mod to index
fh = open("index.html", "w+")
for index_content in index_content_list:
    # fh.write(index_content + "\n")
    fh.write(index_content)
fh.close()