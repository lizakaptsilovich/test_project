from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

engine = create_engine("postgresql+psycopg2://postgres:lizalocal@localhost:5432/lizalocal")


class Base(DeclarativeBase): pass


class Person(Base):
    tablename = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


# создаем таблицы
Base.metadata.create_all(bind=engine)

# создаем сессию подключения к бд
with Session(autoflush=False, bind=engine) as db:
    # создаем объект Person для добавления в бд
    tom = Person(name="Tom", age=38)
    db.add(tom)  # добавляем в бд
    db.commit()  # сохраняем изменения
    print(tom.id)  # можно получить установленный id