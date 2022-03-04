## Purpose:
I made this quick and dirty script to automate resume applications or general form submissions. These days, most job applications don't have HTML that complies with browser built-in autofill. This creates a series of JS commands to automate some of the info filling. It will not work all the time; it depends heavily on the css selectors for the `<input>` and `<label>` tags in the website.

## How to use:
1. Clone the repo
2. run `python fill_info.py` and follow the directions. Your goal should be to feed it the shortest possible string that matches precisely with a piece of your data. For example, instead of "First Name: Daniel", just give it "first:Daniel" since it is more likely a website will include the shorter string in its css.
3. run `python create_js.py` and (optional) pipe to your clipboard with | clip or something nice.
4. Copy the output from step 3 and paste it into the console of whatever website you are submitting a form on. If it doesn't do any changes, the website probably used generic css selectors like `input-4` that make pattern matching much harder (not dirty enough).

### Sample output from create_js.py
  document.querySelectorAll("input[id*=school]").forEach((a) => a.value = "Purdue University");
  document.querySelectorAll("input[class*=school]").forEach((a) => a.value = "Purdue University");
  document.querySelectorAll("input[placeholder*=school]").forEach((a) => a.value = "Purdue University");
  document.querySelectorAll("label[id*=school] + input").forEach((a) => a.value = "Purdue University");
  document.querySelectorAll("label[id*=school] + input").forEach((a) => a.value = "Purdue University");
  document.querySelectorAll("label[id*=school] + input").forEach((a) => a.value = "Purdue 
  document.querySelectorAll("input[id*=svasv]").forEach((a) => a.value = "asffvas");
  document.querySelectorAll("input[class*=svasv]").forEach((a) => a.value = "asffvas");
  document.querySelectorAll("input[placeholder*=svasv]").forEach((a) => a.value = "asffvas");
  document.querySelectorAll("label[id*=svasv] + input").forEach((a) => a.value = "asffvas");
  document.querySelectorAll("label[id*=svasv] + input").forEach((a) => a.value = "asffvas");
  document.querySelectorAll("label[id*=svasv] + input").forEach((a) => a.value = "asffvas");
