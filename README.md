## Purpose:
I made this quick and dirty script to automate resume applications or general form submissions. These days, most job applications don't have HTML that complies with browser built-in autofill. This creates a series of JS commands to automate some of the info filling. It will not work all the time; it depends heavily on the css selectors for the `<input>` and `<label>` tags in the website.

## How to use:
1. Clone the repo
2. run `python fill_info.py` and follow the directions. Your goal should be to feed it the shortest possible string that matches precisely with a piece of your data. For example, instead of "First Name: Daniel", just give it "first:Daniel" since it is more likely a website will include the shorter string in its css.
3. run `python create_js.py` and (optional) pipe to your clipboard