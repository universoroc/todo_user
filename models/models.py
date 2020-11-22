# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TodoUser(models.Model):
    _name = "todoroc_app.todoroc_app"
    _inherit = 'todoroc_app.todoroc_app', 'mail.thread'
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="What needs to be done?")

    def todo_app_do_clear_done(self):
        domain = [('is_done', '=', True),
                  '|', ('user_id', '=', self.env.uid),
                  ('user_id', '=', False)]
        dones = self.search(domain)
        dones.write({'active': False})
        return True

    def todo_app_do_toggle_done(self):
        for task in self:
            if task.user_id != self.env.user:
                raise ValidationError(
                    'Only the responsible can do this!')
        return super(TodoUser, self).todo_app_do_toggle_done()
