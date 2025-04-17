from sqlalchemy.orm import sessionmaker
from config.db import engine
from config.models import Author, Article 

# Session = sessionmaker(bind=engine)
# session = Session()

# ezz = Author(
#     firstname="Ezzeddin",
#     lastname="Abdullah",
#     email="ezz_email@gmail.com"
# )

# ahmed = Author(
#     firstname="Ahmed",
#     lastname="Mohammed",
#     email="ahmed_email@gmail.com"
# )


# article1 = Article(
#     slug="clean-python",
#     title="How to Write Clean Python",
#     content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
#     author=ezz
#     )

# # session.add(article1)
# # session.commit()

# print(article1.title)