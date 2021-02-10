"""crud"""



from model import db, User, Stock, CompanyStat, UserFavorite, connect_to_db

# user info================================================================
def get_user():
    """Return list of user objects"""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary with user email"""
    user_id_identification = User.query.get(user_id)

    return user_id_identification

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_user(email, password, dob, first_name, last_name):
    """create a new user"""

    user = User(email=email,
                password=password, 
                dob=dob, 
                first_name=first_name, 
                last_name=last_name)

    db.session.add(user)
    db.session.commit()

    return user

def check_password(email, password):
    """ Check password and email for logging in"""

    user= get_user_by_email(email)

    if user == None:
        return False
    elif user.password == password:
        return True
    else:
        return False
# stock info ================================================================

def create_stock_info(symbol, name, description, ceo, headquarters, founded, employees, address, sector, exchange, asset_type):
    """create a stocks profile"""
    stock = Stock(symbol=symbol, 
                name=name,
                description=description, 
                founded=founded,
                employees=employees,
                exchange=exchange, 
                asset_type=asset_type)

    db.session.add(stock)
    db.session.commit()

    return stock

def get_stocks_info():
    """Return all stocks"""

    return Stock.query.all()

def create_company_stat():
    """create stocks stats"""

    companyStat= CompanyStat(
            gross_profit = gross_profit,
            peratio=peratio,
            pegratio = pegratio,
            dividend_share = dividend_share,
            dividend_yield = dividend_yield, 
            week52high = week52high, 
            week52low =  week52low,
            eps = eps, 
            stock_id = stock_id,
            stock = stock )

    db.session.add(company_stat)
    db.session.commit()

    return company_stat

def get_company_stat():
    """Return all company stat"""

    return CompanyStat.query.all()


    
# favorite info ================================================================
def create_favorites(user_id, stock_id):
    """create a and returns user favorites from stocks list """

    userFavorites = UserFavorites(
                    user_id = user_id,
                    stock_id = stock_id)

    
    db.session.add(userFavorites)
    db.session.commit()

    return userFavorites

def user_favorites(user_id):
    """returns all user favorites"""
    user_id_identification = User.query.get(user_id)

    return Stock.query.all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)





