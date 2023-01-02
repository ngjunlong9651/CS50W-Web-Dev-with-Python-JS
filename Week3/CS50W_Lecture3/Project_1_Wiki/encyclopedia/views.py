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
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    else:
        title = request.POST['new_entry'] ## This is taken from the new_page.html, converting new_entry into title
        content = request.POST['new_content']## This is taken from the new_page.html, converting new_content into content
        titleExist = util.get_entry(title)
        if titleExist is not None: ## Checking if the page exists.
            return render(request, "encyclopedia/error.html", {
                "message": "Entry Page Already Exists"
            })
        else: ## If page doesnt exist. Call save entry function from utiils
            util.save_entry(title,content)
            html_content = md_converter(content) ## Convert MD to html
            return render(request, "encyclopedia/entry.html",{
                "title": title,
                "content": html_content
            })



def random_page(request):
    return render(request, "encyclopedia/random_page.html")

def search(request):
    if request.method == "POST": ## Linked to the form in layout.html
        entry_search = request.POST['q'] ## Grabbing the data from the form's input segment
        html_content = md_converter(entry_search) ## Converting the type
        if html_content is not None: ## Ensuring that there was already an entry beforehand
            return render(request, "encyclopedia/entry.html", {
                "title" : entry_search,
                "content" : html_content
            }) ## Returns the content to the user is there was a previous entry
        else:
             allEntries = util.list_entries() ## Getting all entries prior
             auto_fill = [] ## Creating an empty list
             for entry in allEntries: ## Looping over all the entries 
                if entry_search.lower() in entry.lower(): ## Checking for individual spelling i.e if dj in django
                    auto_fill.append(entry) ## appends the previous entry to the newly created list - recommendations
             return render(request, "encyclopedia/search.html", { ## Returns the page to the user 
                "auto_fill": auto_fill
            })

def edit(request):
    if request.method == "POST":
        title= request.POST['entry_title']
        content=util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title":title,
            "content": content
        })

def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = md_converter(title) ## Converting the type
        return render(request, "encyclopedia/entry.html",{
            "title" : title,
            "content": html_content
        })