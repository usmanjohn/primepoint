from whitenoise.storage import CompressedManifestStaticFilesStorage


class RelaxedManifestStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False
