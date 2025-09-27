from sqlalchemy import create_engine, Column, Integer, String, func, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from tkinter import *

engine = create_engine("postgresql+psycopg2://liza_user:lizalocal@localhost:5433/lizalocal")

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    rating = Column(Float())
    description = Column(String(100))

    def __repr__(self):
        return f"<Movie(title='{self.title}', rating={self.rating})>"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

root=Tk()
root.geometry("600x500")

info = Entry(root, width=40)
info.grid(row=0, column=1, padx=5, pady=5, sticky="w")
title = Label(root, text="Title:")
title.grid(row=1, column=0, padx=(20, 5), pady=5, sticky="e")
title_text = Entry(root)
title_text.grid(row=1, column=1, padx=5, pady=5, sticky="w")
rating = Label(root, text="Rating:")
rating.grid(row=2, column=0, padx=(20, 5), pady=5, sticky="e")
rating_text = Entry(root)
rating_text.grid(row=2, column=1, padx=5, pady=5, sticky="w")
desc = Label(root, text="Description:")
desc.grid(row=3, column=0, padx=(20, 5), pady=5, sticky="e")
desc_text = Entry(root)
desc_text.grid(row=3, column=1, padx=5, pady=5, sticky="w")
save = Button(root, text='Save')
save.grid(row=4, column=1, pady=5, sticky="e")
text = Text(root, width=60, height=10)
text.grid(row=5, column=1, padx=5, pady=5, sticky="w")
view = Button(root, text='View all')
view.grid(row=6, column=1, pady=5, sticky="e")
search = Entry(root, width=30)
search.grid(row=7, column=1, padx=5, pady=5, sticky="w")
search_button = Button(root, text='Search by Name')
search_button.grid(row=7, column=1, pady=5, sticky="e")
clear_button = Button(root, text='Clear all fields')
clear_button.grid(row=8, column=1, pady=5, sticky="e")

def save_movie(event):
    title=title_text.get()
    rating=rating_text.get()
    desc=desc_text.get()

    if not title or not rating or not desc:
        info.delete(0, "end")
        info.config(fg="red")
        info.insert("0", "All fields must be populated.")
        return

    try:
        rating = float(rating)
    except ValueError:
        info.delete(0, "end")
        info.config(fg="red")
        info.insert("0", "Rating should be a numerical value.")
        return


    movie=Movie(title=title, rating=rating, description=desc)
    session.add(movie)
    title_text.delete(0, "end")
    rating_text.delete(0, "end")
    desc_text.delete(0, "end")
    session.commit()
    info.delete(0, "end")
    info.config(fg="green")
    info.insert("0", "The movie is successfully added!")

def show_all(event):
    text.delete("1.0", "end")
    with Session() as db:
       result=db.query(Movie).all()
       print("Result length:", len(result))
       if result:
           for i in result:
               text.insert("end", f"title: {i.title}, rating: {i.rating}, desc: {i.description}\n")
       else:
           text.insert("end", f"There are currently no movies added.")
def search_by_name(event):
    title=search.get()
    text.delete("1.0", "end")
    info.delete(0, "end")
    if not title:
        info.config(fg="red")
        info.insert("end", f"Enter a movie title.\n")
        return
    with Session() as db:
        result = db.query(Movie).filter(Movie.title.ilike(f"%{title}%")).all()
        if result:
            for i in result:
               text.insert("end", f"title: {i.title}\n")
        else:
            text.insert("end", f"Movie with such title is not found.\n")
    search.delete(0, "end")

def clear_all(event):
    info.delete(0, "end")
    text.delete("1.0", "end")
    search.delete(0, "end")


save.bind('<Button-1>', save_movie)
view.bind('<Button-1>', show_all)
search_button.bind('<Button-1>', search_by_name)
clear_button.bind('<Button-1>', clear_all)
root.mainloop()

