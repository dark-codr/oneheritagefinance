import os

from django.conf import settings
from django.template.defaultfilters import slugify
from storages.backends.s3boto3 import S3Boto3Storage


class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = "media"
    default_acl = "public-read"
    file_overwrite = False


class ProtectedRootS3Boto3Storage(S3Boto3Storage):
    location = "protected"
    default_acl = "private"
    file_overwrite = False
    custom_domain = False


def get_logo_upload_folder(instance, pathname):
    "A standardized pathname for uploaded files and images."
    root, ext = os.path.splitext(pathname)
    return "{0}/logo/{1}/{2}{3}".format(
        "IMG", slugify(instance.name), slugify(root), ext
    )


def get_file_upload_folder(instance, pathname):
    "A standardized pathname for uploaded files and designs."
    root, ext = os.path.splitext(pathname)
    if instance.type == "FILE":
        return f"FILE/{instance.slug}/{slugify(root)}{ext}"
    else:
        return f"DESIGN/{instance.slug}/{slugify(root)}{ext}"


def get_training_video_upload_folder(instance, pathname):
    "A standardized pathname for uploaded training videos."
    root, ext = os.path.splitext(pathname)
    return f"TRAINING/{instance.training.slug}/{instance.id}/{instance.slug}/{slugify(root)}{ext}"
