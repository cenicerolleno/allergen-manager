from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import User, Allergen, Ingredient, Dish, DishIngredient
from extensions import db

class UsersModelView(ModelView):
    column_list = ('id', 'username', 'email', 'is_active', 'is_admin')
    column_searchable_list = ('username', 'email')
    form_columns = ('username', 'email', 'password_hash', 'is_active', 'is_admin')

class AllergensModelView(ModelView):
    column_list = ('id', 'name', 'is_active')
    column_searchable_list = ('name',)
    form_columns = ('name', 'is_active')
    
class IngredientsModelView(ModelView):
    column_list = ('id', 'name', 'is_active', 'allergen_status', 'last_updated', 'allergens')
    column_searchable_list = ('name',)
    form_columns = ('name', 'is_active', 'allergen_status', 'last_updated', 'allergens')
    
class DishesModelView(ModelView):
    column_list = ('id', 'name', 'is_active', 'dish_ingredients')
    column_searchable_list = ('name',)
    form_columns = ('name', 'is_active', 'dish_ingredients')
    
class DishIngredientsModelView(ModelView):
    column_list = ('id', 'dish_id', 'ingredient_id')
    form_columns = ('dish_id', 'ingredient_id')
    
def setup_admin(app):
    admin = Admin(app, name='Allergen Manager')
    admin.add_view(UsersModelView(User, db.session, endpoint='admin_users'))
    admin.add_view(AllergensModelView(Allergen, db.session, endpoint='admin_allergens'))
    admin.add_view(IngredientsModelView(Ingredient, db.session, endpoint='admin_ingredients'))
    admin.add_view(DishesModelView(Dish, db.session, endpoint='admin_dishes'))
    admin.add_view(DishIngredientsModelView(DishIngredient, db.session, endpoint='admin_dish_ingredients'))