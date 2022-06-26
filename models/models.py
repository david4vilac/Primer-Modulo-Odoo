from odoo import models, fields 

class Todo(models.Model):
    _name = "pr.todo"

    name = fields.Char("Nombre")
    status = fields.Selection(selection = [("borrador","Borrador"), ("hecho","Hecho")])