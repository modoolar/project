# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo import models, api, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    vault_ids = fields.One2many(
        comodel_name='encrypted.vault',
        inverse_name='project_id',
        string='Vaults'
    )

    vault_count = fields.Integer(
        compute='_compute_vault_count',
        string='Delivery Packages Count')

    @api.multi
    def _compute_vault_count(self):
        for project in self:
            project.vault_count = len(project.vault_ids)

    @api.multi
    def open_vaults(self):
        self.ensure_one()
        action = self.env.ref(
            'encrypted_vault.action_encrypted_vault'
        ).read()[0]

        action.update({
            'domain': [('project_id', '=', self.id)],
            'context': {
                'default_project_id': self.id,
            }
        })
        return action
