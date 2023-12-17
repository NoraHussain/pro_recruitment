
frappe.ui.form.on('Job Opening', {
    refresh: async function(frm) {

        let labels = await frm.events.call_api();

        var df_field_label = frappe.meta.get_docfield("Applicants Selection Criteria", "field_label", cur_frm.doc.name);
		df_field_label.options =  labels.labels;
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
        let result = await cur_frm.events.call_api();
        var indexOfLabel =  result.labels.indexOf(d.field_label);
        d.field_name =  result.values[indexOfLabel];
        frm.refresh_fields()
    }
})