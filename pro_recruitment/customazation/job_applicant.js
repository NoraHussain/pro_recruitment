frappe.listview_settings["Job Applicant"] = {
	onload: function (me) {
    me.page.add_action_item('Short Listing', function() {

      const applicants = me.get_checked_items();

      console.log(applicants);

      // var url = `/app/job-applicant?custom_long_list=1`;
      // window.location.href = url;
  });
}
}

frappe.ui.form.on('Job Applicant', {
  
  refresh: function(frm) {
    
  },

  // Add new event handlers or override existing ones
  validate: function(frm) {
      // Your custom validation logic here
  },

  // Add more events or overrides as needed
});