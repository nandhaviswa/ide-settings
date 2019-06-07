import sublime
import sublime_plugin
import datetime;


class FnxtAnnotateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		today=datetime.datetime.now();
		content="/**\n * \n * @see \n * @since "+today.strftime("%a %B %d, %Y %I:%M %p")+".\n */";
		# content="/**\n * \n * @see \n * @author nandha.viswanathan@sifycorp.com.\n * @since "+today.strftime("%a %B %d, %Y %I:%M %p")+".\n */";
		self.view.run_command("insert_snippet",{"contents":content});
