# -*- coding: utf-8 -*-

from odoo import models, fields


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    appointment_id = fields.Many2one('hospital.patient_appointment', string="Appointment")

    def action_cancel(self):
        for rec in self:
            rec.appointment_id['state'] = 'canceled'
