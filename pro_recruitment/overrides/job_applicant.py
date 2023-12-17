import frappe
import json

@frappe.whitelist()
def longListing(applicants):
    if isinstance(applicants, str): applicants = json.loads(applicants)
    
    for a in applicants:
        frappe.set_value("Job Applicant", a['name'], "custom_short_list", 1)

    return applicants
