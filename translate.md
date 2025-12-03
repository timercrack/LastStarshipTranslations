# Format of language.csv

`Language.csv` is a Comma-Separated-Value text file in UTF-8 encoding. It must start with a header row which indicates columns for **state, key, svn, english, translation**.

**state**: NEW, MODIFIED, PREVIOUS, CURRENT, OBSOLETE

- NEW, it means that the string was recently added to the game and there is no translation for it yet.
- MODIFIED means that the English string was changed since the last time it was translated and maybe the translation needs to be updated too.
- PREVIOUS indicates the previous translation (or translations). These are typically for reference, and you should supply a translation for the MODIFIED key instead.
- CURRENT indicates the current translation for a particular string.
- OBSOLETE indicates old translations. These have been superceded by new translations. They are for reference only and should typically not be changed.

**key**: the language key (e.g. `newmainmenu_newgame`)

**svn**: the source code revision number (Subversion Revision) when this key's english was last updated. This is a kind of version number of the key. You can have several rows with the same key and the game should use the translation with the highest svn number. You should leave this value unmodified so that it is clear which version of the key the translation corresponds to.

**english**: the English text corresponding to the key.

**translation**: the translation itself.

## Double Quotes ""

Note that because language.csv is a comma-separated value text file, if there are any commas present in the English or the Translation, then the value should be surrounded by double quotes "".

For example, if the English was:

Hello, John.

Then in the language.csv file, it should have "" around it:

"Hello, John."

This is so that the game can tell which commas separate fields of the translation table and which are part of the text itself. Note that the enclosing double quotes ("") will be ignored by the game and won't render on the screen.

## Markers in the text

### Programmatic Placeholders

Some strings have markers in them. We use these to programmatically add information to strings while the game is running. They are an asterisk followed by a single letter (e.g. \*X). These markers must be kept as an asterisk followed by the given letter, but can be placed anywhere in the string.

For example, \*X might be the number of fuel containers on your ship, or it might be a monetary value. If it is not clear, please ask for more context.

There are some markers that are special:

- S\*X - a star system (e.g. NG11).
- $\*X - an amount of money. The game uses the format_currency key to format it accordingly.
- L\*X - the name of a star ship (e.g. PROCYON).
- R\*X -the name of an object type in game (e.g. Fuel, Crew, Docking Port).

### Escaped characters, e.g. \n

Some strings contain newline markers (written as \n) which should be left in appropriate places. They are used to start a new line and/or paragraphs.
