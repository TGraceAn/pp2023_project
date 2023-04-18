from tkinter import *
from .Table import Table
from .AddWindow import AddWindow

class RepairWindow(Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.data_update = {}
    def add_widget(self, row_names: list[str], padx=4, pady=2):
        frame = Frame(self)
        frame.pack(side=TOP)
        self.entrys = []
        for index_row in range(0, len(row_names)):
            label = Label(frame, text=row_names[index_row].upper())
            label.pack()
            entry = Entry(frame)
            entry.pack()
            self.entrys.append(entry)
        self.submit = Button(self, text = "Submit", command=self.repair_submit_handle)
        self.submit.pack(padx = padx, pady = pady)
    def insert_data(self, values):
        for index in range(0, len(self.entrys)):
            self.entrys[index].insert(0, str(values[index]))
    def set_alert(self, alert):
        self.alert = alert
    def repair_submit_handle(self):
        data = self.get_entry_data()
        cols = self.table.cols
        item = self.table.select_item
        self.table.treev.item(item, values=data)
        for index in range(0, len(cols)):
            self.data_update.update({cols[index] : data[index]})
        self.destroy()

    # def get_data_list(self):
    #     return self.data_update

    def get_entry_data(self):
            data_list = []
            for entry in self.entrys:
                data = entry.get()
                if data == "":
                    data_list.append(None)
                else:
                    data_list.append(data)
            return data_list
    def set_table(self, table : Table):
        self.table = table
    


if __name__ == "__main__":
    win = RepairWindow("NOPE")

    win.mainloop()
    