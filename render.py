#!/usr/bin/python

import sys
import os
import yaml
import isbnlib
from imdb import IMDb



def render_item(item, header, indent):
    typ = list(item.keys())[0]
    markdown = ""
    metadata = item[typ]

    markdown = " " * 4 * indent

    if typ == "section":
        markdown += "- ##"
        markdown += "#" * header
        markdown += " {}\n\n".format(metadata["title"])

    elif typ == "article":
        markdown += "- [ ] 📝 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])
        
    elif typ == "book":
        if "title" not in metadata:
            isbn = str(metadata['isbn'])
            if isbnlib.notisbn(isbn, level='strict'):
                print("invalid isbn {}".format(isbn))
                raise

            data = isbnlib.meta(isbn)
            if "Title" not in data:
                data = isbnlib.meta(isbn, 'openl')
            metadata["title"] = data["Title"]
        if "link" not in metadata:
            metadata["link"] = "https://www.amazon.com/s?k={}".format(metadata['isbn'])
        
        markdown += "- [ ] 📖 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])

    elif typ == "website":
        markdown += "- [ ] 🌐 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])

    elif typ == "video":
        markdown += "- [ ] 🎥 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])

    elif typ == "paper":
        markdown += "- [ ] 📒 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])

    elif typ == "legaldoc":
        markdown += "- [ ] 📜 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])

    elif typ == "podcast":
        markdown += "- [ ] 🎧 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])

    elif typ == "forum":
        markdown += "- [ ] 💬 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])

    elif typ == "tweet":
        markdown += "- [ ] 🐦 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])
    
    elif typ == "spec":
        markdown += "- [ ] 📑 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])
    
    elif typ == "code":
        markdown += "- [ ] 💻 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])
    
    elif typ == "tutorial":
        markdown += "- [ ] 📋 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])
    elif typ == "course":
        markdown += "- [ ] 🎓 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])
    

    elif typ == 'film':
        if "title" not in metadata:
            movie = IMDb().get_movie(metadata['imdb'])
            metadata["title"] = movie
        if "link" not in metadata:
            metadata["link"] = "https://www.imdb.com/title/tt{}".format(metadata['imdb'])
        
        markdown += "- [ ] 🎥 [**{}**]({})\n\n".format(metadata["title"], metadata["link"])


    elif typ == "text":
        if "completable" in metadata and metadata["completable"]:
            if "title" in metadata:
                markdown += "- [ ] **{}**\n\n".format(metadata["title"])
                markdown += " " * (4 * indent)
                markdown += "    {} \n\n".format(metadata["description"])
            else:     
                markdown += "- [ ] {} \n\n".format(metadata["description"])
        else:
            if "title" in metadata:
                markdown += "**{}**\n\n".format(metadata["title"])
                markdown += " " * (4 * indent)
                markdown += "{} \n\n".format(metadata["description"])
            else:
                markdown += "{} \n\n".format(metadata["description"])

    else:
        print(typ)
        raise


    if "description" in metadata and typ != "text":
        markdown += " " * (4 * indent)
        markdown += "    "
        markdown += "{}\n".format(metadata["description"].replace("\n","\n\n    {}".format(" " * (4 * indent))))
        markdown += "\n"
        
    if "items" in metadata:
        for item in metadata["items"]:
            markdown += render_item(item, header + 1, indent + 1)
            # if list(item.keys())[0] == "section":
            #     markdown += render_item(item, header + 1, indent + 1)
            # else:
            #     markdown += render_item(item, header, indent + 1)
    
        

    return markdown



if len(sys.argv) < 2:
    print("pass yaml to render as command line argument")
    exit

with open(sys.argv[1]) as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    syllabus = yaml.load(file, Loader=yaml.FullLoader)

    markdown = ""

    markdown += "# {} \n".format(syllabus["title"])
    if "curator" in syllabus:
        markdown += "## **{}".format(syllabus["curator"])
        if "source" in syllabus:
            markdown += ' | [(Source)]({})'.format(syllabus["source"])
        markdown += "**\n"

    markdown += "---\n\n"

    if "description" in syllabus:
        markdown += syllabus["description"].replace("\n","\n\n")
        markdown += "\n"
        

    for item in syllabus["items"]:
        markdown += render_item(item, 0, 0)
        # if list(item.keys())[0] == "section":
        #     markdown += render_item(item, 0, 0)
        # else:
        #     markdown += render_item(item, 0, 0)

    print(markdown)

    

    with open("./markdown/{}.md".format(os.path.splitext(os.path.basename(sys.argv[1]))[0]), "w") as htmlfile:
        htmlfile.write(markdown)