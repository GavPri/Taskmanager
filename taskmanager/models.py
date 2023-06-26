from taskmanager import db


class Category(db.Model):
    # schema for the category table
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship(
        "Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(slef):
        return "#{0} - Task : {1} | Urgent : {2}".format(
            self.id, self.task_name, self.is_urgent
        )


class Task(db.Model):
    # schema for task model
    id = db.Column(db.Integer, primary_key=TRUE)
    task_name = db.column(db.String(50), unique=True, nullable=False)
    task_description = db.column(db.Text(50), nullable=False)
    is_urgent = dbColumn(db.Boolean, default=False, nullable=False)
    due_date = db.column(db.date(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category_id", ondelete="CASCADE"), nullable=False)
