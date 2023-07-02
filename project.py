from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("Web Scraping")
root.geometry("700x250")
root.config(bg = "#0EC1C7")

# function to get url and all required data
def find():
    if entry.get():
        url = entry.get()
        r = requests.get(url)
        htmlContent = r.content
        soup = BeautifulSoup(htmlContent, "html.parser")
        file = open(entry_2.get(), 'w')
        file.writelines("Title of page is: \n")
        file.close()


        # to get title of page
        a = soup.find('title')
        abc = a.get_text()
        file = open(entry_2.get(), 'a')
        file.write(abc)


        # to get text of page
        file.write("\n\nThe text of page is: \n")
        for p in soup.find_all("p"):
            ptxt = p.get_text()
            file.write("%s\n" % ptxt)


        # to get links in page of url
        links = soup.find_all('a')
        file.write("\n\nThe links in this page are: \n")
        for link in links:
            if (link.get('href')):
                linktext = link.get('href')
                for l in linktext:
                    if linktext.startswith(('http://', 'https://')):
                        ltxt = linktext
                        file.write("%s\n" % ltxt)
                        break


        # to get image from url
        images = soup.find_all('img')
        file.write("\n\nThe images in this page are: \n")
        for image in images:
            if (image.get('src')):
                image_ = image.get('src')
                for i in image_:
                    if image_.endswith(('jpg', 'png')):
                        img = image_
                        file.write("%s\n" % img)
                        break

        file.close()


# label and entry to get url
label_1 = Label(root, text="Enter URL", font=('arial', 10), fg="black")
label_1.place(x=80, y=50)
label_1.config(bg = "#0EC1C7")
entry = Entry(root, width=55)
entry.place(x=180, y=50)

# label and entry to get file name with extension
label_2 = Label(root, text="Give name for file", font=('arial', 10), fg="black")
label_2.place(x=60, y=100)
label_2.config(bg = "#0EC1C7")
entry_2 = Entry(root, width=55)
entry_2.place(x=180, y=100)

# button to run to function and get data
button = Button(root, width=10, text="Get Data", command=find)
button.place(x=180, y=150)
button.config(bg = "#7DC23B")

root.mainloop()