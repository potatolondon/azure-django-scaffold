module.exports = function(grunt) {
	var path = require('path');

	require('load-grunt-config')(grunt, {
		config: {
			configPath: path.join(process.cwd(), 'grunt'),
			build: 'staticfiles',
			ui: '{{ project_name }}/static',
			templates: '{{ project_name }}/templates'
		}
	});
};
