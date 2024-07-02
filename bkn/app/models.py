from app.database import get_db


class Receta:

    # constuctor
    def __init__(self, id_receta=None, title=None, ingredientes=None, procedimiento=None, banner=None):
        self.id_receta = id_receta
        self.title = title
        self.ingredientes = ingredientes
        self.procedimiento = procedimiento
        self.banner = banner

    def serialize(self):
        return {
            'id_receta': self.id_receta,
            'title': self.title,
            'ingredientes': self.ingredientes,
            'procedimiento': self.procedimiento,
            'banner': self.banner
        }

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM recetas"
        cursor.execute(query)
        rows = cursor.fetchall()  # Me devuelve un lista de tuplas

        recetas = [Receta(id_receta=row[0], title=row[1], ingredientes=row[2], procedimiento=row[3], banner=row[4]) for row in rows]

        # movies = []
        # for row in rows:
        #     new_movie = Movie(id_movie=row[0], title=row[1], director=row[2],
        #  release_date=row[3], banner=row[4])
        #     movies.append(new_movie)

        cursor.close()
        return recetas

    @staticmethod
    def get_by_id(receta_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM recetas WHERE id_receta = %s", (receta_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Receta(id_receta=row[0], title=row[1], ingredientes=row[2], procedimiento=row[3], banner=row[4])
        return None

    """
    Insertar un registro si no existe el atributo id_receta
    """
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_receta:
            cursor.execute("""
                UPDATE recetas SET title = %s, ingredientes = %s, procedimiento = %s, banner = %s
                WHERE id_receta = %s
            """, (self.title, self.ingredientes, self.procedimiento, self.banner, self.id_receta))
        else:
            cursor.execute("""
                INSERT INTO recetas (title, ingredientes, procedimiento, banner) VALUES (%s, %s, %s, %s)
            """, (self.title, self.ingredientes, self.procedimiento, self.banner))
            self.id_receta = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM recetas WHERE id_receta = %s", (self.id_receta,))
        db.commit()
        cursor.close()
