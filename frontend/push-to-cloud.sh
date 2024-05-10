#!/bin/bash

S3_BUCKET="tim-web-hosting"
CLOUDFRONT_DISTRIBUTION_ID="E26Q7XGH5SJ2D9"
BUILD_COMMAND="build"


# Build Angular project
echo "Build started"
npm run $BUILD_COMMAND

# Copy Angular dist folder to S3 bucket
echo "Copying build to S3 bucket"
aws s3 --recursive cp ./dist/angular-17-crud/browser s3://$S3_BUCKET/

# Invalidate CloudFront distribution
echo "Invalidating CloudFront distribution"
aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_DISTRIBUTION_ID --paths "/*"
