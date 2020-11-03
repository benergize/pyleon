# pyleon
My dumb way to package scripts.

Welcome to the fabulous world of pyleon, where all your dreams come true before your eyes. This is a dumb python script I wrote that takes scripts and puts them together in one file.

## Use Case

The problem:
I have files jane.js, dick.js, and bob.js. I want all of those files together in a single file called DJB.js, but I'm too lazy to open up a text editor and copy and paste them together every time I edit one of them.

The solution:
Good ol' pyleon to the rescue. This would be the config file for this scenario:

```
{
  "output": "DJB.js",
  "files": [
    "jane.js",
    "dick.js",
    "bob.js"
  ]
}
```

Run the command ``pyleon.py config.json`` and your scripts will be magically combined!

## "Ben, there are already tools that do this and they're better than this garbage."

Yes!
