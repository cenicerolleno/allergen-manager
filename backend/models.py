from extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum
from sqlalchemy import String, Boolean, Enum, DateTime, ForeignKey, Table, Column, Integer


allergens_ingredients = Table(
    'allergens_ingredients',
    db.metadata,
    Column('allergen_id', Integer, ForeignKey('allergens.id'), primary_key=True),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'), primary_key=True)
)

class AllergenStatus(enum.Enum):
    pending = "pending"
    no_allergens = "no_allergens"
    not_found = "not_found"



class Allergen(db.Model):
    __tablename__ = 'allergens'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)  
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


    def __repr__(self):
        return f"Allergen {self.name}"
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_active': self.is_active
        }
        
class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    
    def __repr__(self):
        return f"User {self.username}"
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'is_active': self.is_active
        }
        
    
class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    api_id: Mapped [str] = mapped_column(String(100), nullable=True)
    allergen_status: Mapped[AllergenStatus] = mapped_column(Enum(AllergenStatus), default=AllergenStatus.pending, nullable=False)   
    last_updated: Mapped[DateTime] = mapped_column(DateTime,nullable=True)
    
    allergens = relationship('Allergen', secondary=allergens_ingredients, backref='ingredients')

    def __repr__(self):
        return f"Ingredient {self.name}"
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_active': self.is_active,
            'api_id': self.api_id,
            'allergen_status': self.allergen_status.value,
            'last_updated': self.last_updated
        }
        
class Dish(db.Model):
    __tablename__ = 'dishes'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    
    user: Mapped['User'] = relationship(backref='dishes')
    
    def __repr__(self):
        return f"Dish {self.name}"
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_active': self.is_active,
            'user_id': self.user_id
        }
        
class DishIngredient(db.Model):
    __tablename__ = 'dish_ingredients'

    id: Mapped[int] = mapped_column(primary_key=True)
    dish_id: Mapped[int] = mapped_column(ForeignKey('dishes.id'), nullable=False)
    ingredient_id: Mapped[int] = mapped_column(ForeignKey('ingredients.id'), nullable=False)
    
    dish: Mapped['Dish'] = relationship(backref='dish_ingredients')
    ingredient: Mapped['Ingredient'] = relationship(backref='dish_ingredients')
    
    def __repr__(self):
        return f"DishIngredient {self.dish_id} - {self.ingredient_id}"
    
    def serialize(self):
        return {
            'id': self.id,
            'dish_id': self.dish_id,
            'ingredient_id': self.ingredient_id
        }
        