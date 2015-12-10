import sublime, sublime_plugin

class createLabel(sublime_plugin.TextCommand):

	# thank you past joshua
    # you let us to this
    # https://github.com/joshuadelange/processSfLabels

	def run(self, edit):

		# we might have multiple regions 
		for region in self.view.sel():

			self.view.replace(edit, region, '{{l."' + self.view.substr(region) + '"}}')

			pass