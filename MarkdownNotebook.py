from tkinter import *

root = Tk()
root.title('MD Notes')
root.geometry('1000x600')
root.configure(bg='#b4d1e1')

# name = str(input('Nombra la nota...: '))
# content = str(input('Escribe algo...: '))
note_name = Entry(root)
note_name.pack()

main_text_field = Text()
main_text_field.pack()


def create_new_note(file_name, content):
    with open(f'{file_name}.txt', 'x', encoding='UTF-8') as new_note:
        new_note.write(content)
        confirm_new_note['text'] = 'Nota creada'


save_new_note_bt = Button(root, text='Guardar', command=lambda: create_new_note(file_name=note_name.get(),
                                                                                content=main_text_field.get('1.0', END)))
save_new_note_bt.pack()

confirm_new_note = Label(root)
confirm_new_note.pack()

#
# def select_and_edit():
#     selected_note = str(input(f'¿Cómo se llama la nota?: '))
#     with open(f'{selected_note}.txt', 'w', encoding='UTF-8') as note:
#         print('Nota abierta')
#         new_content = str(input('Escriba el nuevo texto: '))
#         note.write(new_content)


# create_new_note(name, content)
# select_and_edit()

if __name__ == '__main__':
    root.mainloop()
