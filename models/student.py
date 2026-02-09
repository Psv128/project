from odoo import models, fields, api

class Student(models.Model):
    _name = "academy.student"
    _description = "Alumno"

    name = fields.Char(string="Nombre", required=True)
    age = fields.Integer(string="Edad")
    course_id = fields.Many2one("academy.course", string="Curso")
    course_cost = fields.Float(string="Coste Curso", compute="_compute_course_cost", store=True)

    @api.depends('course_id')
    def _compute_course_cost(self):
        for student in self:
            if student.course_id:
                student.course_cost = student.course_id.price + 100
            else:
                student.course_cost = 0
