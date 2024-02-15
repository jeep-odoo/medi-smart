from odoo import fields, models


class medismartAppointment(models.Model):
    _name = "medismart.appointment"
    _description = "medismart appointment model"
    _inherit = ["mail.thread", "mail.activity.mixin"]


    patient_id = fields.Many2one("medismart.patient", string="Patient", required=True)
    doctor_id = fields.Many2one("medismart.doctor", string="Doctor", required=True)
    appointment_date = fields.Datetime(default=fields.Datetime.now(), string="Date", tracking=True)
    purpose = fields.Selection(
        string="Purpose",
        selection=[
            ("general_checkup", "General Checkup"),
            ("accident", "Accident"),
            ("post_surgery_visit", "Post Surgery Visit"),
            ("pre_surgery_visit", "Pre Surgery Visit"),
            ("surgery", "Surgery"),
        ],
        required=True,
        default="general_checkup",
        tracking=True,
    )
    status = fields.Selection(
        string="Status",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Confirmed"),
            ("done", "Done"),
            ("cancel", "Canceled"),
        ],
        required=True,
        default="draft",
        tracking=True,
    )
    appointment_note = fields.Text(string = "Note")
