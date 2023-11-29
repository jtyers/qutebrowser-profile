# qutebrowser-profile

A simple wrapper script for qutebrowser that allows you to maintain different profiles, each with their own history and session state but sharing the same `config.py`.

## Why?

I use my system for different projects and purposes, such as *email*, *cloud development*, *web browsing* and so on. Using `qutebrowser-profile` I can keep all of these in separate qutebrowser profiles. (I in fact also keep them in separate i3 profiles via [i3-launcher](https://github.com/jtyers/i3-launcher) too, but that's another story).

## Installation

Clone this repository and add it to your `$PATH`.

The script depends on `dmenu`. Rofi is also supported and automatically used if available. You can also override, e.g. `--dmenu="rofi -dmenu"`.

### Arch Linux

There is a [package](https://aur.archlinux.org/packages/qutebrowser-profile-git/) available in the AUR:

```
yay qutebrowser-profile-git
```

## Getting started

To create a new profile, just call the script:

`qutebrowser-profile`

You'll get a rofi prompt asking for a profile name (if you don't have `rofi` installed, the script will try to use `dmenu`, and fallback to asking via the terminal). Type one in and hit enter, and qutebrowser will load your profile.

Note that:
* qutebrowser's window will have `[my-profile-name]` at the start, so you can easily distinguish different qutebrowsers loaded with different profiles
* qutebrowser loads configuration from the normal location (and all qutebrowsers share configuration regardless of profile, this includes quickmarks/bookmarks)
* other data, such as session history, cache, cookies, etc, will be unique to that profile

Credit to @ayekat for the inspiration for the approach.

## Other options

Here's the full options list (also available with `--help`):

```
  qutebrowser-profile - use qutebrowser with per-profile cache, session history, etc

USAGE
    Usage: qutebrowser-profile [OPTIONS] [QB_ARGS]...

    Options:
      --profiles-root TEXT            The directory to store profiles in
      --choose / --no-choose          Prompt the user to choose a profile, then
                                      launch it (try rofi, dmenu then fallback to terminal)
      --load TEXT                     Load the given profile (fails if profile
                                      does not exist, see --new)
      --new / --no-new                Allow --load to create a new profile if it
                                      does not exist
      --dmenu TEXT                    Override the location of dmenu/rofi when
                                      using --choose
      --only-existing / --no-only-existing
                                      Do not allow the user to specify a new (non-
                                      existent) profile during --choose
      -l, --list-profiles, --list / --no-list-profiles, --no-list
                                      List existing profiles
      --show-stdio / --no-show-stio   Show stdout/stderr from qutebrowser when it
                                      is launched
      --qutebrowser TEXT              Location of qutebrowser launcher
      --help                          Show this message and exit.
```

## Licence

MIT
