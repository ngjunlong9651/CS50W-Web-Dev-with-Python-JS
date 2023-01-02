from django.shortcuts import render
from django.http import HttpResponse
import markdown

from . import util


## Creating a markdown to HTML converter function using markdown package
def md_converter(titles):
    content = util.get_entry(titles)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)



def index(request): ## This function will send existing entries to the front end 
                    ## located at templates/encyclopedia/index.html
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request,title):
    html_content = md_converter(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "This entry does not exist yet."
        })
    else:
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": html_content
        })


def new_page(request):
    return render(request, "encyclopedia/new_page.html")


def random_page(request):
    return render(request, "encyclopedia/random_page.html")