import os
import shutil
from generate_page import generate_page_recursive
build_location = "docs"
def main(basepath = "/"):
    print("Copying...")
    copy_static("static", build_location)
    generate_page_recursive(f"content", "template.html", build_location, basepath)

source_cleaned = False
def copy_static(source, destination):
    if os.path.exists(source):
        global source_cleaned
        if source_cleaned == False:
            shutil.rmtree(destination)
            print(f"Cleaned {destination}!")
            source_cleaned = True
            os.mkdir(destination)
        contents = os.listdir(source)
        for path in contents:
            print(f"Now checking: {source}/{path}")
            if not os.path.exists(destination):
                os.mkdir(os.path.join(destination))
            if os.path.isfile(os.path.join(source, path)):
                shutil.copy(os.path.join(source, path), os.path.join(destination, path))
                print(f"Moved {os.path.join(source, path)} to {os.path.join(destination, path)}")
            else:
                copy_static(os.path.join(source, path), os.path.join(destination, path))





if __name__=="__main__":
    main()