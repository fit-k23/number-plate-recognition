

image = "https://metalbyexample.com/wp-content/uploads/figure-65.png"
url = "https://lens.google.com/uploadbyurl?hl=en&lr=en&url=" + image
response = s.get(url)

print(response)