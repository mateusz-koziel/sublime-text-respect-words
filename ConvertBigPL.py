import sublime
import sublime_plugin
import re


def to_big_PL(text):
	small = ('ci', 'ciebie', 'cię', 'twoje', 'tobie', 'ty', 'twój', 'twojego', 'twego', 'twych', 'twojej', 'twoich', 'twoją')
	title = tuple(idx.title() for idx in small)
	changes = dict(zip(small,title))
	pattern = re.compile(r'\b(' + '|'.join(changes.keys()) + r')\b')
	return pattern.sub(lambda x: changes[x.group()], text)

def strip_wrapping_underscores(text):
    return re.sub("^(_*)(.*?)(_*)$", r'\2', text)

def run_on_selections(view, edit, func):
    for s in view.sel():
        region = view.word(s)
        text = strip_wrapping_underscores(view.substr(region))
        view.replace(edit, region, func(text))


class TobigplCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		run_on_selections(self.view, edit, to_big_PL)
