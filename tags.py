import requests
from bs4 import BeautifulSoup

#Refer https://www.crummy.com/software/BeautifulSoup/bs4/doc/

with open("sample.html", "r") as f:
    html_doc = f.read()  # html_doc will have the content of this text file as string

soup = BeautifulSoup(html_doc, "html.parser") # BeautifulSoup ye sample.html de mai apne hisaab se soup banaunga jisme mai comfortable hu
#ek aisa object jaha pe mai apne comfort ke hisaab se tag fecth kar paau

# print(soup.prettify())  # HTMl content beautify hoke dikhta hai 


# print(soup.title.string, type(soup.title.string)) # To get tiltle of page

# print(soup.div) # To get 1st div tag element

# print("To get HTML element of all that type",soup.findAll("div"))         # To get HTML element of all that type
# print("To get 1st div element",soup.findAll("div")[0])         # To get 1st div element
# print("To get 2nd div element",soup.findAll("div")[1])         # To get 2nd div element



# for link in soup.find_all("a"):
#     print(link.get("href"))        # to get link 
#     print(link.get_text())          # To get Text  


# s= soup.find(id="link3")
# print(s.get("href"))


# print(soup.select("div.italic"))  # We can also extract data css selector ki madad se bhi extract kr sakte hai
# print(soup.select("span#italic"))   # If we want to select with id
# print(soup.span.get("class"))  # soup ke span ka class ka naam bata do 

# print(soup.find(class_="italic"))  # to just get the first class of italic type
# print(soup.find_all(class_="italic")) # To get all the class of italic type 

# To see how many childrens are there in that element
# for child in soup.find(class_="container").children: # Find by id, ek aisa div find karo jiski id container ho aur uske saare children hai wo de do
#     print(child)                                        # Kabhi kisi element ke children chahiye toh

# pehla element with class = box print kaise karungi
# i=0
# for parent in soup.find(class_="box").parents: # Box --> container --> body
#     i+=1
#     print(parent)
#     if(i==2):
#         break

# cont = soup.find(class_="container")
# # print(cont)
# cont.name="span"            #To modify elements
# cont["class"] ="myclass class2" # to give more than one class which is myclass class2
# cont.string = "I am a string"
# print(cont)


# # To insert a new Tag
# # we need to first prepare a new tag.

# ulTag = soup.new_tag("ul")

# liTag = soup.new_tag("li")
# liTag.string ="Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string ="About"
# ulTag.append(liTag)

# soup.html.body.insert(0,ulTag ) # ye body ka 0th element banega
# with open("modified.html", "w") as f:
#     f.write(str(soup))


# Now to know kisi Tag me koi attribute hai ki nahi hai
# cont = soup.find(class_="container")
# print(cont.has_attr("id"))
# print(cont.has_attr("class"))
# print(cont.has_attr("contenteditable"))



# Kisi ek tag andar me class hai lekin id attribute nahi hai ye pata lagana hai agar toh
def has_class_but_not_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id") # yaane ki isme id attribute na ho par class attribute ho tab wo tag jo hai tab usse return true kare function

# ek aisa tag jiske child ke andar ek given class ka element hai ki nahi

#kuch aise finall ka istemal kar sakte hai hum ab

# results = soup.find_all(has_class_but_not_id) # wo saare element de do jiske liye ye functn True return karta hai
# for result in results:
#    print(result, "\n\n")


#meta tags jisme sirf content attribute set hai wo kaise find out kare
def has_content(tag):
    return tag.has_attr("content")

#find all let ahai args like class_=,id=, function bhi le leta hai aur uss functn ke acc jo ho tag True return karenge unko humko de deta hai
results = soup.find_all(has_content) # wo saare element de do jiske liye ye functn True return karta hai
for result in results:
   print(result, "\n\n")

