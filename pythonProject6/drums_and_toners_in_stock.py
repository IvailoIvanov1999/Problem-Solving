from tkinter import *
import sqlite3

# counter = 1
root = Tk()
root.title("Inventory")

# """ Create a database or connect to one"""
conn = sqlite3.connect("Inventory_book.db")

# """ Create a cursor """
c = conn.cursor()

""" Create a table """
c.execute("""CREATE TABLE IF NOT EXISTS inventory(
             Model text,
             toners integer,
             drums integer
             )""")

def click_button_add():
    conn = sqlite3.connect("Inventory_book.db")

    # """ Create a cursor """
    c = conn.cursor()

    c.execute("INSERT INTO inventory VALUES (:model,:toners,:drums)",
              {
                  "model": model.get(),
                  "toners": toners_count.get(),
                  "drums": drums_count.get()

              }

              )

    # """ Commit changes"""
    conn.commit()

    # """ Close connection """
    conn.close()

    # clear input field box
    model.delete(0, END)
    toners_count.delete(0, END)
    drums_count.delete(0, END)


def click_button_search():
    print_records = ""
    conn = sqlite3.connect("Inventory_book.db")

    # """ Create a cursor """
    c = conn.cursor()

    c.execute(f'SELECT *, oid FROM inventory')

    records = c.fetchall()

    print(records)

    for record in records:
        print_records += f'Model:  {record[0]}' + "  "
        print_records += f'[{str(record[1])} toners.]'  + ' '
        print_records += f'[{str(record[2])} drums.]'  + '\n'


    output_label = Label(root, text='\n' + print_records)
    output_label.grid(row=4, column=8, columnspan=2)

    # """ Commit changes"""
    conn.commit()

    # """ Close connection """
    conn.close()


top_label = Label(root, text="Input Device model: ")
top_label.grid(row=0, column=4, padx=30, pady=30)

sec_label = Label(root, text="Input Toners count: ")
sec_label.grid(row=1, column=4, padx=30, pady=30)

third_label = Label(root, text="Input Drums count: ")
third_label.grid(row=2, column=4, padx=30, pady=30)

model = Entry(root, width=50)
model.grid(row=0, column=5, padx=10, pady=10)
model.insert(0, "")

toners_count = Entry(root, width=50)
toners_count.grid(row=1, column=5, padx=10, pady=10)
toners_count.insert(0, "")

drums_count = Entry(root, width=50)
drums_count.grid(row=2, column=5, padx=10, pady=10)
drums_count.insert(0, "")

# add button
f_button = Button(root, text="Add the device", pady=10, command=click_button_add, fg="red")
f_button.grid(row=3, column=4, padx=10, pady=10)
# search button
s_button = Button(root, text="Show all", padx=25, pady=10, command=click_button_search, fg="green")
s_button.grid(row=3, column=8, padx=10, pady=10)





# """ Commit changes"""
conn.commit()

# """ Close connection """
conn.close()

root.mainloop()
