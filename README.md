# Changer for Polish respect words
## Why use it?
Plugin is useful for change all Polish recpect words in selected text:

e.g.

**cię -> Cię**

## How to use it?
1. Clone and extract repository
2. Move file `ConvertBigPL.py` to directory:
   - Windows: `%AppData%\Roaming\Sublime Text 3\Packages\User`
   - Linux: `~/.config/sublime-text-3/Packages`
3. Run Sublime Text 3 and console (`ctrl`+`~`)
4. Run command: `view.run_command("tobigpl")`

## How to create Hotkey?
You can do own HK for plugin:
1. Go to **Preferences->Key Bindings**
2. In window of the right paste: `{ "keys": ["ctrl+shift+y"], "command": "tobigpl" }`
3. Now you are able to use `ctrl`+`shift`+`y` to change words.
