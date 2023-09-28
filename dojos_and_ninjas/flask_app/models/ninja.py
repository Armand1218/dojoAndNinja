from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL("dojo_ninjas_schema").query_db(query, data)

    @classmethod
    def edit_ninja(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL("dojo_ninjas_schema").query_db(query, data)

    @classmethod
    def get_one_db(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL("dojo_ninjas_schema").query_db(query, data)
        return cls(result[0])

    @classmethod
    def delete_ninja(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL("dojo_ninjas_schema").query_db(query, data)