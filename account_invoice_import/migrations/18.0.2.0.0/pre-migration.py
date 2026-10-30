# Copyright 2026 Akretion France (https://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade

_column_renames = {
    "res_partner": [("invoice_import_single_line", None)],
}

# XML parsing moved to the factur-x lib: these modules are not installable
# anymore. Merge them so that databases where they were installed don't keep
# them in "to upgrade" state.
_merged_modules = [
    ("account_invoice_import_ubl", "account_invoice_import"),
    ("account_invoice_import_facturx", "account_invoice_import"),
]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_columns(env.cr, _column_renames)
    openupgrade.update_module_names(env.cr, _merged_modules, merge_modules=True)
