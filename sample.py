def browser():
    n = input()
    import webbrowser
    import requests
    from bs4 import BeautifulSoup
    url = "https://www.google.com/search?q=" + n
    def open_website():
        webbrowser.open(url)
    if __name__ == "__main__":
        open_website()

def square():
    import turtle
    n = input().split(' ')
    if n.count('square') != 0:
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
square()
