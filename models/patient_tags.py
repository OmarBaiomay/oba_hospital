# -*- coding: utf-8 -*-

from odoo import models, fields


class Patient(models.Model):
    _name = 'hospital.patient.tags'
    _description = 'Patient Tags Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    active = fields.Boolean(string="Active", default=True, tracking=True)
    name = fields.Char(string="Name", required=True, tracking=True)
    color = fields.Integer(string="Color", tracking=True)
