#!/usr/bin/env python
import sys

import boto3
import pandas as pd


# https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates

relevant_columns = [
    "Region",
    "Architecture",
    "CreationDate",
    "Description",
    "Hypervisor",
    "ImageId",
    "ImageLocation",
    "Name",
    "PlatformDetails",
    "RootDeviceType",
    "State",
    "VirtualizationType",
]

def get_regions():
    """Retrieve a list of regions from AWS."""
    # print("Getting regions...")
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    regions = [x['RegionName'] for x in response['Regions']]

    return regions


def get_images_from_region(region):
    """Get a list of images for a region."""
    # print(f"Getting images from {region}")
    ec2 = boto3.client('ec2')
    response = ec2.describe_images(
        Owners=["309956199498"],
        Filters=[
            {
                'Name': 'image-type',
                'Values': ['machine']
            }
        ]
    )

    images = [dict(item, Region=region) for item in response['Images']]
    return images

df = pd.DataFrame(columns=relevant_columns)

for region in get_regions():
    images = get_images_from_region(region)
    temp_df = pd.DataFrame(images, columns=relevant_columns)
    df = df.append(temp_df, ignore_index=True)

print(
    df.sort_values(by=["CreationDate"], ascending=False).to_html()
)
