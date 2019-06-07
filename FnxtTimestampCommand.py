import sublime
import sublime_plugin
import time


class FnxtTimestampCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		content=time.strftime("%a %b %d, %Y %I:%M %p");
		self.view.run_command("insert_snippet",{"contents":content});
