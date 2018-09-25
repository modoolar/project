# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo import models, fields


class EncryptedVault(models.Model):
    _inherit = 'encrypted.vault'

    project_id = fields.Many2one(
        comodel_name="project.project",
        string="Project",
        required=False,
        copy=False,
    )
