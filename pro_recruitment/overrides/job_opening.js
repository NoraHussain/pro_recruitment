var fields = [];
frappe.ui.form.on('Job Opening', {
    fields_array : [],
    refresh: async function(frm) {
        fields_array = await frm.events.call_api();
        var df_field_label = frappe.meta.get_docfield("Applicants Selection Criteria", "field_label", cur_frm.doc.name);
		df_field_label.options =  fields_array.labels;
		frm.refresh_fields();
    },

    call_api: async function(){
        var result;
        await frappe.call({
            method: 'pro_recruitment.overrides.job_opening.get_job_applicant_fields',
        }).then(r=>{
            result = r.message;
        });
        return result;
    }
  });

  frappe.ui.form.on('Applicants Selection Criteria', {
	field_label: async function(frm, cdt, cdn){
        var d = locals[cdt][cdn];
        // let result = await cur_frm.events.call_api();
        var indexOfLabel =  fields_array.labels.indexOf(d.field_label);
        d.field_name =  fields_array.values[indexOfLabel];
        frm.refresh_fields();
    }       
})