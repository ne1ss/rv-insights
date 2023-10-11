from src.create_database import *
from werkzeug.security import generate_password_hash
import pandas as pd

app_ctx = flask_app.app_context()
app_ctx.push()

logins_df = pd.read_excel('logins.xlsx')


for index, row in logins_df.iterrows():
    username = row[0]
    email = row[2]
    password = str(row[1])
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = Users(username=username, email=email, password=hashed_password)

    db.session.add(new_user)

db.session.commit()

## check
# users = Users.query.all()
# for user in users:
#   print(f"id: {user.id}, username: {user.username}, email: {user.email}, password:{user.password}", )
