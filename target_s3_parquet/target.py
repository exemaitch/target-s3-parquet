"""S3Parquet target class."""

from __future__ import annotations

from singer_sdk.target_base import Target
from singer_sdk import typing as th

from target_s3_parquet.sinks import (
    S3ParquetSink,
)


class TargetS3Parquet(Target):
    """Sample target for S3Parquet."""

    name = "target-s3-parquet"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "s3_path",
            th.StringType,
            description="The s3 path to write the parquet files to. Should be in the format s3://bucket/path",
            required=True,
        ),
        th.Property(
            "aws_access_key_id",
            th.StringType,
            description="AWS Access Key ID",
            required=True
        ),
        th.Property(
            "aws_secret_access_key",
            th.StringType,
            description="AWS Secret Access Key",
            required=True,
        ),
    ).to_dict()

    default_sink_class = S3ParquetSink


if __name__ == "__main__":
    TargetS3Parquet.cli()
