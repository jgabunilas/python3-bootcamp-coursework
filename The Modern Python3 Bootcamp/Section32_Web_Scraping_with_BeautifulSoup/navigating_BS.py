from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="super-special">This list item is special.</li>
    <li>This list item is not special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="no">bye</div>
</body>
</html>
"""

# soup = BeautifulSoup(html, "html.parser")
# data = soup.body.contents[1].next_sibling.next_sibling
# print(data)

# soup = BeautifulSoup(html, "html.parser")
# data = soup.find(class_="super-special").parent
# print(data)

# soup = BeautifulSoup(html, "html.parser")
# data = soup.find(id="first").find_next_sibling()
# print(data)

soup = BeautifulSoup(html, "html.parser")
data = soup.find(class_ = "super-special").find_next_sibling(class_="special")
print(data)