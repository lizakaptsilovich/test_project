import datetime
from tkinter import *
from tkinter import ttk
import os
import re
import pandas as pd

folder_path = "/Users/lizavetakaptsilovich/Documents/mom"
changes_file = "/Users/lizavetakaptsilovich/Documents/mom2/changes.xlsx"

all_files = [i for i in os.listdir(folder_path) if i.endswith(".xlsx")]


def file_to_date(file_name):
    name = re.sub(r"\.xlsx$", "", file_name).replace("на ", "")
    return name


files_sorted = sorted(all_files, key=file_to_date, reverse=True)
files_final = [re.sub(r"\.xlsx$", "", f) for f in files_sorted]
files_with_empty = [""] + files_final

COLUMNS_TO_SHOW = ["Лицевой счет", "Кол-во месяцев долга", "Исх. сальдо без пени", "Исх. сальдо по пене",
                   "Просроченная задолженность"]
measures = ["Предупрежд", "Откл ЖКУ", "Увед о расторж", "Увед об отчужд", "Исполн Надп", "Выселение", "Посещение",
            "Отчуждение", "Опл п/ уведомл"]
measures_with_comment = measures + ["Комментарий"]
columns = ["Дата"] + COLUMNS_TO_SHOW
columns_second = ["Л/С"] + measures
headers_map = {
    "Предупрежд": "Предупрежд",
    "Откл ЖКУ": "Откл ЖКУ",
    "Увед о расторж": "Ув о расторж",
    "Увед об отчужд": "Ув о/ отчужд",
    "Исполн Надп": "Исп Надпись",
    "Выселение": "Выселение",
    "Посещение": "Посещение",
    "Отчуждение": "Отчуждение",
    "Опл п/ уведомл": "Оплата п/ ув"
}

root = Tk()
root.geometry("1200x800")
root.grid_rowconfigure(4, weight=1)



def validate_account():
    account = id_text.get().strip()
    if not account:
        return None, "Введите номер лицевого счета."
    if not account.isdigit():
        return None, "Лицевой счет должен быть числом."
    return int(account), ""


def check_info():
    # Очищаем Treeview перед поиском
    for row in text.get_children():
        text.delete(row)

    account, error_message = validate_account()
    if account is None:
        validation.config(text=error_message)
        return

    validation.config(text="")  # очищаем сообщение об ошибке

    drop1 = dropdown1.get()
    drop2 = dropdown2.get()

    # Формируем список файлов для поиска
    if not drop1 and not drop2:
        drop_list = files_sorted
    elif drop1 == drop2:
        drop_list = [drop1 + ".xlsx"]
    else:
        drop_list = []
        if drop1:
            drop_list.append(drop1 + ".xlsx")
        if drop2:
            drop_list.append(drop2 + ".xlsx")
        drop_list = sorted(drop_list, key=file_to_date, reverse=True)

    found = False
    account_str = str(account)  # приводим к строке для сравнения
    for file in drop_list:
        try:
            file_path = os.path.join(folder_path, file)
            df = pd.read_excel(file_path, engine="openpyxl", sheet_name="Лицевые счета", header=1, dtype=str)  # читаем всё как строки
            df["Лицевой счет"] = df["Лицевой счет"].astype(str)  # на всякий случай
            row = df[df["Лицевой счет"] == account_str]
            if not row.empty:
                found = True
                values = []
                file_display = re.sub(r"\.xlsx$", "", file).replace("на ", "")
                values.append(file_display)
                for col in COLUMNS_TO_SHOW:
                    val = row.iloc[0][col] if col in row.columns else ""
                    values.append(val)
                text.insert("", "end", values=values)
        except FileNotFoundError:
            validation.config(text=f"Файл {file} не найден")
            return
        except Exception as e:
            validation.config(text=f"Неизвестная ошибка: {e}")
            return

    if not found:
        validation.config(text=f"Лицевой счет {account} не найден")


