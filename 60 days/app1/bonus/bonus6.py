contents = ["All carrots are to be sliced longitudinally.", "The carrots were reportedly sliced.", "The carrots were sliced by the chef."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"{filename}", "w")
    file.write(content)
    file.close()

