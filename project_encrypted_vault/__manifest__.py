# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

{
    "name": "Project Encrypted Vault",
    "summary": "This module integrates Encrypted Vault with Project",
    "category": "Project",
    "version": "11.0.1.0.0",
    "license": "LGPL-3",
    "author": "Modoolar",
    "website": "https://www.modoolar.com/",
    "images": ["static/description/banner.png"],
    "depends": [
        "project",
        "encrypted_vault",
    ],
    "data": [
        "security/security.xml",
        "views/project_project_view.xml",
        "views/encrypted_vault_view.xml",
    ],
    "application": False,
}