def add_measure_func():
    measures_with_empty=[""] + measures
    popup = Toplevel(root)
    popup.title("Добавить меру")
    popup.geometry("380x180+180+130")
    save_validation = Label(popup, text="", fg="red", font=("Arial", 12))
    save_validation.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    account_name = Label(popup, text="Лицевой счет:")
    account_name.grid(row=1, column=0, padx=(20, 5), pady=5, sticky="e")
    account = Entry(popup, width=13)
    account.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    date_name = Label(popup, text="Выберите дату:")
    date_name.grid(row=2, column=0, padx=(20, 5), pady=5, sticky="e")
    frame3 = Frame(popup)
    frame3.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
    day = Spinbox(frame3, from_=1, to=31, width=5)
    day.grid(row=2, column=1)
    month = Spinbox(frame3, from_=1, to=12, width=5)
    month.grid(row=2, column=2)
    year = Spinbox(frame3, value=2025, width=5)
    year.grid(row=2, column=3)
    measure_name = Label(popup, text="Выберите меру:")
    measure_name.grid(row=3, column=0, padx=(20, 5), pady=5, sticky="e")
    measure = ttk.Combobox(popup, values=measures_with_empty, width=10, state="readonly")
    measure.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    save = Button(popup, text='Сохранить')
    save.grid(row=4, column=1, pady=5, sticky="w")

    id_in_popup = id_text.get()
    if id_in_popup:
        account.insert(0, id_in_popup)

    def save_changes():
        account_id = str(account.get()).strip()
        d = day.get().strip()
        m = month.get().strip()
        y = year.get().strip()
        meas = measure.get().strip()

        # Создаём dmy только если мера выбрана, чтобы избежать ошибок
        dmy = f"{int(d):02d}.{int(m):02d}.{y}" if meas else ""

        try:
            df = pd.read_excel(changes_file, engine="openpyxl")
            if "Лицевой счет" in df.columns:
                df.rename(columns={"Лицевой счет": "Л/С"}, inplace=True)
        except FileNotFoundError:
            if not meas:
                validation.config(text=f"Ошибка: Нельзя сохранить комментарий без меры, так как файл не существует.")
                popup.destroy()
                return
            df = pd.DataFrame(columns=["Л/С"] + measures_with_comment)

        df["Л/С"] = df["Л/С"].astype(str)

        for col in measures_with_comment:
            if col in df.columns:
                df[col] = df[col].astype(str).replace("nan", "")

        if account_id in df["Л/С"].values:
            if meas:
                old_record = df.loc[df["Л/С"] == account_id, meas].fillna("").values[0]
                if old_record.strip() == "":
                    dates = []
                else:
                    dates = old_record.split('\n')

                dates.append(dmy)
                sorted_dates = sorted(dates, key=lambda x: datetime.datetime.strptime(x, "%d.%m.%Y"))
                df.loc[df["Л/С"] == account_id, meas] = "\n".join(sorted_dates)
            else:
                save_validation.config(text=f"Мера не выбрана.")
                return
        else:
            if meas:
                new_row = {col: "" for col in df.columns}
                new_row["Л/С"] = account_id
                new_row[meas] = dmy
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            else:
                save_validation.config(text=f"Ошибка: Лицевой счет не найден, и мера не выбрана.")
                popup.destroy()
                return

        # Сохранение и закрытие
        with pd.ExcelWriter(changes_file, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']
            cell_format = workbook.add_format({'bold': True})
            worksheet.set_column('A:A', 25, cell_format)
            worksheet.set_column('B:L', 20)

        popup.destroy()
        if account_id:
            combo_func()
    save.config(command=save_changes)

def save_comment(event):
    id = id_text.get()
    comment_to_save = comments.get("1.0", "end-1c").strip()

    try:
        df = pd.read_excel(changes_file, engine="openpyxl")
        # Если колонка "Лицевой счет" есть, переименовываем её в "Л/С"
        if "Лицевой счет" in df.columns:
            df.rename(columns={"Лицевой счет": "Л/С"}, inplace=True)
    except FileNotFoundError:
        # 4. Если файл не найден, создаем новый DataFrame
        df = pd.DataFrame(columns=["Л/С", "Комментарий"])

    df["Комментарий"] = df["Комментарий"].astype(str).replace("nan", "")

    df["Л/С"] = df["Л/С"].astype(str)

    if id in df["Л/С"].values:
        df.loc[df["Л/С"] == id, "Комментарий"] = comment_to_save
    else:
        if comment_to_save:
            new_row = {col: "" for col in df.columns}
            new_row["Л/С"] = id
            new_row["Комментарий"] = comment_to_save
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        else:
            validation.config(text=f"Нельзя сохранить пустой комментарий для нового лицевого счета")
            return

    # Сохранение и закрытие
    with pd.ExcelWriter(changes_file, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

    validation.config(text="Комментарий успешно обновлен.", fg="green")


def show_measures():
    for row in text_second.get_children():
        text_second.delete(row)
    comments.delete("1.0", "end")
    account, error_message = validate_account()
    if account is None:
        validation.config(text=error_message)
        return

    for row in text_second.get_children():
        text_second.delete(row)

    try:
        df = pd.read_excel(changes_file, engine="openpyxl")
        if "Лицевой счет" in df.columns:
            df.rename(columns={"Лицевой счет": "Л/С"}, inplace=True)

        df["Л/С"] = df["Л/С"].astype(str)
        row = df[df["Л/С"] == str(account)]

        if not row.empty:
            values2 = [" " if pd.isna(row.iloc[0][col]) else row.iloc[0][col] for col in columns_second]
            value = [" " if pd.isna(row.iloc[0][col]) else row.iloc[0][col] for col in ["Комментарий"]]
            comment_text = value[0]
            text_second.insert("", "end", values=values2)
            comments.insert("end", comment_text)


    except FileNotFoundError:
        validation.config(text="Файл 'changes.xlsx' не найден. Создайте его, добавив первую меру.")
    except Exception as e:
        validation.config(text=f"Неизвестная ошибка: {e}")


def combo_func(event=None):
    for row in text.get_children():
        text.delete(row)
    for row in text_second.get_children():
        text_second.delete(row)
    comments.delete("1.0", "end")

    # 1. Выполняем валидацию
    account, error_message = validate_account()

    if account is None:
        validation.config(text=error_message)
        add_measure.config(state="disabled")
        edit_comment.config(state="disabled")
        return

    # 2. Выполняем поиск (check_info)
    check_info()

    # 3. Проверяем, было ли сообщение об ошибке (например, "не найден")
    # Если validation.cget('text') пуста, значит, счет найден, и ошибки нет.
    current_validation_text = validation.cget('text')

    if "не найден" in current_validation_text or current_validation_text != "":
        # Если есть ошибка, или счет не найден (сообщение непустое), отключаем кнопки
        add_measure.config(state="disabled")
        edit_comment.config(state="disabled")
    else:
        # Если поиск прошел успешно (validation.cget('text') пуста)
        add_measure.config(state="normal")
        edit_comment.config(state="normal")

    show_measures()


frame1 = Frame(root)
frame1.grid(row=4, column=1, padx=5, pady=5, sticky="sw")
frame2 = Frame(root)
frame2.grid(row=6, column=1, padx=5, pady=30, sticky="nsew")
frame3 = Frame(root)
frame3.grid(row=5, column=1, columnspan=2, padx=5, pady=30, sticky="nsew")

style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 12), padding=(5, 15, 5, 15), wraplength=80)
validation = Label(root, text="", fg="red", font=("Arial", 12))
validation.grid(row=0, column=1, padx=5, pady=5, sticky="w")
id = Label(root, text="Лицевой счет:")
id.grid(row=1, column=0, padx=(20, 5), pady=5, sticky="e")
id_text = Entry(root)
id_text.grid(row=1, column=1, padx=5, pady=5, sticky="w")
dropdown_frame=Frame(root)
dropdown_frame.grid(row=2, column=1, padx=5, pady=5, sticky="w")
drop_text = Label(root, text="Выберите 2 файла:")
drop_text.grid(row=2, column=0, padx=(20, 5), pady=5, sticky="e")
dropdown1 = ttk.Combobox(dropdown_frame, values=files_with_empty, width=10, state="readonly")
dropdown1.pack(side=LEFT, padx=(1,10))
dropdown2 = ttk.Combobox(dropdown_frame, values=files_with_empty, width=10, state="readonly")
dropdown2.pack(side=LEFT, padx=(1,5))
search = Button(root, text='Поиск')
search.grid(row=3, column=1, pady=5, padx=4, sticky="w")
text = ttk.Treeview(frame1, columns=columns, show="headings", height=12)
for col in columns:
    if col == "Лицевой счет":
        header = "Л/С"
    elif col == "Исх. сальдо без пени":
        header = "Сальдо"
    elif col == "Исх. сальдо по пене":
        header = "Пеня"
    elif col == "Кол-во месяцев долга":
        header = "КМД"
    elif col == "Просроченная задолженность":
        header = "П/З"
    else:
        header = col
    text.heading(col, text=header)
    if col in ("Дата", "Лицевой счет"):
        width = 60
    else:
        width = 90
    text.column(col, width=width, anchor="e")
text.grid(row=0, column=0, padx=5, pady=5)
comments = Text(frame1, height=5, width=50, wrap="word")
comments.grid(row=0, column=1, padx=(25, 5), pady=(5, 40))
add_measure = Button(frame3, text='Добавить меру', command=add_measure_func, state="disabled")
add_measure.grid(row=0, column=0, pady=5, sticky="w")
edit_comment = Button(frame3, text='Обновить комментарий', state="disabled")
edit_comment.grid(row=0, column=1, pady=5, padx=380, sticky="e")
text_second = ttk.Treeview(frame2, columns=columns_second, show="headings", height=12)
for col in columns_second:
    if col == "Л/С":
        header = "Л/С"
    else:
        header = headers_map.get(col, col)
    if col == "Л/С":
        width = 62
    else:
        width = 90
    text_second.heading(col, text=header)
    text_second.column(col, width=width, anchor="e")
text_second.grid(row=6, column=1, columnspan=2, padx=5, pady=30, sticky="nsew")

edit_comment.bind('<Button-1>', save_comment)
search.bind('<Button-1>', combo_func)
id_text.bind('<Return>', combo_func)
root.mainloop()