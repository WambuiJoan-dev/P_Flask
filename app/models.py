from . import db

#user can have many posts- one to many r/ship
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



#many-many r/ship- a student can enroll n many courses and a course can have many students

#create an association table
student_course = db.Table('student_course',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
    )

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)

    courses = db.relationship('Course', secondary=student_course, backref='students')

#one to one r/ship - A user has one profile
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', backref=db.backref('profile', useList=False))

    def __repr__(self):
        return f'<User {self.username}>'