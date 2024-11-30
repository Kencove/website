# Copyright 2023 Kencove
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "No Modal Search Header",
    "summary": """
        Enable search input in the page view and disable it in the modal view""",
    "version": "17.0.0.0.1",
    "license": "LGPL-3",
    "author": "Kencove,Odoo Community Association (OCA)",
    "maintainers": ["kobros-tech"],
    "website": "https://github.com/OCA/website",
    "depends": [
        "website", 
    ],
    "data": [
        "views/website_templates.xml",
    ],
    "installable": True,
    "auto_install": True,
}
