"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
brand = Brand.query.filter(Brand.id == 8).one()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
chevy = Model.query.filter(Model.name=="Corvette", Model.brand_name=="Chevrolet").all()

# Get all models that are older than 1960.
pre_1960 = db.session.query(Brand.founded, Model.name).join(Model).filter(Brand.founded <= 1960)

# Get all brands that were founded after 1920.
after_1920 = Brand.query.filter(Brand.founded >= 1920)
>>> for brand in after_1920:
...     print brand.name


# Get all models with names that begin with "Cor".
cor = Model.query.filter(Model.name.like('%Cor%')).all()
>>> for car in cor:
...     print car.name

# Get all brands with that were founded in 1903 and that are not yet discontinued.
brand = Brand.query.filter(Brand.founded=="1903").filter(Brand.discontinued.isnot(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
b_1950_or_dis = Brand.query.filter(db.or_(Brand.founded < 1950, Brand.discontinued.is_(None))).all()
>>> for b in b_1950_or_dis:
...     print b.name

# Get any model whose brand_name is not Chevrolet.
 not_chevy = Model.query.filter(Model.brand_name.isnot("Chevrolet")).all()
 >>> for car in not_chevy:
...     print car.brand_name

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand)

    model_year_info = models.filter(Model.year==year)
    
    for model in model_year_info.all():
		print model.name, model.brand_name, model.headquarters


def get_brands_summary(brand_name):
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     summary =db.session.query(Model.brand_name, Model.name).filter(Model.brand_name=="brand_name")

     for sums in summary.all():
     	print sums.brand_name, sums.name


# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
## It returns the location of the flask_sqlalchemy BaseQuery object in memory

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

## An association table utilizes the primary key, foreign key relationship to demonstrate 'one-to-many relationships' between categories of data. 
