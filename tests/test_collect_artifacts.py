import os
import shutil
import tempfile
import unittest

import beets.util
from beets import config
from beetsplug import copyartifacts


class CollectArtifactsPathTypesTest(unittest.TestCase):
    """Regression tests for beets 2.13+ path type handling."""

    def setUp(self):
        config.read(user=False, defaults=True)
        config['ignore'] = ['.DS_Store', 'Thumbs.db']
        self.temp_dir = beets.util.bytestring_path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(beets.util.syspath(self.temp_dir))
        config.clear()
        config._materialized = False

    def test_bytes_paths_with_string_ignore_patterns(self):
        """Item paths are bytes; config ignore patterns are strings."""
        album_path = os.path.join(self.temp_dir, b'the_album')
        os.makedirs(beets.util.syspath(album_path))
        open(beets.util.syspath(os.path.join(album_path, b'artifact.file')), 'a').close()
        open(beets.util.syspath(os.path.join(album_path, b'.DS_Store')), 'a').close()

        plugin = copyartifacts.CopyArtifactsPlugin()
        item = type('Item', (), {
            'artist': 'Tag Artist',
            'albumartist': 'Tag Artist',
            'album': 'Tag Album',
        })()
        source = os.path.join(album_path, b'track.flac')
        dest = os.path.join(
            self.temp_dir, b'libdir', b'Tag Artist', b'Tag Album', b'track.flac'
        )

        plugin.collect_artifacts(item, source, dest)

        files = plugin._process_queue[0]['files']
        self.assertIn(os.path.join(album_path, b'artifact.file'), files)
        self.assertNotIn(os.path.join(album_path, b'.DS_Store'), files)


if __name__ == '__main__':
    unittest.main()
