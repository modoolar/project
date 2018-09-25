# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).
{
    "name": "Project Workflow Default State Per Security Group",
    "summary": "This module enables default task states per security group.",
    "category": "Project",
    "version": "11.0.1.0.0",
    "license": "LGPL-3",
    "author": "Modoolar",
    "website": "https://www.modoolar.com/",
    "images": ["static/description/banner.png"],
    "depends": [
        "project_workflow_management"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/project_workflow_view.xml",
    ],
    "installable": True,
}
