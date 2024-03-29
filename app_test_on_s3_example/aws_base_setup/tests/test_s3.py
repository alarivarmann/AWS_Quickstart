import pytest
import boto3
from moto import mock_s3
from aws_base_setup.s3 import download


# TESTING FROM CHILD DIR : IMPORT FAILS import s3

@pytest.yield_fixture(scope="session")
def mock_boto():
	mock_s3().start()
	output_str = "Something"
	resource = boto3.resource("s3")
	resource.create_bucket(Bucket="gdelt-open-data").put_object(Key="events/1979.csv", Body=output_str)
	yield resource
	mock_s3().stop()


def test_download(mock_boto):
	"""Test S3 download function"""
	resource = mock_boto
	res = download(resource=resource, bucket="gdelt-open-data",
				   key="events/1979.csv", filename="1979.csv")
	assert res == "1979.csv"
