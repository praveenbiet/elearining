from typing import Optional

from minio import Minio
from minio.error import S3Error

from .config import get_settings
from .logger import get_logger

settings = get_settings()
logger = get_logger(__name__)

# Create MinIO client
minio_client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=True,
)


async def create_bucket(bucket_name: str) -> bool:
    """Create a MinIO bucket."""
    try:
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)
            logger.info(
                "Bucket created",
                extra={
                    "bucket": bucket_name,
                },
            )
            return True
        return False
    except S3Error as e:
        logger.error(
            "Failed to create bucket",
            extra={
                "bucket": bucket_name,
                "error": str(e),
            },
        )
        raise


async def upload_file(
    bucket_name: str,
    object_name: str,
    file_path: str,
    content_type: Optional[str] = None,
) -> bool:
    """Upload a file to MinIO."""
    try:
        minio_client.fput_object(
            bucket_name,
            object_name,
            file_path,
            content_type=content_type,
        )
        logger.debug(
            "File uploaded",
            extra={
                "bucket": bucket_name,
                "object": object_name,
            },
        )
        return True
    except S3Error as e:
        logger.error(
            "Failed to upload file",
            extra={
                "bucket": bucket_name,
                "object": object_name,
                "error": str(e),
            },
        )
        raise


async def download_file(
    bucket_name: str,
    object_name: str,
    file_path: str,
) -> bool:
    """Download a file from MinIO."""
    try:
        minio_client.fget_object(
            bucket_name,
            object_name,
            file_path,
        )
        logger.debug(
            "File downloaded",
            extra={
                "bucket": bucket_name,
                "object": object_name,
            },
        )
        return True
    except S3Error as e:
        logger.error(
            "Failed to download file",
            extra={
                "bucket": bucket_name,
                "object": object_name,
                "error": str(e),
            },
        )
        raise


async def get_presigned_url(
    bucket_name: str,
    object_name: str,
    expires: int = 3600,
) -> Optional[str]:
    """Get a presigned URL for an object."""
    try:
        url = minio_client.presigned_get_object(
            bucket_name,
            object_name,
            expires=expires,
        )
        logger.debug(
            "Presigned URL generated",
            extra={
                "bucket": bucket_name,
                "object": object_name,
            },
        )
        return url
    except S3Error as e:
        logger.error(
            "Failed to generate presigned URL",
            extra={
                "bucket": bucket_name,
                "object": object_name,
                "error": str(e),
            },
        )
        raise


async def delete_file(bucket_name: str, object_name: str) -> bool:
    """Delete a file from MinIO."""
    try:
        minio_client.remove_object(
            bucket_name,
            object_name,
        )
        logger.debug(
            "File deleted",
            extra={
                "bucket": bucket_name,
                "object": object_name,
            },
        )
        return True
    except S3Error as e:
        logger.error(
            "Failed to delete file",
            extra={
                "bucket": bucket_name,
                "object": object_name,
                "error": str(e),
            },
        )
        raise


async def list_files(
    bucket_name: str,
    prefix: Optional[str] = None,
) -> list[str]:
    """List files in a MinIO bucket."""
    try:
        objects = minio_client.list_objects(
            bucket_name,
            prefix=prefix,
        )
        return [obj.object_name for obj in objects]
    except S3Error as e:
        logger.error(
            "Failed to list files",
            extra={
                "bucket": bucket_name,
                "error": str(e),
            },
        )
        raise 