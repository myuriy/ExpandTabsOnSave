# coding: utf-8
""" ExpandTabsOnSave SublimeText3 plugin """
import sublime_plugin


class ExpandTabsOnSave(sublime_plugin.EventListener):
    """Expand tabs / spaces on file save."""

    def on_pre_save(self, view):
        """ Run ST's 'expand_tabs' command when saving a file. """
        if view.settings().get('convert_tabspaces_on_save'):
            if view.settings().get('translate_tabs_to_spaces'):
                view.run_command('expand_tabs', {"set_translate_tabs": True})
            else:
                view.run_command('unexpand_tabs', {"set_translate_tabs": True})
