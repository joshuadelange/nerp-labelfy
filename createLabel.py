import sublime, sublime_plugin, re

class createLabelCommand(sublime_plugin.TextCommand):

    # thank you past joshua
    # you let us to this
    # https://github.com/joshuadelange/processSfLabels

    def run(self, edit):

        print("fire!")

        # we might have multiple regions 
        for region in self.view.sel():

            label_text = self.view.substr(region)
            label_camel_case = re.sub(r'\W+', '', ''.join(x for x in label_text.title() if not x.isspace()))[:80]

            self.view.replace(edit, region, '{{l.' + label_camel_case + '}}')

            self.view.insert(edit, self.view.size(), "\n" + label_camel_case + " : " + label_text + "\n")

            pass