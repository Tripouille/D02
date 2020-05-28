import os


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False,
                 skip_top=0, skip_bottom=0):
        self.file = open(filename, 'r')
        if header:
            self.header = self.file.readline()
        else:
            self.header = None
        self.data = [line.replace('\n', '').split(sep)
                     for line in self.file.readlines()]
        self.len = len(self.data)
        if skip_top + skip_bottom > self.len:
            raise ValueError("skip_top or skip_bottom too high")
        elif skip_top + skip_bottom == self.len:
            self.data = []
        else:
            self.data = self.data[skip_top:]
            if skip_bottom:
                self.data = self.data[:-skip_bottom]

    def close(self):
        self.file.close()

    def __enter__(self):
        if not all(len(self.data[0]) == len(line) for line in self.data):
            return None
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header


if __name__ == "__main__":
    filename = 'test.csv'
    os.system("cat " + filename)
    print("\n")
    with CsvReader(filename, sep=',', header=False,
                   skip_top=1, skip_bottom=1) as file:
        if file is None:
            print("File is corrupted")
        else:
            print("\nheader:", file.getheader())
            print('data:', file.getdata())
