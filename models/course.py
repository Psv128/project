from odoo import models, fields

class Course(models.Model):
    _name = "academy.course"
    _description = "Curso"

    name = fields.Char(string="Nombre", required=True)
    price = fields.Float(string="Precio", required=True)
    student_ids = fields.One2many("academy.student", "course_id", string="Alumnos")
