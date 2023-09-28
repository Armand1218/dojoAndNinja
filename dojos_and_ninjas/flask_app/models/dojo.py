from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojo_ninjas_schema").query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save_dojo_db(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        results = connectToMySQL("dojo_ninjas_schema").query_db(query, data)
        return results

    @classmethod
    def one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL("dojo_ninjas_schema").query_db(query, data)
        return cls(results[0])

    @classmethod
    def update_dojo(cls, data):
        query = "UPDATE dojos SET name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL("dojo_ninjas_schema").query_db(query, data)

    @classmethod
    def delete_dojo(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL("dojo_ninjas_schema").query_db(query, data)

    @classmethod
    def get_dojo_ninja(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojo_ninjas_schema").query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for dojos in results:
            d = {
                'id': dojos['ninjas.id'],
                'first_name': dojos['first_name'],
                'last_name': dojos['last_name'],
                'age': dojos['age'],
                'created_at': dojos['ninjas.created_at'],
                'updated_at': dojos['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(d))
        return dojo