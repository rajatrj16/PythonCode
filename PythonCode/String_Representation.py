class book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, pages: {}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages


b = book("python","rajat",200)
print(b)
print(len(b))
