from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def show(self, indent=0):
        pass

class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print(" " * indent + f" {self.name}")


class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show(self, indent=0):
        print(" " * indent + f" {self.name}")
        for child in self.children:
            child.show(indent + 2)


if __name__ == "__main__":
    file1 = File("readme.txt")
    file2 = File("data.csv")
    file3 = File("photo.jpg")

    docs = Directory("Документы")
    docs.add(file1)
    docs.add(file2)

    images = Directory("Изображения")
    images.add(file3)

    root = Directory("Мой диск")
    root.add(docs)
    root.add(images)
    root.show()