import frappe
from frappe import _

from hrms.hr.doctype.job_opening.job_opening import JobOpening

class CustomJobOpening(JobOpening):
    def validate(self):
        super(CustomJobOpening, self).validate()

        filters = {
            "job_title" : self.name
        }
        
        for i in self.custom_auto_screening_criteria:
            if i.operator == '=':
                if filters.get(i.field_name, -1) != -1:
                    filters[i.field_name][1].append(i.value)
                else:
                    filters[i.field_name] =  [ "in", [i.value]]
            else:
                filters[i.field_name] =  [ i.operator, [i.value]]

        applicants = frappe.get_all("Job Applicant", filters=filters)

        # for applicant in applicants:
            # frappe.db.set_value("Job Applicant", applicant.name, "custom_long_list", 1)

        frappe.msgprint(str(applicants))
        

@frappe.whitelist()
def get_job_applicant_fields():
    excluded_field_types = [
        'Section Break', 'Column Break', 'Attach', 'Image',
        'Text', 'Long Text', 'HTML', 'Password',
        'Table', 'Barcode', 'Color', 'Read Only'
    ]

    docfields = frappe.get_all("DocField", filters={"parent": "Job Applicant"}, fields=["label", "fieldname", "fieldtype"])
    docCustomFields = frappe.get_all("Custom Field", filters={"dt": "Job Applicant"}, fields=["label", "fieldname", "fieldtype"])

    # Merge the results of both queries into a single list of fields
    fields = docfields + docCustomFields

    # Use a list comprehension to filter the fields
    filtered_fields = [field for field in fields if field['fieldtype'] not in excluded_field_types]

    # Extract labels and fieldnames using list comprehensions
    labels = [field['label'] for field in filtered_fields]
    fieldnames = [field['fieldname'] for field in filtered_fields]

    return {
        "labels": labels,
        "values": fieldnames
    }