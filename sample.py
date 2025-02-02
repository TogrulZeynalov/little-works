def browser():
    print('browser function is active, give input:')
    n = input()
    import webbrowser
    import requests
    url = "https://www.google.com/search?q=" + n
    def open_website():
        webbrowser.open(url)
    if __name__ == "__main__":
        open_website()

def square():
    import turtle
    print('square function is active, give input:')
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
browser()

