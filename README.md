# Mezzanine File Collections

Mezzanine File Collection is a simple file container page type for the
Django / Mezzanine CMS.

The Mezzanine's core gallery module only deals with images. I got frustrated
with it, I quickly developed an alternative to handle any filetype.

Most of this app's code is directly inspired from the Mezzanine's core.

## Installation

Installation is quite simple.

    $ pip install mezzanine-file-collections

Add "mezzanine_file_collections" to your list of installed apps. Then migrate
your database. That's it.

## Usage

Once installed, just create a new "File collection", and upload your files
the usual way.

The default templates uses Bootstrap's media objects for a basic rendering,
but it's very easy to overwrite it. Just look into the template.
