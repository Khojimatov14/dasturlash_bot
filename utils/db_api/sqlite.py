import sqlite3

class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        with sqlite3.connect(self.path_to_db) as connection:
            cursor = connection.cursor()
            data = None
            cursor.execute(sql, parameters)

            if commit:
                connection.commit()
            if fetchall:
                data = cursor.fetchall()
            if fetchone:
                data = cursor.fetchone()
        return data

    def createTableVideos(self):
        sql = """
        CREATE TABLE Cources (
            id integer primary key,
            videoNum int NOT NULL,
            language varchar(20) NOT NULL,
            videoName varchar(255) NOT NULL,
            videoFileCode varchar(255)NOT NULL
            );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def formatArgs(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def addVideo(self, videoNum: int, language: str, videoName: str, videoFileCode: str):
        sql = """
        INSERT INTO Cources(videoNum, language, videoName, videoFileCode) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(videoNum, language, videoName, videoFileCode), commit=True)

    def selectAllVideos(self):
        sql = """
        SELECT * FROM Cources
        """
        return self.execute(sql, fetchall=True)

    def selectVideo(self, **kwargs):
        sql = "SELECT * FROM Cources WHERE "
        sql, parameters = self.formatArgs(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def countVideos(self, language):
        return self.execute(f"SELECT COUNT(*) FROM Cources WHERE language='{language}';", fetchone=True)

    def deleteVideos(self):
        self.execute("DELETE FROM Cources WHERE TRUE", commit=True)

    def createTableUsers(self):
        sql = """
        CREATE TABLE Users (
            userId int PRIMARY KEY NOT NULL,
            userName varchar(50),
            userFullName varchar(50) NOT NULL,
            userPhoneNumber varchar(20),
            userLastVideoNumberPython INT,
            userLastVideoNumberJS INT,
            userLastVideoNumberHTML INT,
            userLastVideoNumberCSS INT,
            userLastVideoNumberJava INT,
            userLastVideoNumberCPlusPlus INT,
            userLastVideoNumberBootstrap INT,
            userLastVideoNumberDoteNet INT,
            userLastVideoNumberDjango INT,
            userLastVideoNumberSass INT
            );
        """
        self.execute(sql, commit=True)

    def addUsers(self, userId: int, userName: str, userFullName: str, userPhoneNumber: str, userLastVideoNumberPython: str, userLastVideoNumberJS: str,
                 userLastVideoNumberHTML: str, userLastVideoNumberCSS: str, userLastVideoNumberJava: str, userLastVideoNumberCPlusPlus: str,
                 userLastVideoNumberBootstrap: str, userLastVideoNumberDoteNet: str, userLastVideoNumberDjango: str, userLastVideoNumberSass: str):
        sql = """
        INSERT INTO Users(userId, userName, userFullName, userPhoneNumber, userLastVideoNumberPython, userLastVideoNumberJS, userLastVideoNumberHTML,
        userLastVideoNumberCSS, userLastVideoNumberJava, userLastVideoNumberCPlusPlus, userLastVideoNumberBootstrap, userLastVideoNumberDoteNet,
        userLastVideoNumberDjango, userLastVideoNumberSass) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(userId, userName, userFullName, userPhoneNumber, userLastVideoNumberPython, userLastVideoNumberJS,
                                      userLastVideoNumberHTML, userLastVideoNumberCSS, userLastVideoNumberJava, userLastVideoNumberCPlusPlus,
                                      userLastVideoNumberBootstrap, userLastVideoNumberDoteNet, userLastVideoNumberDjango, userLastVideoNumberSass), commit=True)

    def selectUser(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.formatArgs(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def selectAllUsers(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def countUsers(self):
        return self.execute(f"SELECT COUNT(*) FROM Users;", fetchone=True)

    def updateUserLastVideoCSS(self, userId, newVideo):
        sql = """
        UPDATE Users SET userLastVideoNumberCSS = ? WHERE userId = ?;
        """
        self.execute(sql, (newVideo, userId), commit=True)

    def updateUserLastVideoPython(self, userId, newVideo):
        sql = """
        UPDATE Users SET userLastVideoNumberPython = ? WHERE userId = ?;
        """
        self.execute(sql, (newVideo, userId), commit=True)

    def updateUserLastVideoHTML(self, userId, newVideo):
        sql = """
        UPDATE Users SET userLastVideoNumberHTML = ? WHERE userId = ?;
        """
        self.execute(sql, (newVideo, userId), commit=True)

    def updateUserLastVideoBootstrap(self, userId, newVideo):
        sql = """
        UPDATE Users SET userLastVideoNumberBootstrap = ? WHERE userId = ?;
        """
        self.execute(sql, (newVideo, userId), commit=True)

    def updateUserLastVideoSass(self, userId, newVideo):
        sql = """
        UPDATE Users SET userLastVideoNumberSass = ? WHERE userId = ?;
        """
        self.execute(sql, (newVideo, userId), commit=True)

    def countUsers(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def deleteUser(self, userId):
        sql = "DELETE FROM Users WHERE userId=?"
        parameters = (userId,)
        self.execute(sql, parameters, commit=True)

    def dropTableUsers(self):
        self.execute("DROP TABLE Users", commit=True)


# def logger(statement):
#     print(f"""
# _____________________________________________________
# Executing:
# {statement}
# _____________________________________________________
# """)
