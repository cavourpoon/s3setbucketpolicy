def s3AllowPolicy(bucket,sourceip):
    sourceiprange=str(sourceip)+'/32'
    buketarn='arn:aws:s3:::{0}/*'.format(bucket)
    policy=  {
        "Version": "2012-10-17",
        "Id": "S3PolicyIPRestrict",
        "Statement": [
            {
                "Sid": "IPAllow",
                "Effect": "Allow",
                "Principal": {
                    "AWS": "*"
                },
                "Action": "s3:*",
                "Resource": buketarn,
                "Condition": {
                    "IpAddress": {
                        "aws:SourceIp": sourceiprange 
                    }
                }
            }
        ]
    }
    return policy