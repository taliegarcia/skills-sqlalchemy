# Note: this file will not run. It is only for recording answers.

# Part 2: Write queries

# Get the brand with the **id** of 8.
brand = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
corv_chevs = Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
older_models = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
golden_brands = Brand.query.filter(Brand.founded > 1920).all()
# this seems to work...but some results in the list [golden_brands] give me this error:
# UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 22: ordinal not in range(128)
# but the query DOES run without error...just when I try to look at some of the brand objects in the list
# there is that unicode error!
# ok - I cheated - I updated the name Citroën to Citroen inside sqlite3
# now this runs fine....but should probably be a better way to set up the unicode format


# Get all models with names that begin with "Cor".
cor_models = Model.query.filter(Model.name.startswith("Cor")).all()
# could not get this to work with filter_by instead of filter
# why??

# Get all brands with that were founded in 1903 and that are not yet discontinued.
brands_continued = Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
brands_old_or_done = Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
not_chevrolets = Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    my_fav_brands = Brand.query.filter(Brand.name.like('%' + mystr + '%')).all()
    return my_fav_brands


def get_models_between(start_year, end_year):
    models_of_the_times = Model.query.filter(Model.year > start_year, Model.year < end_year).all()
        # for m in models_of_the_times:
        #     print m.name, m.year
    return models_of_the_times

# Part 3: Discussion Questions

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# It is a query object. No value is returned until we fetch results with .all(), .first(), .one()

# 2. In your own words, what is an association table, and what *type* of relationship 
# does an association table manage?
# An association table only contains information on exactly how the relationship between other tables is defined
# It does not contain any unique information (except an id per instance)
# We can think of it as a table with a primary key and the other attributes would all be foreign keys
# or references to the associated tables - do not store any other info in an assoc table 
