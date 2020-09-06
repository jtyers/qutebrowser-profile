# qutebrowser-profile

A simple wrapper script for qutebrowser that allows you to maintain different profiles, each with their own history and session state but sharing the same `config.py`.

## Why?

I use my system for different projects and purposes, such as *email*, *cloud development*, *web browsing* and so on. Using `qutebrowser-profile` I can keep all of these in separate qutebrowser profiles. (I in fact also keep them in separate i3 profiles via [i3-launcher](https://github.com/jtyers/i3-launcher) too, but that's another story).

## Installation

Clone this repository and add it to your `$PATH`.

The script depends on `dmenu`. Rofi is also supported and automatically used if available. You can also override, e.g. `--dmenu="rofi -dmenu"`.

## Getting started

To create a new profile, just call the script:

`qutebrowser-profile`

You'll get a rofi/dmenu prompt asking for a profile name. Type one in and hit enter, and qutebrowser will load your profile.

Note that:
* qutebrowser's window will have `[my-profile-name]` at the start, so you can easily distinguish different qutebrowsers loaded with different profiles
* qutebrowser loads configuration from the normal location (and all qutebrowsers share configuration regardless of profile, this includes quickmarks/bookmarks)
* other data, such as session history, cache, cookies, etc, will be unique to that profile

## Other options

Here's the full options list (also available with `--help`):

```
  qutebrowser-profile - use qutebrowser with per-profile cache, session history, etc

USAGE
  qutebrowser-profile [--list] [--choose [--only-existing] | --load <name> | --new <name>] [qutebrowser args]

  --choose, -c
    If specified, the user is asked to select a profile via dmenu. If dmenu returns an empty string or non-zero 
    exit code (eg user pressed escape instead of choosing an option) the operation is aborted and qutebrowser 
    is not opened.
 
    The user can choose any existing profile or type the name of a new profile into dmenu to load qutebrowser
    in a new profile. See --only-existing below to restrict this.
 
  --only-existing, -e
    If specified, and --choose is in operation, the user can only choose an existing profile.
 
  --list
    List all known profiles
  
  --dmenu
    Override location of dmenu. Rofi is autodetected without you needing to set this.
  
  --qutebrowser
    Override location of qutebrowser to call.

```

## Licence

MIT
